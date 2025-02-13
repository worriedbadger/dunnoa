class RecipeCalculator:
    def __init__(self):
        self.dry_material = 100
        self.water = 40
        self.portion_size = 40
        self.stain_percentage = 7

    def calculate_values(self):
        # Calculate total mixture
        total_mixture = self.dry_material + self.water

        # Calculate percentages
        dry_percentage = (self.dry_material / total_mixture) * 100
        water_percentage = (self.water / total_mixture) * 100

        # Calculate amounts in portion
        dry_in_portion = (self.portion_size * dry_percentage) / 100
        water_in_portion = (self.portion_size * water_percentage) / 100
        stain_amount = (dry_in_portion * self.stain_percentage) / 100

        return {
            'total_mixture': total_mixture,
            'dry_percentage': dry_percentage,
            'water_percentage': water_percentage,
            'dry_in_portion': dry_in_portion,
            'water_in_portion': water_in_portion,
            'stain_amount': stain_amount
        }

    def update_values(self):
        print("\nRecipe Ratio Calculator")
        print("-" * 30)
        
        try:
            self.dry_material = float(input("Enter dry material (g): "))
            self.water = float(input("Enter water (g): "))
            self.portion_size = float(input("Enter portion size (g): "))
            self.stain_percentage = float(input("Enter stain percentage (%): "))
        except ValueError:
            print("Please enter valid numbers!")
            return False
        return True

    def display_results(self):
        results = self.calculate_values()
        
        print("\nTotal Mixture Analysis")
        print("-" * 30)
        print(f"Total mixture: {results['total_mixture']:.2f}g")
        print(f"Dry material percentage: {results['dry_percentage']:.2f}%")
        print(f"Water percentage: {results['water_percentage']:.2f}%")
        
        print("\nPortion Calculations")
        print("-" * 30)
        print(f"Dry material in portion: {results['dry_in_portion']:.2f}g")
        print(f"Water in portion: {results['water_in_portion']:.2f}g")
        print(f"Stain amount needed: {results['stain_amount']:.2f}g")

def main():
    calculator = RecipeCalculator()
    while True:
        if calculator.update_values():
            calculator.display_results()
        
        if input("\nCalculate another recipe? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
