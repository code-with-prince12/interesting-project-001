class LogisticsBillingEngine:
    def __init__(self, client_name, base_currency):
        self.client_name = client_name
        self.base_currency = base_currency
        self.valid_manifests = []
        self.fraud_alerts = []

    def process_manifest(self, raw_packet):
        # Cleaning strings and extracting fields safely
        clean_id = raw_packet[0].strip()
        weight = raw_packet[1]
        destination = raw_packet[2].strip()
        status = raw_packet[3]

        clean_order = [clean_id, weight, destination, status]

        # Fraud Detection Logic (Weight validation)
        if clean_order[1] < 0:  
            self.fraud_alerts.append(raw_packet)
        else:
            self.valid_manifests.append(clean_order)
        
    def calculate_corporate_invoice(self):
        print("\n------ Processing Corporate Invoices & Surcharges ------")
        # Fixed variable name from weight to 'manifest' for professional clarity
        for manifest in self.valid_manifests:
            order_id = manifest[0]
            weight_val = manifest[1]

            # Tiered Pricing Algorithm
            if weight_val <=5 :
                base_price = weight_val * 100    
            else:
                base_price = weight_val * 80

                # 5% Fuel Surcharge addition
                final_price = base_price + (base_price * 0.05)
                print(f"Order {order_id} -> TOtal Invoice: {self.base_currency} {final_price:.2f}")

    def generate_audit_report(self):
        processed_count = len(self.valid_manifests)
        fraud_count = len(self.fraud_alerts)

        print("\n============== AUDIT REPORT ===============")
        print(f"Total Successfully processed Orders: {processed_count}")
        print(f"Total Fraudulent Attempts Intercepted: {fraud_count}")
        print("============================================")

# -------XECUTION BLOCK--------

amazon_data = [
    ["  ORD_AMZ_001  ", 4.5, "  Delhi_NCR  ", "In-Transit"],
    ["ORD_AMZ_002", -1.2, "Mumbai", "Flagged"], # Yeh fraud mein jaana chahiye!
    ["  ORD_AMZ_003  ", 12.0, "  Bangalore  ", "Delivered"]
]

engine = LogisticsBillingEngine("Amazon India B2B", "INR")

# Ingesting files into the pipeline:
engine.process_manifest(amazon_data[0])
engine.process_manifest(amazon_data[1])
engine.process_manifest(amazon_data[2])
engine.calculate_corporate_invoice()
engine.generate_audit_report()