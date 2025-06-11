# 📊 Job Application Tracker

A simple Python CLI app to track job applications and analyze your job search journey. Built using basic Python, file handling, and OOP principles. Includes a Power BI dashboard for visual insights.

---

## 🖥️ Features

- Add and track job applications via CLI
- View application history directly from the terminal
- Stores data in an Excel file (`job_data.xlsx`)
- Power BI dashboard for detailed analysis

---

## 🗃️ Data Fields

The Excel file includes the following columns:

- `Company`
- `Role`
- `Status` (Applied, Interviewed, Offer, Rejected, etc.)
- `Date Applied`

---

## 📈 Power BI Visuals Used

| Insight / Question                                                          | Visual Used               |
|-----------------------------------------------------------------------------|----------------------------|
| Total number of job applications                                           | `Card Visual`             |
| Number of applications per company                                         | `Bar Chart`               |
| Application status distribution (Applied, Interviewed, Offer, etc.)        | `Donut Chart / Pie Chart` |
| Applications over time (by week/month)                                     | `Line Chart`              |
| Applications per job role                                                  | `Horizontal Bar Chart`    |
| Status breakdown per company                                               | `Stacked Column Chart`    |
| Interview/Offer trends over time                                           | `Stacked Area Chart`      |
| Most successful companies by status outcome                                | `Funnel Chart`            |

---

## ▶️ How to Run the CLI App

1. Make sure you have Python 3 installed.
2. Run the main script:

```bash
python main.py
```

You can add new jobs and view previously logged ones via the terminal.

---

## 📂 File Structure

```
JobApplicationTracker/
├── main.py              # CLI interface
├── job_tracker.py       # Core logic
├── job_data.xlsx        # Excel data file
├── job application.pbix # Power BI dashboard file
└── README.md            # This file
```

---

## 👨‍💻 Author

- Created by [Middivari Charan Kumar Reddy]
- GitHub: [charankumar3009]

---