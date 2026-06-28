import numpy as np

class StockPulseOptimizer:
    def __init__(self, client_name, market_matrix):
        """
        Constructor to bind data inside the object (Encapsulation )
        """
        self.client_name = client_name
        self.matrix = market_matrix
        # Storing the array inside the class instance

    def validate_market_shape(self):
        """
        Validates whether the incoming financial data is structural 2D matrix
        """

        if self.matrix.ndim != 2:
            print("[ERROR] Invalid Matrix Dimensions!")
        else:
            print(f"[SUCCESS] Matrix validated successfully for client: {self.client_name}")

    def detect_volatile_days(self):
        """
        Uses high-performancee NumPy masking to find coordinate indices where
        stock price breaks the 500 resistance barrier without loops.
        """

        volatile_indices = np.argwhere(self.matrix > 500)
        print("\n--- High Volatility Days Detected (Row, Column Indices)---")
        print((volatile_indices))

    def calculate_average_pulse(self):
        """
        Calculates the historical baseline price for each company (Columns) 
        using axis=0 reduction
        """
        # axis=0 takes the mean vertically down the columns for individual companies
        company_averages = np.mean(self.matrix, axis=0)
        print("\n======= Enterprise Market Analysis Dashboard ========")
        print(f"Company Wise Historical Averages: {np.round(company_averages, 2)}")
    
# =====================================================
#            REAL-WORLD EXECUTION BLOCK
# =====================================================

# Days of stock prrices for 3 individual companies (Rows=Days, Columns=Companies)
wall_street_data = np.array([
    [120, 510, 300],
    [150, 490, 320],
    [110, 480, 550], 
    [130, 495, 310]
])

# Initializing engine with data inside the object safely
engine = StockPulseOptimizer("Prince Rajput", wall_street_data)

# Triggering Data Pipeline Methods
engine.validate_market_shape()
engine.detect_volatile_days()
engine.calculate_average_pulse()