# GitHub Stars Crawler 

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Automation-blueviolet)
![Status](https://img.shields.io/badge/Status-Production%20Ready-green)

> Automated, scalable pipeline to crawl GitHub stars, store data in PostgreSQL, and export CSV artifacts using **Python** and **GitHub Actions**.

---

## 1️⃣ Problem Understanding

The goal is to **continuously monitor GitHub repositories** and collect their star counts as a **real-time, updating data pipeline**.  

**Challenges solved:**  
- Efficiently handle thousands of repositories  
- Respect GitHub API **rate limits**  
- Maintain **data integrity** during updates  
- Prepare for **massive scale (500M+ repositories)**  

---

## 2️⃣ Architecture

A **modular end-to-end pipeline**:

