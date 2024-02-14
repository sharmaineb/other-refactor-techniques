# by Kami Bigdely
# Extract Class
class Recipe:
    def __init__(self, name, prep_time, is_veggie, food_type, cuisine, ingredients, recipe_steps):
        self.name = name
        self.prep_time = prep_time
        self.is_veggie = is_veggie
        self.food_type = food_type
        self.cuisine = cuisine
        self.ingredients = ingredients
        self.recipe_steps = recipe_steps

recipes = {
    'butternut squash soup': Recipe('Butternut Squash Soup', 45, True, 'soup', 'North African',
                                    ['butter squash', 'onion', 'carrot', 'garlic', 'butter', 'black pepper',
                                     'cinnamon', 'coconut milk'],
                                    '1. Grill the butter squash, onion, carrot and garlic in the oven until '
                                    'they get soft and golden on top 2. Put all in blender with '
                                    'butter and coconut milk. Blend them till they become puree. Then move the '
                                    'content into a pot. Add coconut milk. Simmer for 5 minutes.'),
    'shirazi salad': Recipe('Shirazi Salad', 5, True, 'salad', 'Iranian',
                            ['cucumber', 'tomato', 'onion', 'lemon juice'],
                            '1. Dice cucumbers, tomatoes, and onions. 2. Put all into a bowl. 3. Pour lemon juice. '
                            '4. Add salt. 5. Mix them thoroughly.'),
    'Home-made Beef Sausage': Recipe('Home-made Beef Sausage', 60, False, 'deli', 'All',
                                      ['sausage casing', 'regular ground beef', 'garlic', 'coriander seeds',
                                       'black pepper seeds', 'fennel seed', 'paprika'],
                                      '1. In a blender, blend coriander seeds, black pepper seeds, fennel seeds, '
                                      'and garlic to make the seasonings. 2. In a bowl, mix ground beef with the '
                                      'seasoning. 3. Add all the content to a sausage stuffer. Put the casing on '
                                      "the stuffer's funnel. Rotate the stuffer's handle (or turn it on) to make "
                                      'your yummy sausages!')
}

for recipe_name, recipe in recipes.items():
    print("Name:", recipe.name)
    print("Prep time:", recipe.prep_time, "mins")
    print("Is Veggie?", 'Yes' if recipe.is_veggie else "No")
    print("Food Type:", recipe.food_type)
    print("Cuisine:", recipe.cuisine)
    print("Ingredients:", ', '.join(recipe.ingredients))
    print("Recipe Steps:", recipe.recipe_steps)
    print("***")