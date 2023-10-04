'''4. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
      If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
      Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)'''


length = 5.5
total_area = 5.5**2
per_square_cost = 500

total_cost = total_area*per_square_cost

print("Total Cost:",total_cost)