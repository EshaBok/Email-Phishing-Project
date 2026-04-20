# CLEANSWEEP: Email Fraud Detection & EDA !!IN PROGRESS!!

CLEANSWEEP is a Python-based project focused on automated exploratory data analysis (EDA) and the detection of email phishing attempts. The system processes domain metadata and assigns safety scores to help identify fraudulent activity.

## 🛠️ Environment & Tools
- **OS:** Windows 11 (Development environment also configured for Arch Linux)
- **Editor:** VS Code / Neovim
- **Database:** SQLite3
- **Language:** Python (SQLAlchemy/Pandas for data handling)

## 📊 Database Schema
The project utilizes a local SQLite database to store and track domain reputations.

### Table: `domain and scores`
| Column | Type | Description |
| :--- | :--- | :--- |
| `id` | INTEGER | Primary Key (Auto-increment) |
| `domain` | TEXT | The URL or email domain being analyzed |
| `scores` | REAL | The calculated reputation score |

```sql
-- Schema Reference
CREATE TABLE "domain and scores" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain TEXT NOT NULL,
    scores REAL
);
