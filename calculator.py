import math

def calculate(fin_height, face_pitch, rows, tube_od):
    """
    Calculate feed counts and water flow parameters based on fin dimensions
    
    Args:
        fin_height: The height of the fin
        face_pitch: The face pitch
        rows: Number of rows
        tube_od: Outside diameter of the tube
    
    Returns:
        Dictionary containing the calculated values
    """
    # Calculate feed numbers
    max_number_of_feeds = math.floor((fin_height / face_pitch) * min(2, rows / 2))
    mid_number_of_feeds = math.floor(max_number_of_feeds / 2)
    min_number_of_feeds = math.floor(max_number_of_feeds / 4)
    
    # Calculate water flow parameters
    water_flow_area = min_number_of_feeds * math.pi * (tube_od ** 2) / 4
    water_flow_rate = 18.7 * water_flow_area
    
    return {
        "MaxNumberOfFeeds": max_number_of_feeds,
        "MidNumberOfFeeds": mid_number_of_feeds,
        "MinNumberOfFeeds": min_number_of_feeds,
        "WaterFlowArea": water_flow_area,
        "WaterFlowRate": water_flow_rate
    }

def main():
    print("Simple Heat Exchanger Calculator")
    print("-------------------------------")
    
    # Get user inputs
    fin_height = float(input("Enter fin height: "))
    face_pitch = float(input("Enter face pitch: "))
    rows = float(input("Enter number of rows: "))
    tube_od = float(input("Enter tube outside diameter (in): "))
    
    # Calculate the values
    results = calculate(fin_height, face_pitch, rows, tube_od)
    
    # Display results
    print("\nResults:")
    print(f"MaxNumberOfFeeds: {results['MaxNumberOfFeeds']}")
    print(f"MidNumberOfFeeds: {results['MidNumberOfFeeds']}")
    print(f"MinNumberOfFeeds: {results['MinNumberOfFeeds']}")
    print(f"WaterFlowArea: {results['WaterFlowArea']:.4f} square inches")
    print(f"WaterFlowRate: {results['WaterFlowRate']:.4f} inches")

if __name__ == "__main__":
    main()