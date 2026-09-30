class ReportService:
    # This makes a nice printable report of all the money stuff

    def generate_report(self, service):
        summary = service.get_summary()
        categories = service.category_summary()

        # Building the report text piece by piece
        report = "\n=======================================================\n"
        report += "                 MY FINANCIAL REPORT\n"
        report += "=======================================================\n"
        
        report += f"Total Money In  : Rs. {summary['income']}\n"
        report += f"Total Money Out : Rs. {summary['expense']}\n"
        report += f"Current Balance : Rs. {summary['balance']}\n"
        report += f"Savings Rate    : {summary['savings_rate']:.1f}%\n"
        
        report += "-------------------------------------------------------\n"
        report += "Where I spent my money:\n"
        report += "-------------------------------------------------------\n"

        if len(categories) > 0:
            for cat, amount in categories.items():
                # Removed the advanced <30 spacing for a simpler bullet point
                report += f"- {cat}: Rs. {amount}\n"
        else:
            report += "Haven't spent anything yet!\n"

        report += "=======================================================\n"
        
        return report