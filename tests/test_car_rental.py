import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from fastapi.testclient import TestClient
import main
import storage

class CarRentalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.data = Path(self.temp.name) / "data"
        shutil.copytree(Path(__file__).resolve().parents[1] / "data", self.data)
        self.patcher = patch.object(storage, "DATA_DIR", self.data)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)
        self.client = TestClient(main.app)
        self.addCleanup(self.client.close)

    def payload(self, **changes):
        result = {"customer_id": 2, "license_plate": "BE123456", "insurance_id": 1,
                  "start_date": "2026-11-01", "end_date": "2026-11-04"}
        result.update(changes)
        return result

    def test_young_driver_price_and_persistence(self):
        response = self.client.post("/rentals", json=self.payload())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["total_price"], 305.0)
        self.assertEqual(response.json()["young_driver_surcharge"], 50.0)
        self.assertEqual(len(self.client.get("/rentals").json()), 1)

    def test_invalid_dates_do_not_write(self):
        response = self.client.post("/rentals", json=self.payload(end_date="2026-10-31"))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.client.get("/rentals").json(), [])

    def test_overlapping_car_rejected(self):
        self.assertEqual(self.client.post("/rentals", json=self.payload()).status_code, 201)
        response = self.client.post("/rentals", json=self.payload(start_date="2026-11-03", end_date="2026-11-06"))
        self.assertEqual(response.status_code, 409)
        self.assertEqual(len(self.client.get("/rentals").json()), 1)

    def test_missing_reference(self):
        self.assertEqual(self.client.post("/rentals", json=self.payload(customer_id=999)).status_code, 404)

    def test_adult_no_surcharge(self):
        response = self.client.post("/rentals", json=self.payload(customer_id=1))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["total_price"], 255.0)

if __name__ == "__main__":
    unittest.main()
