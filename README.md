# Heat Exchanger Calculator

A simple Python calculator for heat exchanger parameters based on fin dimensions and tube specifications.

## Description

This calculator computes the following variables:
- MaxNumberOfFeeds = floor((FinHeight / FacePitch) * min(2, rows / 2))
- MidNumberOfFeeds = floor(MaxNumberOfFeeds / 2)
- MinNumberOfFeeds = floor(MaxNumberOfFeeds / 4)
- WaterFlowArea = MinNumberOfFeeds * π * tubeOD² / 4
- WaterFlowRate = 18.7 * WaterFlowArea

## How to Use

1. Run the calculator script:
   ```
   python calculator.py
   ```

2. Enter the requested values when prompted:
   - Fin height
   - Face pitch
   - Number of rows
   - Tube outside diameter (OD)

3. The program will calculate and display:
   - MaxNumberOfFeeds
   - MidNumberOfFeeds
   - MinNumberOfFeeds
   - WaterFlowArea
   - WaterFlowRate

## Example

```
Simple Heat Exchanger Calculator
-------------------------------
Enter fin height: 10
Enter face pitch: 2
Enter number of rows: 4
Enter tube outside diameter: 0.5

Results:
MaxNumberOfFeeds: 10
MidNumberOfFeeds: 5
MinNumberOfFeeds: 2
WaterFlowArea: 0.3927 square inches
WaterFlowRate: 7.3435 inches
```

## Formula Explanation

- **MaxNumberOfFeeds**: Maximum number of feeds based on fin height, face pitch, and rows
- **MidNumberOfFeeds**: Half of the maximum number of feeds
- **MinNumberOfFeeds**: Quarter of the maximum number of feeds
- **WaterFlowArea**: Flow area calculated using minimum feeds and tube dimensions
- **WaterFlowRate**: Water flow rate based on the flow area (constant 18.7)

## Notes

- All measurements should use consistent inches
- Results are rounded down to the nearest integer where appropriate