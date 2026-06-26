"""
Smart Delivery Logistics Automation Engine
Author: Prince Rajput (AI & Automation Engineer)
Description: A High- Performance procedural pipeline designed to parse raw server
logs, sanitize data, inputs and apply financial/security validation guardrails.
"""

# PHASE 1: RAW INGESTION DAYA BLOCK

# Raw unstructural logs streamed directly from the transactional server
raw_order_data = [
    "ORD101, prince_rajput, 1200, delivered",
    "ORD102, aman_maurya, 450, pending",
    "ORD103, divya_sharma, 2500, cancelled",
    "ORD104, rohit_singh, 80, DELIVERED",
    "ORD105, rahul_verma, -50, corrupted"
]

# PHASE 2: CORE PROCEDURAL FUNCTIONS (PIPELINES UTILITIES)

def parse_order(order_string):
    """
    Parses a raw comma-separated transaction string into a structured data schema.
    Applies string trimming and case normalization logic.
    """
    # Splitting string and removing whitespaces efficiently in one go 
    chunks = [chunk.strip() for chunk in order_string.split(",")]

    # Mapping structured chunks into an isolated dictionary payload
    dict_format = {
        "id": chunks[0], "name": chunks[1], "amount": float(chunks[2]), # Casting currency to data float representation
        "status": chunks[3].lower() # Standardizing status string tokens to lowercase
    }
    return dict_format
 

def check_order_security(order_dict):
    """
    Financial and Security guardrail engine.
    Evaluates transactional parameters to flag fraud risks and brand loyalty indicators.
    """
    # Guardrail 1: Flag invalid entries or absolute integer systemic corruption
    if order_dict["amount"] < 0 or order_dict["status"] == "corrupted":
        return "Failed/Fraud"
    
    # Guardrail 2: Premium Tier evaluation based on revenue contribution thresholds
    elif order_dict["amount"] > 1000 and order_dict["status"] == "delivered":
        return "PREMIUM ELIGIBLE"
    
    # Guardrail 3: Standard successfully processed telemetry state
    else:
        return "PROCESSED"
    
# PHASE 3: ORCHESTRATION ENGINE & EXECUTION RUNTIME

# Vault arrays initializing for production memory caching 
clean_order_vault = []

print("=== INITIATING LOGISTICS DATA PIPELINE PROCESSING ===")

# Running loop over bulk unstructured ingestion feeds
for line in raw_order_data:
    # Step 1: Parse and serialize unstructured string data
    data_box = parse_order(line)

    # Step 2: Pass serialized data objects directly to the security validator
    # FIXED OPTIMIZATION: Call function exactly once and reuse variables to save CPU registers
    checked_security = check_order_security(data_box)

    # Step 3: Mutate data objects to track security status inside metadata logs
    data_box["system_flag"] = checked_security

    #Step 4: Cache safe database registries into storage arrays

    clean_order_vault.append(data_box)

print("===== PIPELINE DISPATCH PROCESS COMPLETION =====\n")

# PHASE 4: ANALYTICS TERMINAL INTERFACE RENDERING
print("------------------ SYSTEM SECURITY DASHBOARD -------------------")
for order in clean_order_vault:
    # Formatting explicit display structurs using standardized variables
    print(f"CUSTOMER: {order["name"]} | Flag: {order["system_flag"]}")
print("-----------------------------------------------------------------")