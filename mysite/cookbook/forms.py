from django import forms

# These are used to generate the recipe categories in the dropdown box 
# on the recipe entry form
RECIPE_TYPES = [
        ('', 'Select'),
        ('Bread and Breakfast', 'Bread and Breakfast'),
        ('Appetizer', 'Appetizer'),
        ('Dessert', 'Dessert'),
        ('Recipe From Famous Person', 'Recipe From Famous Person'),
        ('Recipe For Kids', 'Recipe For Kids'),
        ('Holiday Recipe', 'Holiday Recipe'),
        ('Main Dish', 'Main Dish'),
        ('Miscellaneous - Jams, Sauces, Beverages', 
            'Miscellaneous - Jams, Sauces, Beverages'),
        ('Salad', 'Salad'),
        ('Side Dish - Vegetables', 'Side Dish - Vegetables'),
        ('Soup', 'Soup'),
]

class RecipeForm(forms.Form): 
    recipe_name = forms.CharField(label="Recipe Name", 
            widget=forms.TextInput(attrs={'class':'form-control',
                'placeholder':'Enter recipe name'}), max_length=100)
    recipe_type = forms.CharField(label='Recipe Category', 
            widget=forms.Select(choices=RECIPE_TYPES))
    author = forms.CharField(label="Author", 
            widget=forms.TextInput(attrs={'class':'form-control',
                'placeholder':'Enter author name'}), max_length=100)
    comment = forms.CharField(label="Comment", 
            widget=forms.Textarea(attrs={'class':'form-control',
                'placeholder':'Enter a short comment about the recipe',
                'rows':'5'}), max_length=500)
    ingredients = forms.CharField(label="Ingredients", 
            widget=forms.Textarea(attrs={'class':'form-control',
                'placeholder':'Enter ingredients with amounts, separated by'\
                        ' commas','rows':'5'}), max_length=2000)
    instructions = forms.CharField(label="Instructions",
            widget=forms.Textarea(attrs={'class':'form-control',
                'placeholder':'Enter instructions for recipe','rows':'5'}), 
                max_length=2000)

class NewUserForm(forms.Form):
    first_name = forms.CharField(label="First Name:", 
            widget=forms.TextInput(attrs={'cols':10, 'class':'form-control',
                'placeholder':'Enter First Name'}), max_length=100)
    last_name= forms.CharField(label="Last Name:", 
            widget=forms.TextInput(attrs={'class':'form-control',
                'placeholder':'Enter Last Name'}), max_length=100)
    username = forms.CharField(label="Username:", 
            widget=forms.TextInput(attrs={'class':'form-control',
                'placeholder':'Enter Username'}), max_length=100)
    password = forms.CharField(label="Enter Password:", 
            widget=forms.TextInput(attrs={'class':'form-control',
                'placeholder':'Enter Password'}), max_length=100)

class LoginForm(forms.Form):
    username = forms.CharField(label="Username:", 
            widget=forms.TextInput(attrs={'class':'form-control',
                'placeholder':'Enter Username'}), max_length=100)
    password = forms.CharField(label="Enter Password:", 
            widget=forms.TextInput(attrs={'class':'form-control',
                'placeholder':'Enter Password'}), max_length=100)
