import csv
from Test_Soup import ScrapLink


urls =[
"https://www.reliantplumbing.com/",
"https://www.plumbersthatcare.com/",
"https://sanddplumbing.com/?utm_source=google&utm_medium=organic&utm_campaign=GMB%20Listing%20Austin",
"https://www.theplumbmasters.com/",
"https://www.mrrooter.com/austin/?cid=LSTL_MRR000199&utm_source=gmb&utm_campaign=local&utm_medium=organic",
"http://www.bluedragonplumbing.com/",
"https://www.mooremoreplumbing.com/",
"https://www.danielsaustin.com/?utm_source=GMB&utm_medium=organic&utm_campaign=austin",
"https://www.clarkekentplumbing.com/"
]

if __name__ == "__main__":
    all_emails = set()  # Use a set to store unique emails

    # Loop through URLs
    for url in urls:
        scrappedEmails = ScrapLink(url)
        # Check if scrappedEmails is not None before processing
        if scrappedEmails:
            # Avoid duplicates by adding only new emails to the set
            all_emails.update(scrappedEmails)

    # Convert the set back to a list if needed
    all_emails_list = list(all_emails)


    # Specify the file name for the CSV
    csv_filename = 'emails.csv'

    # Writing all emails to CSV file
    with open(csv_filename, 'w', newline='') as csvfile:
        # Create a CSV writer
        fieldnames = ['Emails']
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header (optional)
        csv_writer.writeheader()

        # Write each email to a new row
        for email in all_emails:
            csv_writer.writerow({'Emails': email})

    print(f'CSV file "{csv_filename}" created successfully.')