# Car Rental Information System – FastAPI

Course assignment prototype adapted from the lecturer's **School-IS-api** teaching repository.

## Scenario and scope
A rental employee creates a rental linking one **Customer**, one **Car** and one **Insurance** option. The system validates dates, rejects overlapping car bookings and calculates the total price. The prototype uses fictional records and local JSON files, not a production database.

## Business rules and assumptions
- Rental end date is **exclusive**. Days = end date − start date; end date must be later than start date.
- Customer age is evaluated **on the rental start date**. Customers must be at least 18 (additional prototype assumption).
- Under age 23: **CHF 50 fixed surcharge per rental** (proposed assumption; confirm with group).
- Total = days × (car daily price + insurance daily cost) + surcharge.
- The same car cannot have overlapping rental periods; back-to-back rentals are allowed.
- Price fields are computed on creation and stored in the rental JSON. Price changes, concurrency and transaction handling are outside prototype scope.

## Files
| File | Purpose |
| --- | --- |
| `main.py` | FastAPI endpoints and input validation |
| `domain.py` | UML-aligned Customer, Car, Insurance and Rental classes |
| `storage.py` | Original JSON load/save functions (unchanged) |
| `run.py` | Original Uvicorn launcher (unchanged) |
| `data/*.json` | Fictional customer, car, insurance and rental data |
| `tests/test_car_rental.py` | Automated tests with isolated temporary data |

## Installation and start
Python 3.12+ recommended. From the project root:

```bash
python -m venv .venv
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python run.py
```

Open http://127.0.0.1:8000/docs (Swagger UI). GitHub Codespaces users can run `python run.py` and open forwarded port 8000 `/docs`.

## Endpoints
| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | `/customers`, `/customers/{customer_id}` | List / retrieve customers |
| GET | `/cars`, `/cars/{license_plate}` | List / retrieve cars |
| GET | `/insurance`, `/insurance/{insurance_id}` | List / retrieve insurance options |
| GET | `/rentals`, `/rentals/{rental_id}` | List / retrieve rentals |
| POST | `/rentals` | Create rental with validation and price calculation |

## Example successful request
In Swagger UI open `POST /rentals`, click **Try it out**, paste:

```json
{"customer_id":2,"license_plate":"BE123456","insurance_id":1,"start_date":"2026-11-01","end_date":"2026-11-04"}
```

**Expected response** (HTTP 201; assumes `data/rentals.json` starts as `[]`):

```json
{"rental_id":1,"customer_id":2,"license_plate":"BE123456","insurance_id":1,"start_date":"2026-11-01","end_date":"2026-11-04","rental_days":3,"customer_age":20,"young_driver_surcharge":50.0,"total_price":305.0}
```

Calculation: 3 × (CHF 75 + CHF 10) + CHF 50 = **CHF 305**.

## Invalid input and conflict tests
Invalid period (HTTP 400 expected): same payload but `end_date: "2026-10-31"`. Expected detail: `End date must be after start date`.

Overlapping rental (HTTP 409 expected): submit the successful example first, then a second request for `BE123456` with `start_date: "2026-11-03"`, `end_date: "2026-11-06"`. Expected detail: `Car is unavailable for the requested period`.

Unknown customer (HTTP 404 expected): use `customer_id: 999`.

To reset the demonstration, replace the contents of `data/rentals.json` with `[]`.

## Automated tests
```bash
python -m pip install -r requirements-test.txt
python -m unittest discover -s tests -v
```
### Testing and verification results

The application was manually tested in GitHub Codespaces on 28 October 2026 using the Swagger UI (`/docs`).

- **Application startup:** Successful; Swagger UI opened correctly.
- **Automated tests:** All 5 tests passed (`Ran 5 tests – OK`).
- **Successful rental creation:** POST `/rentals` returned HTTP 201. Rental ID 1 was created for customer 2 and car BE123456, from 2026-11-01 to 2026-11-04.
- **Price calculation:** 3 rental days, CHF 50 young driver surcharge, total CHF 305.
- **Rejected overlapping rental:** POST `/rentals` for the same car from 2026-11-03 to 2026-11-06 returned HTTP 409 Conflict.
- **Data persistence:** GET `/rentals` returned HTTP 200 and showed the saved rental.
- **Test isolation improvement:** The test setup now resets the temporary rentals file before each test, preventing demo bookings from affecting automated test results.

The application uses fictional data. These results were observed during testing, not merely assumed.

## Mapping models to implementation
- ER Customer / Car / Insurance / Rental → `domain.py` classes and matching JSON files.
- ER 1:N relationships → `customer_id`, `license_plate`, `insurance_id` references on Rental.
- Derived Age → `Customer.calculate_age()`; derived Total Price → `Rental.calculate_total_price()`.
- UML Create Rental → `POST /rentals`; invalid period and car conflict → HTTP 400 / 409.

### UML diagrams

- [Use Case Diagram](USE_CASE_DIAGRAM.mmd)
- [Class Diagram](CLASS_DIAGRAM.mmd)

## Limitations
No authentication, payment, customer self-service, cancellation, concurrent-write protection or relational database. Only `POST /rentals` writes data. Existing rentals keep calculated prices but the system does not snapshot all underlying rate details. Use only fictional data.

## Group members and contributions
- **Olivia Pécoud** – Collaborative development, testing, documentation, and project review.
- **Barbara Barta** – Collaborative development, testing, documentation, and project review.
- **Gian-Carlo Zimmermann** – Collaborative development, testing, documentation, and project review.
- **Michal Selecky** – Collaborative development, testing, documentation, and project review.

All four group members contributed equally to the project through teamwork, discussions, implementation, testing, and documentation.

## AI use and verification
AI tools, including ChatGPT (OpenAI) and Claude (Anthropic), were used by group members as supporting resources during the project. ChatGPT was used for code review, troubleshooting, test analysis, and documentation improvements. Claude was also used by some group members; its specific use cases have not been documented.
AI-assisted suggestions were reviewed and checked against the project's implementation. The application was successfully started in GitHub Codespaces, and the API was tested using Swagger UI (`/docs`).
All five automated tests passed. Manual testing confirmed successful rental creation (HTTP 201), rejection of overlapping bookings (HTTP 409), and retrieval of saved rental data (HTTP 200).
During verification, a test-data dependency was identified and corrected by resetting the temporary rentals file before each test. All five automated tests passed again after the correction.
The reported test results are based on actual execution rather than assumed or AI-generated outcomes.