fraud_words = ["urgent", "action required", "free", "congradulations"]
urgency_words = ["Now", "Urgency", "Deadline", "immediately", "fast", "act now", "hurry", "quick"]
financial_words = ["money", "cash", "prize", "winner", "lottery", "inheritance", "account", "invoice", "transfer"]
action_words = ["click here", "download", "open attachment", "provide information", "verify account", "update information", "verify attachment", "login"]

def scan_email_for_fraud(email):
   email = email.lower()
   score = 0
   for word in fraud_words:
      if word in email:
         score += 10
   for word in urgency_words:
      if word in email:
         score += 5
   for word in financial_words:
      if word in email:
         score += 8
   for word in action_words:
      if word in email:
         score += 6
   return score

def extracting_domain(email):
   domain = re.search(r'[\w\.-]+@([\w\.-]+)', email)
   if domain:
      return domain.group(1)
   else:
      return None

if __name__ == "__main__":
   email = input("Copy and enter the email content: ")
   emailscore = scan_email_for_fraud(email)
   if emailscore >= 15:
      print("This email is likely to be fraudulent.")
   else:
      print("This email is likely to be safe.")


