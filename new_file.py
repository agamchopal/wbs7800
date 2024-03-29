import nltk
nltk.download('punkt')  # For tokenization
nltk.download('stopwords')  # For stopwords
nltk.download('all')

nltk.download('vader_lexicon')
#import os

# Now you can use NLTK's functionalities
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import streamlit as st
import pandas as pd
import preprocessor
import Helper
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_option_menu import option_menu
import spacy
nlp = spacy.load("en_core_web_md")
nltk.downloader.download('vader_lexicon')
st.sidebar.header('Whatsapp Bussiness Visualizer')
st.download_button(label="Download",data="1/16/23, 2:11 AM - john: Good Quality Dog Food
1/16/23, 2:09 PM - john: Not as Advertised
1/15/23, 2:36 AM - john: "Delight" says it all
1/16/23, 3:18 AM - john: Cough Medicine
1/16/23, 3:12 PM - john: Great taffy
1/16/23, 0:47 AM - john: Nice Taffy
1/16/23, 0:15 AM - john: Great!  Just as good as the expensive brands!
1/16/23, 11:06 AM - john: Wonderful, tasty taffy
1/16/23, 7:13 AM - john: Yay Barley
1/16/23, 3:20 PM - john: Healthy Dog Food
1/13/23, 7:43 PM - john: The Best Hot Sauce in the World
1/15/23, 8:21 PM - john: My cats LOVE this "diet" food better than their regular food
1/16/23, 0:05 AM - john: My Cats Are Not Fans of the New Food
1/15/23, 10:01 PM - john: fresh and greasy!
1/15/23, 4:19 PM - john: Strawberry Twizzlers - Yummy
1/15/23, 2:34 PM - john: Lots of twizzlers, just what you expect.
1/16/23, 2:28 PM - john: poor taste
1/16/23, 1:37 PM - john: Love it!
1/16/23, 7:56 AM - john: GREAT SWEET CANDY!
1/16/23, 6:07 AM - john: Home delivered twizlers
1/16/23, 4:50 AM - john: Always fresh
1/16/23, 3:36 AM - john: TWIZZLERS
1/16/23, 2:28 AM - john: Delicious product!
1/16/23, 2:21 AM - john: Twizzlers
1/15/23, 11:51 PM - john: Please sell these in Mexico!!
1/15/23, 9:51 PM - john: Twizzlers - Strawberry
1/16/23, 10:10 AM - john: Nasty No flavor
1/16/23, 9:57 AM - john: Great Bargain for the Price
1/16/23, 11:54 AM - john: YUMMY!
1/13/23, 7:43 PM - john: The Best Hot Sauce in the World
1/16/23, 0:27 AM - john: Great machine!
1/15/23, 9:51 PM - john: THIS IS MY TASTE...
1/14/23, 11:09 AM - john: Best of the Instant Oatmeals
1/14/23, 11:58 AM - john: Good Instant
1/14/23, 2:26 PM - john: Great Irish oatmeal for those in a hurry!
1/15/23, 0:14 AM - john: satisfying
1/14/23, 6:47 PM - john: Love Gluten Free Oatmeal!!!
1/15/23, 8:00 AM - john: it's oatmeal
1/16/23, 3:12 PM - john: GOOD WAY TO START THE DAY....
1/16/23, 5:52 AM - john: Wife's favorite Breakfast
1/16/23, 2:03 AM - john: Why wouldn't you buy oatmeal from Mcanns? Tastes great!
1/16/23, 1:42 AM - john: Oatmeal For Oatmeal Lovers
1/15/23, 9:30 PM - john: Food-Great
1/15/23, 0:43 AM - john: Good Hot Breakfast
1/15/23, 0:01 AM - john: Great taste and convenience
1/14/23, 10:46 PM - john: Hearty Oatmeal
1/14/23, 7:19 PM - john: good
1/14/23, 9:21 PM - john: Mushy
1/14/23, 7:01 PM - john: Very good but next time I won't order the Variety Pack
1/16/23, 10:33 AM - john: Same stuff
1/14/23, 10:16 PM - john: Don't like it
1/15/23, 9:31 AM - john: HOT!  And good!  Came back for more  :)
1/16/23, 2:41 PM - john: You'll go nuts over Ass-Kickin' Peanuts.
1/15/23, 7:00 PM - john: not ass kickin
1/16/23, 7:20 AM - john: Roasts up a smooth brew
1/16/23, 2:49 PM - john: Our guests love it!
1/16/23, 7:20 AM - john: Awesome Deal!
1/16/23, 11:09 AM - john: How can you go wrong!
1/16/23, 6:46 AM - john: Awsome - Kids in neighborhood loved us!
1/16/23, 6:41 AM - john: great deal.
1/16/23, 6:18 AM - john: Better price for this at Target
1/16/23, 6:30 AM - john: pretty expensive
1/15/23, 1:35 AM - john: stale product.
1/16/23, 10:24 AM - john: Hammer Nutrition 's Fizz Rocks!
1/16/23, 10:26 AM - john: great source of electrolytes
1/16/23, 9:51 AM - john: Great for preventing cramps
1/16/23, 1:39 PM - john: Low Carb Alternative to Gatorade
1/16/23, 11:47 AM - john: Taste is not so good.
1/14/23, 0:47 AM - john: How much would you pay for a bag of chocolate pretzels?
1/14/23, 5:22 PM - john: pretzel haven!
1/15/23, 0:25 AM - john: Great Gummi!
1/15/23, 10:07 PM - john: Bigger then other brands
1/16/23, 8:36 AM - john: Best ever latice tart
1/16/23, 11:02 AM - john: Warning!  WARNING!  -ALCOHOL SUGARS!
1/15/23, 9:41 PM - john: nothing special
1/15/23, 6:10 PM - john: No Tea Flavor
1/16/23, 2:34 PM - john: Good
1/16/23, 2:29 PM - john: Taste great
1/16/23, 2:09 PM - john: Order only in cold weather
1/16/23, 1:35 PM - john: this is the best
1/16/23, 8:05 AM - john: Delicious!
1/16/23, 7:56 AM - john: Great
1/16/23, 8:13 AM - john: Forget Molecular Gastronomy - this stuff rockes a coffee creamer!
1/16/23, 1:23 AM - john: Natural Balance Lamb and Rice
1/16/23, 4:46 AM - john: INCREASED MY DOGS ITCHING
1/15/23, 11:08 PM - john: Great food!
1/16/23, 10:27 AM - john: Great for my dogs allergies
1/16/23, 6:54 AM - john: Great for stomach problems!
1/16/23, 4:20 AM - john: Better life for you dog!
1/16/23, 2:16 PM - john: Great Food
1/16/23, 10:56 AM - john: Great food for my my dog who has a sensitive stomach.
1/16/23, 10:49 AM - john: Great dog food
1/16/23, 10:32 AM - john: Mmmmm  Mmmmm good.
1/16/23, 9:27 AM - john: Great Dog Food!
1/16/23, 9:20 AM - john: So convenient
1/16/23, 6:41 AM - john: Good healthy dog food
1/16/23, 2:09 AM - john: Great dog food
1/16/23, 0:21 AM - john: Great allergy sensitive dog food, dogs love it
1/15/23, 11:48 PM - john: Perfect for our English Bulldog with Allergies
1/16/23, 9:46 AM - john: Bad
1/15/23, 6:30 AM - john: Taste wise it is a 6 star item
1/15/23, 1:01 PM - john: Great Support
1/16/23, 10:52 AM - john: TART!
1/16/23, 10:00 AM - john: Omaha Apple Tartlets
1/16/23, 8:26 AM - john: Loved these Tartlets
1/16/23, 3:31 AM - john: The best
1/15/23, 7:26 AM - john: disappointing
1/15/23, 11:48 PM - john: Wasting Vinegar on a Cucumber is a Shame!
1/15/23, 9:28 AM - john: Asparagus Bliss
1/16/23, 5:39 AM - john: My Idea of a Good Diet Food.
1/15/23, 11:26 AM - john: Low Carb Angel Food Puffs
1/16/23, 0:30 AM - john: Delicious tea
1/16/23, 11:39 AM - john: My every day green tea
1/16/23, 3:36 AM - john: the best tea ever... freah bright clean
1/16/23, 10:17 AM - john: Tea review
1/16/23, 8:29 AM - john: Wonderful Tea
1/16/23, 2:28 AM - john: Great cookies
1/16/23, 2:21 PM - john: Best everyday cookie!
1/15/23, 10:36 PM - john: So Far So Good
1/16/23, 7:49 AM - john: Best Cat Food
1/16/23, 3:46 AM - john: Great food.
1/16/23, 9:43 AM - john: Perfect Cat Food For Older Cats!
1/16/23, 4:45 AM - john: Good for Feline UTI
1/15/23, 11:02 PM - john: Palatable and healthy
1/16/23, 2:44 PM - john: Healthy & They LOVE It!
1/16/23, 0:46 AM - john: Wonderful food - perfect for allergic kitties
1/16/23, 10:36 AM - john: Holistic select cat food
1/16/23, 8:16 AM - john: Tastes great. Love Hot & Spicy. Bad price here.
1/16/23, 5:08 AM - john: My favorite ramen
1/16/23, 9:17 AM - john: It burns!
1/16/23, 9:34 AM - john: Amazing to the last bite.
1/16/23, 7:43 AM - john: Not for me
1/16/23, 1:13 PM - john: Great spicy flavor
1/16/23, 10:48 AM - john: Great value and convenient ramen
1/16/23, 10:43 AM - john: great flavor
1/16/23, 10:29 AM - john: Tastes great, but is cheaper locally.
1/16/23, 2:55 PM - john: Tastes awesome & looks beautiful
1/16/23, 0:47 AM - john: Happy Face
1/16/23, 9:12 AM - john: Simply the BEST!
1/15/23, 4:17 PM - john: Excellent Product/Life Saver
1/16/23, 5:08 AM - john: Nice snack
1/16/23, 1:36 AM - john: Good Licorice
1/15/23, 9:10 PM - john: I love these!!!!!!!!
1/15/23, 4:32 PM - john: Great for the kids!
1/15/23, 5:12 PM - john: Bite sized
1/15/23, 8:26 AM - john: Sweet with a nice kick!
1/15/23, 4:10 AM - john: BROKEN BOTTLE BOTTOMS!
1/16/23, 1:26 PM - john: Love the salsa!!
1/16/23, 3:05 PM - john: Ehhh...
1/16/23, 8:22 AM - john: awesome cornmeal
1/16/23, 0:37 AM - john: GREAT marinade!
1/16/23, 10:50 AM - john: Awesome stuff
1/16/23, 8:29 AM - john: tastes good
1/16/23, 8:02 AM - john: Rip off Price
1/15/23, 4:03 PM - john: JELL-O
1/16/23, 7:40 AM - john: Great flavor of Jell-o.
1/16/23, 8:48 AM - john: Great Deal
1/16/23, 2:51 PM - john: Great tasting sea salt WITH iodine
1/15/23, 2:00 PM - john: tastes very fresh
1/16/23, 5:31 AM - john: Simple but good
1/16/23, 7:30 AM - john: tasty!
1/16/23, 2:47 PM - john: Not the greatest tasting..
1/16/23, 2:31 PM - john: Not Bad
1/16/23, 2:28 PM - john: Right size, taste
1/15/23, 4:33 PM - john: Tasteless but low calorie
1/16/23, 11:48 AM - john: This stuff is sooooo good!
1/16/23, 10:35 AM - john: Best Stuff Ever
1/16/23, 1:43 PM - john: Very Low quality
1/16/23, 3:01 PM - john: Not Banana Runts
1/16/23, 1:49 PM - john: Banana Heads Not Banana Runts
1/16/23, 1:33 PM - john: Worked great!
1/15/23, 8:28 PM - john: Ricore forever
1/15/23, 2:35 PM - john: Delicious!
1/16/23, 1:35 PM - john: Fluffy, Soft, Delicious and Sugary Sweet
1/15/23, 7:46 PM - john: Great but not as good as it was back in the day as a teen
1/16/23, 1:06 AM - john: EXCELLENT LEMON JUICE
1/16/23, 8:06 AM - john: Great Product
1/16/23, 5:25 AM - john: Handy
1/15/23, 11:25 PM - john: ReaLemon Juice from Amazon.
1/16/23, 5:05 AM - john: relaxing, almost like something you smoke
1/16/23, 8:52 AM - john: Never paid that much !
1/16/23, 0:05 AM - john: Marley's Mellow Mood Lite - Half Tea Half Lemonade
1/16/23, 10:45 AM - john: Great product to help you sleep
1/15/23, 11:05 PM - john: Perfect for gluten-free chocolate chip cookies
1/15/23, 7:12 AM - john: Garbonzo  Bean Flour
1/16/23, 11:28 AM - john: yum falafel
1/16/23, 10:30 AM - john: Make a fresh fruit tart, light and beautiful
1/15/23, 7:22 AM - john: Miracle
1/16/23, 5:06 AM - john: not bad for instant healthy coffee
1/16/23, 0:23 AM - john: It's ok
1/16/23, 11:57 AM - john: I love it!
1/16/23, 11:44 AM - john: great taste and has health benefits!
1/16/23, 11:08 AM - john: Tastes Great. Arrived in 2 days!
1/16/23, 7:43 AM - john: Great for after lunch
1/15/23, 8:44 PM - john: Nice little mints, but pricey.
1/16/23, 1:13 AM - john: Altoids mini mints tins
1/15/23, 5:54 PM - john: Altoids Smalls-Wintergreen
1/15/23, 7:07 PM - john: Sugarfree...
1/15/23, 3:38 PM - john: Tasty!!
1/16/23, 1:32 PM - john: These mints are awesome!
1/16/23, 9:40 AM - john: Altoids Smalls
1/16/23, 6:51 AM - john: Love these! And reusable containers
1/16/23, 6:47 AM - john: Altoids
1/16/23, 5:48 AM - john: A huge hit at the office!
1/16/23, 7:20 AM - john: Love 'em, they're great!
1/15/23, 5:13 PM - john: Love these!
1/16/23, 5:19 AM - john: fresh!
1/16/23, 5:11 AM - john: Wintergreen Me
1/16/23, 5:08 AM - john: These just don't do it for me as breath mints
1/16/23, 0:54 AM - john: better than average, more expensive than average.
1/15/23, 4:12 PM - john: My cat loves it!
1/16/23, 5:16 AM - john: Great For Fat Cats and Senior Citizens
1/16/23, 4:01 AM - john: Nearly killed the cats
1/15/23, 2:57 AM - john: CHANGED FORMULA MAKES CATS SICK!!!!
1/16/23, 6:53 AM - john: Best by the case
1/15/23, 10:17 PM - john: Looking for a different flavor?
1/16/23, 0:01 AM - john: Price cannot be correct
1/16/23, 2:21 PM - john: More Hot/Spicy than McCormick's Brand
1/15/23, 3:41 PM - john: Ahmad Loose Imperial Blend Tea is great for the price
1/15/23, 5:26 PM - john: Nice tea
1/16/23, 3:14 PM - john: A fragrant tea
1/16/23, 4:04 AM - john: Best Ahmad Tea
1/16/23, 3:20 AM - john: My favorite tea
1/16/23, 9:40 AM - john: Best tea ever!
1/15/23, 8:13 PM - john: Not a real tea
1/15/23, 3:12 PM - john: DELICIOUS
1/16/23, 1:53 PM - john: Best Bloody Mary mixer
1/16/23, 11:42 AM - john: The Best
1/16/23, 10:33 AM - john: Mcclures bloody Mary mix
1/16/23, 1:46 PM - john: Not Good
1/16/23, 2:13 PM - john: Love this tea!
1/16/23, 10:30 AM - john: Really Nice Taste!
1/16/23, 1:14 PM - john: just give me some watermelon and citron sea salt
1/16/23, 1:14 PM - john: Furniture Polish Taste
1/16/23, 2:00 AM - john: Big tub o' salt
1/16/23, 1:45 AM - john: Taste is neutral, quantity is DECEITFUL!
1/16/23, 0:44 AM - john: Eukanuba puppy small breed dog food
1/16/23, 9:47 AM - john: High Quality... But it gave my dog wicked gas..
1/16/23, 9:33 AM - john: Great tasting green tea and such a great deal.
1/16/23, 3:11 PM - john: OMG best chocolate jelly belly
1/16/23, 9:38 AM - john: Excellent loose tea.
1/16/23, 7:43 AM - john: Good anytime hot tea
1/16/23, 1:52 AM - john: My everyday cup of Tea
1/15/23, 5:28 PM - john: This is what you get in the store
1/15/23, 6:11 PM - john: Ahmad Tea
1/15/23, 9:57 AM - john: Disappointed
1/16/23, 11:48 AM - john: Wonderful!
1/16/23, 3:02 PM - john: Best way to buy kcups
1/16/23, 0:25 AM - john: delicious
1/15/23, 5:02 PM - john: keeps you out of the dentest chair
1/16/23, 10:39 AM - john: Super!  SuperFoods are Super easy!
1/16/23, 4:37 AM - john: Pok Chops
1/16/23, 1:29 PM - john: Sad outcome
1/16/23, 2:08 PM - john: Best Energy Shot For Me
1/16/23, 0:10 AM - john: Don't Waste Your Money
1/16/23, 6:02 AM - john: If you can't handle caffeine, this is not for you.
1/16/23, 2:15 PM - john: Yum, Yummy, Yummier
1/16/23, 2:28 PM - john: Reeks like chemicals
1/16/23, 1:39 PM - john: Disappointed!
1/16/23, 2:34 PM - john: Great for Gluten-free lifestyle!!
1/16/23, 11:24 AM - john: my dog loves these
1/16/23, 0:43 AM - john: YUMMY
1/14/23, 8:25 PM - john: sugar in the raw
1/15/23, 11:47 PM - john: Manufacturing Problems Diminish Product
1/16/23, 0:10 AM - john: Good product but terrible agricultural practices
1/15/23, 5:08 AM - john: Sugar in the raw
1/15/23, 2:13 AM - john: Sugar in the raw
1/16/23, 1:19 PM - john: Lie!!!!
1/16/23, 11:08 AM - john: It's sugar..
1/16/23, 4:42 AM - john: Excellent but not perfect
1/16/23, 1:52 AM - john: Good product
1/16/23, 0:30 AM - john: You'll never use white sugar again.
1/16/23, 0:15 AM - john: Thanks for the review Scott
1/16/23, 0:12 AM - john: great
1/15/23, 9:08 PM - john: Awesome Sugar!
1/15/23, 2:13 PM - john: Great product - weak packaging
1/15/23, 0:15 AM - john: Excellent!
1/16/23, 1:14 PM - john: Excellent for G/F
1/16/23, 5:22 AM - john: Amazing!
1/15/23, 6:17 PM - john: Very tasty chips!
1/15/23, 5:25 PM - john: YUMMY
1/15/23, 10:32 AM - john: Excellent Taste
1/15/23, 7:48 PM - john: Over priced chips and lack rice taste
1/15/23, 8:36 PM - john: Rotel saves me on a daily basis
1/15/23, 2:29 PM - john: it's fabulous, but *not* from amazon!
1/15/23, 3:12 AM - john: too expensive
1/15/23, 7:42 PM - john: Not mild enough for me lol
1/15/23, 6:30 PM - john: Great Natural Energy
1/15/23, 7:36 PM - john: I like this stuff
1/15/23, 4:14 PM - john: Great Energy
1/15/23, 1:37 PM - john: Not sure
1/16/23, 4:14 AM - john: The best energy shot out there, smooth and organic!
1/16/23, 0:50 AM - john: Fantastic, natural energy
1/15/23, 11:39 PM - john: Way better than Guayaki!
1/15/23, 1:59 PM - john: Doesn't taste that good but provides you the energy
1/16/23, 7:24 AM - john: Rocket in a Bottle
1/16/23, 7:17 AM - john: This stuff works!!!
1/16/23, 10:52 AM - john: Favorite energy shot and all natural too!
1/16/23, 10:46 AM - john: natural energy boost
1/16/23, 6:47 AM - john: Best energy shot I have ever tasted!
1/16/23, 2:15 PM - john: The Best
1/16/23, 1:48 PM - john: Tested by a trucker
1/16/23, 1:32 PM - john: Good Stuff
1/16/23, 0:00 AM - john: Great energy drink without artificial ingredients
1/16/23, 10:23 AM - john: Flavor getting better, energy is great
1/16/23, 8:32 AM - john: So awful I can barely describe
1/15/23, 9:40 PM - john: could use only once
1/16/23, 2:45 PM - john: VANILLA TOOTSIE ROLLS
1/16/23, 0:53 AM - john: One of my Favoritte foods
1/16/23, 6:47 AM - john: Fantastic!
1/16/23, 2:31 AM - john: WOW
1/16/23, 1:12 PM - john: Very Dissapointed
1/16/23, 7:36 AM - john: what quantity is it!
1/16/23, 0:30 AM - john: Very Good Coffee
1/15/23, 10:26 PM - john: Very Tasty
1/15/23, 4:17 PM - john: Excellent coffee
1/16/23, 10:07 AM - john: Hot!
1/15/23, 11:16 AM - john: Hot and delicious
1/16/23, 3:11 PM - john: Swiss Chalet
1/16/23, 5:45 AM - john: Oyster Sauce
1/16/23, 2:36 AM - john: ABSOLUTELY DELICIOUS!
1/14/23, 0:34 AM - john: Great gag gift
1/15/23, 6:20 AM - john: arrived FAST
1/14/23, 9:23 PM - john: Penguin Pooper
1/14/23, 0:31 AM - john: Never Arrived
1/16/23, 1:42 PM - john: coffee-mate coffee creamer hazelnut
1/16/23, 0:48 AM - john: No broken creamers!
1/16/23, 0:23 AM - john: Shipped great
1/16/23, 11:06 AM - john: Better Packaging
1/16/23, 9:30 AM - john: coffee-mate creamer
1/16/23, 8:32 AM - john: Perfect for work
1/16/23, 2:57 PM - john: AWFUL
1/16/23, 11:15 AM - john: Pop-Tarts Work of Art
1/16/23, 6:51 AM - john: Yes, this is real excellent coffee!!!
1/16/23, 11:18 AM - john: Does not taste very good
1/16/23, 8:28 AM - john: No no
1/16/23, 3:10 PM - john: The king of all seasoning salts.
1/16/23, 1:42 PM - john: Toasted Sesame oil
1/16/23, 2:11 PM - john: Tasty, tasty tasty!
1/14/23, 0:41 AM - john: Love, Love, Love These!
1/15/23, 8:00 PM - john: great for eating whole foods, clean with veggie brush
1/14/23, 6:44 PM - john: Absolutely LOVE IT!!
1/14/23, 3:50 PM - john: Only good for ice
1/14/23, 1:58 PM - john: Great for teething
1/14/23, 1:58 PM - john: Wonderful idea-difficult to clean.
1/14/23, 1:26 PM - john: I wasn't that impressed
1/14/23, 0:34 AM - john: Love the Fresh Food Feeder!!
1/14/23, 11:24 PM - john: Great Beans!!!
1/14/23, 8:49 PM - john: Good stuff!
1/14/23, 3:28 PM - john: excellent - exactly what I expected
1/14/23, 4:14 PM - john: These are the Best!
1/16/23, 2:21 PM - john: Love Love Love
1/15/23, 1:36 PM - john: The product is great but the price is out of line
1/15/23, 7:39 PM - john: Swedish Pearl is not the same as  Belgian Pearl
1/15/23, 10:48 PM - john: Perfect!
1/16/23, 9:53 AM - john: great taste
1/16/23, 0:24 AM - john: Taste-tested by a wine maker
1/16/23, 6:56 AM - john: Excellent Everyday Olive Oil
1/16/23, 2:25 PM - john: Love Weavers, I am a fan.
1/16/23, 6:10 AM - john: Make My Day
1/16/23, 6:18 AM - john: Treat yourself to the best coffee!
1/16/23, 1:45 PM - john: Bitter
1/16/23, 8:54 AM - john: Drinking it now, love the latin america "aroma"
1/16/23, 7:46 AM - john: GREAT SNACK
1/16/23, 5:36 AM - john: Best Bar
1/16/23, 1:56 PM - john: Can't find anywhere else!
1/16/23, 11:52 AM - john: My New Granola Bar
1/16/23, 2:52 AM - john: Another Husband Favorite
1/15/23, 8:36 PM - john: Price surprise
1/15/23, 8:09 PM - john: Very Smooth Coffee - Highly Recommended
1/16/23, 8:38 AM - john: A saving grace for Green Mountain Coffee...
1/16/23, 4:49 AM - john: My favorite
1/16/23, 2:41 AM - john: Good Coffee
1/16/23, 0:50 AM - john: Nantucket blend k-cups
1/16/23, 2:24 PM - john: Fantastic Chicken Noodle soup
1/16/23, 0:12 AM - john: Greatest Oil since slice bread !!!!!!!
1/16/23, 4:36 AM - john: Best Ever!
1/16/23, 10:52 AM - john: Deliciously scrumptious
1/16/23, 3:02 PM - john: Heinz no more!
1/16/23, 11:15 AM - john: This is really good stuff
1/16/23, 11:09 AM - john: Disappointing
1/16/23, 3:41 AM - john: Waste of money
1/16/23, 4:43 AM - john: Porcini Mushrooms an excellent product
1/16/23, 10:52 AM - john: Excellent flavor, mostly large pieces
1/16/23, 8:09 AM - john: The Best
1/16/23, 7:46 AM - john: Good for the money
1/16/23, 6:24 AM - john: not the highest quality, but good for the price.
1/16/23, 4:30 AM - john: Fresh - Whole.. perfect
1/15/23, 11:51 PM - john: Fresh and Tasty
1/15/23, 7:00 AM - john: Valentine gift winner
1/15/23, 11:03 PM - john: Cat won't go near it!
1/15/23, 11:03 PM - john: Simply WIld Chick & Brown RIce for Cats
1/16/23, 2:47 AM - john: Ham Base
1/16/23, 2:12 PM - john: MSG Ham Base
1/14/23, 6:21 PM - john: Delisious Pancakes
1/15/23, 7:07 PM - john: A Great All Around Mix
1/15/23, 1:40 AM - john: Great mix
1/14/23, 11:57 PM - john: Perfect mix for egg-allergic!
1/14/23, 9:23 PM - john: Arrowhead Mills whole grain buttermilk Pancakes are easy!
1/15/23, 1:48 PM - john: Good for Egg Allergy
1/14/23, 5:39 PM - john: Love the product disappointed in the shipping.
1/14/23, 4:53 PM - john: poor item packaging
1/14/23, 11:22 PM - john: Awful
1/16/23, 1:01 PM - john: disappointing
1/15/23, 1:29 PM - john: Great Healthy Snack
1/14/23, 9:04 PM - john: Sweet and Soothing
1/15/23, 9:53 PM - john: minty flavor
1/16/23, 0:05 AM - john: Ingredients take about 2 seconds to read
1/15/23, 1:24 PM - john: A Fantastic & Healthy Product
1/16/23, 1:07 PM - john: Great product
1/16/23, 0:36 AM - john: Excellent tea!
1/16/23, 8:55 AM - john: french's roast'n bags
1/15/23, 8:15 PM - john: best roast ever
1/15/23, 3:20 PM - john: Franch's is the best
1/16/23, 1:45 AM - john: Double the pleasure!
1/16/23, 11:15 AM - john: VERY GOOD! Great taste and easy for a single guy!
1/16/23, 1:33 PM - john: An acquired taste!
1/16/23, 4:42 AM - john: Look elsewhere for your whole grains
1/16/23, 1:36 PM - john: Hey!
1/16/23, 0:53 AM - john: These are Famous for a reason.
1/16/23, 11:34 AM - john: Wow
1/16/23, 10:56 AM - john: God, I love these cookies!!!
1/16/23, 10:56 AM - john: Hard
1/16/23, 10:43 AM - john: Kettle potato chips:  Fully loaded baked potato
1/16/23, 10:37 AM - john: Fresh, Lightly-Spiced, Crunchy Kettle Chips. Good Value, Good Product.
1/16/23, 10:33 AM - john: glad to find them in 1 oz size
1/16/23, 10:33 AM - john: pretty good, could be better
1/16/23, 10:27 AM - john: a slight taste of jalapeno
1/16/23, 9:57 AM - john: Best chips ever
1/16/23, 9:44 AM - john: Kettle potato chips:  Sweet onion
1/16/23, 9:41 AM - john: Ridiculously Good
1/16/23, 8:51 AM - john: Delicious!
1/16/23, 8:42 AM - john: PUCKER UP
1/16/23, 8:31 AM - john: I love these chips.  They are thick and crunchy!
1/16/23, 8:21 AM - john: Quite good
1/16/23, 8:21 AM - john: Delicious
1/16/23, 8:15 AM - john: Salty and vinegary!!!
1/16/23, 7:26 AM - john: WOW!!!!
1/16/23, 7:09 AM - john: Best gluten-free dairy-free chips
1/16/23, 5:28 AM - john: A unique flavor for fans of Thai food
1/16/23, 2:25 AM - john: Honey Dijon leaves bad aftertaste, NY Cheddar are pretty good
1/16/23, 2:24 AM - john: Yowzah!!
1/16/23, 1:22 AM - john: Very good.
1/16/23, 1:16 AM - john: Excellent!
1/16/23, 0:31 AM - john: Tangy goodness.
1/16/23, 0:25 AM - john: Heavy on the Vinegar
1/15/23, 11:58 PM - john: A delicious, crisp chip with good flavor
1/15/23, 11:03 PM - john: BEST BUY in BBQ Chips
1/15/23, 10:29 PM - john: Love Them!
1/15/23, 10:24 PM - john: Crunchy and Tasty
1/15/23, 10:06 PM - john: Convenience at low cost
1/15/23, 10:01 PM - john: An Acquired Taste
1/15/23, 9:36 PM - john: Best deal ever!
1/15/23, 7:59 PM - john: Yum!
1/15/23, 3:51 PM - john: Barbeque perfection
1/15/23, 3:05 PM - john: Excellent Thai-flavored chip
1/15/23, 1:32 PM - john: Best Kettle Chips!
1/15/23, 1:27 PM - john: The Supreme Salt & Vinegar
1/15/23, 0:54 AM - john: Delicious as always!
1/15/23, 11:24 AM - john: OooH Yummy!
1/15/23, 11:03 AM - john: Not quite the best...
1/15/23, 9:51 AM - john: want to gaain twenty pounds with no control whatsoever? Buy this!
1/15/23, 9:50 AM - john: One of Their Best Flavors
1/15/23, 9:44 AM - john: Love these chips!
1/15/23, 7:42 AM - john: Highly addicitive chips
1/15/23, 6:12 AM - john: These are AWESOME!
1/15/23, 6:08 AM - john: One bite and you'll become a "chippoisseur"
1/15/23, 6:08 AM - john: Crunchy, salty, sweet...finally, a Superbowl snack that scooores!
1/15/23, 6:05 AM - john: These chips make me weak at the knees
1/15/23, 3:17 AM - john: By far my favorite chips
1/15/23, 3:11 AM - john: Good chips, more cheese
1/15/23, 2:49 AM - john: Pretty good tasting chip
1/15/23, 2:09 AM - john: Yummy chips
1/15/23, 2:09 AM - john: Best sour cream & onion chip I've had
1/15/23, 2:06 AM - john: Great chips
1/15/23, 2:03 AM - john: Fabulous!
1/15/23, 1:46 AM - john: Box-o-Chips
1/15/23, 1:37 AM - john: fantastic!you can not beat this taste and you can not resist to it only one if you are spice lover
1/15/23, 1:35 AM - john: An addictive potato chip
1/15/23, 1:35 AM - john: Great Chip!
1/15/23, 1:33 AM - john: Excellent balance of taste, crunchiness, and moisture
1/15/23, 1:33 AM - john: Yum
1/15/23, 1:32 AM - john: Very good chips at a great price.
1/15/23, 1:26 AM - john: 70% of the chips in the bag are over cooked
1/15/23, 1:24 AM - john: Great chips!
1/15/23, 1:13 AM - john: Not bad but a little hard to get used to
1/15/23, 1:13 AM - john: Firm quality chip
1/15/23, 1:12 AM - john: Not  Very Creamy or Chivey...
1/15/23, 0:59 AM - john: Prefer other flavors
1/15/23, 0:47 AM - john: These will be habit forming!
1/15/23, 0:20 AM - john: Good and tangy
1/14/23, 11:11 PM - john: the best chips ever
1/14/23, 10:20 PM - john: I do not even like kettle chips and I love these
1/14/23, 10:20 PM - john: You have to love sea salt and vinegar already
1/14/23, 10:17 PM - john: Addictive
1/14/23, 9:43 PM - john: amazing chips
1/14/23, 8:25 PM - john: Best Chip Ever
1/14/23, 5:36 PM - john: Tangy, spicy, and sweet- oh my!
1/14/23, 4:56 PM - john: An indulgence with a bite
1/14/23, 4:43 PM - J. Baker: The best I've had
1/14/23, 1:55 PM - J. Baker: Excellent chip!
1/15/23, 1:13 AM - J. Baker: salt and vinegar chips
1/16/23, 2:45 PM - J. Baker: Delicious!!
1/16/23, 8:52 AM - J. Baker: I like them.
1/16/23, 5:44 AM - J. Baker: Love Kettle Chips
1/15/23, 11:02 PM - J. Baker: Best unsalted chips
1/15/23, 9:43 PM - J. Baker: So Delicious...Yet my companions wont touch them.
1/15/23, 10:36 AM - J. Baker: Love Kettle Chips, but not this flavor!
1/15/23, 6:36 AM - J. Baker: Maybe the worst chips ever.
1/15/23, 11:58 AM - J. Baker: Surprise 1  It's different...
1/14/23, 9:31 PM - J. Baker: Tasty
1/16/23, 5:06 AM - J. Baker: Crisp
1/16/23, 0:17 AM - J. Baker: Vinegar... Not my taste!
1/15/23, 11:00 PM - J. Baker: spicy thai chips
1/15/23, 10:40 PM - J. Baker: Delicious, what else did you expect?
1/15/23, 10:37 PM - J. Baker: Great Value
1/15/23, 7:17 PM - J. Baker: I have had better "Jalapeno Kettle Chips"
1/15/23, 3:23 PM - J. Baker: Spicy but good
1/15/23, 2:28 PM - J. Baker: boulder salt and malt vinegar chips are way better
1/15/23, 1:36 PM - J. Baker: POTATO CHIPS
1/15/23, 0:40 AM - J. Baker: Lightly Salted, Heavily Delicious!
1/15/23, 11:34 AM - J. Baker: Too Much Flavor
1/14/23, 11:18 PM - J. Baker: Love at first bite!  Tongue-puckering tang and crunch!
1/14/23, 5:19 PM - J. Baker: The Best Chips...PERIOD!
1/14/23, 9:30 PM - J. Baker: Delicious Extra Crunchy
1/15/23, 6:07 AM - J. Baker: Chip snob alert!
1/14/23, 10:04 PM - J. Baker: Best Salt & Vinegar!
1/14/23, 2:18 PM - J. Baker: Gourmet powerful Salt & Vinegar chips!
1/15/23, 0:20 AM - J. Baker: They changed the Chips now they taste horrible
1/16/23, 8:48 AM - J. Baker: Do not miss the salt!
1/15/23, 7:01 AM - J. Baker: Great deal
1/15/23, 1:23 AM - J. Baker: Best Chips out there!!!
1/15/23, 2:55 AM - J. Baker: Great price, but not as tangy as I expected.
1/15/23, 1:14 AM - J. Baker: burnt
1/14/23, 4:56 PM - J. Baker: Gaaak!  An "extreme" potato chip...!
1/15/23, 9:00 PM - J. Baker: Kettle Chips
1/16/23, 11:29 AM - J. Baker: Absotively, Posilutely Delicious
1/16/23, 9:57 AM - J. Baker: Gone down hill
1/16/23, 9:02 AM - J. Baker: completely ripped off
1/16/23, 3:37 AM - J. Baker: C H I P.....C H I P.....H O O R A Y....!!!!!  :  )  ( B A C K Y A R D.....B A R B E C U E )
1/15/23, 9:50 AM - J. Baker: Not the Best
1/15/23, 9:07 PM - J. Baker: STALE.  Beware buying these on special!
1/14/23, 11:49 PM - J. Baker: THESE ARE VERY GOOD
1/16/23, 9:08 AM - J. Baker: USED to be my favorite chips
1/16/23, 9:00 AM - J. Baker: Stale, Rancid Oil Taste, And if You Like Even the Tiniest Bit of Salt Flavor on Your Chips...
1/16/23, 3:01 AM - J. Baker: Disgusting
1/15/23, 9:28 PM - J. Baker: Taste terrible, way too strong
1/15/23, 2:34 PM - J. Baker: Over-fried
1/15/23, 1:10 PM - J. Baker: No salt Kettle chips.
1/14/23, 9:12 PM - J. Baker: Not as good as the English sell
1/15/23, 8:09 AM - J. Baker: VERY DISAPPOINTED
1/15/23, 5:36 PM - J. Baker: dripping in oil
1/15/23, 8:52 PM - J. Baker: Not so good.
1/15/23, 7:03 AM - J. Baker: Bags O' Salt with chips added.
1/15/23, 1:37 AM - J. Baker: Chips
1/16/23, 9:38 AM - J. Baker: Garbage
1/15/23, 4:48 AM - J. Baker: They're Not Madhouse Munchies!!!
1/15/23, 10:00 PM - J. Baker: Too SOUR!
1/15/23, 9:17 PM - J. Baker: AWFUL TASTE
1/14/23, 6:12 PM - J. Baker: delicious
1/16/23, 1:45 AM - J. Baker: Kettle has sold out, the chips are horrible now
1/16/23, 0:46 AM - J. Baker: The bags were damaged with holes and stains.
1/15/23, 11:31 PM - J. Baker: Kettle Chips Make Great Mouse Food
1/14/23, 10:26 PM - J. Baker: orgasmic
1/14/23, 7:13 PM - J. Baker: A tang that packs a punch!
1/14/23, 2:24 PM - J. Baker: great (hot) new flavor....
1/16/23, 10:27 AM - J. Baker: HORRIBLE I CANT BELIEVE THIS!
1/16/23, 9:11 AM - J. Baker: Favorite Kettle flavor and a great value!
1/16/23, 8:18 AM - J. Baker: Kettle Brand Potato Chips - New York Cheddar
1/16/23, 7:36 AM - J. Baker: My favorite flavor
1/16/23, 6:02 AM - J. Baker: So much flavor your farts will smell like sweet onions
1/15/23, 11:48 AM - J. Baker: Great Chip!
1/15/23, 8:31 AM - J. Baker: Awesome and delicious!
1/15/23, 7:58 AM - J. Baker: The only thing I have ever been addicted too...these chips!
1/15/23, 6:08 AM - J. Baker: One bite and you'll become a "chippoisseur"
1/15/23, 3:43 AM - J. Baker: Good chips
1/16/23, 6:01 AM - J. Baker: what happened? the recipe has changed
1/15/23, 11:02 AM - J. Baker: YUM! If you want a snack, have something REALLY good!
1/16/23, 2:55 PM - J. Baker: a good buy
1/16/23, 2:47 PM - J. Baker: Yoli
1/16/23, 2:38 PM - J. Baker: Good chips
1/16/23, 2:29 PM - J. Baker: Awesome
1/16/23, 1:20 PM - J. Baker: burns the skin off your lips
1/16/23, 11:51 AM - J. Baker: Great chips with very low sodium
1/16/23, 10:33 AM - J. Baker: Kettle Chips
1/16/23, 10:27 AM - J. Baker: Spicy Thai
1/16/23, 8:55 AM - J. Baker: smiles
1/16/23, 8:52 AM - J. Baker: My favorite Kettle Chip
1/16/23, 8:47 AM - J. Baker: Best salt & vinegar chips out there!
1/16/23, 8:45 AM - J. Baker: Amazing Service
1/16/23, 3:44 AM - J. Baker: Crunchy and spicy.
1/16/23, 2:55 AM - J. Baker: Pretty tasty and decently spiced. . . .
1/15/23, 11:16 PM - J. Baker: Great Tasting Chips
1/15/23, 10:10 PM - J. Baker: Kettle Chips, Sea Salt
1/15/23, 9:51 PM - J. Baker: Good deal but close expiration date!
1/15/23, 7:43 PM - J. Baker: GREAT TASTING CHIPS
1/15/23, 3:53 PM - J. Baker: Buy These, Eat These, Be Happy!
1/15/23, 1:13 PM - J. Baker: Eating them for years.
1/15/23, 10:58 AM - J. Baker: These chips will make you fat
1/15/23, 10:13 AM - J. Baker: Like Spice? Get these
1/15/23, 9:50 AM - J. Baker: Fantastic
1/15/23, 9:04 AM - J. Baker: Sweet, salty, tangy: the way a snack should be
1/15/23, 7:37 AM - J. Baker: One bite and you'll become a "chippoisseur"
1/15/23, 5:29 AM - J. Baker: One bite and you'll become a "chippoisseur"
1/15/23, 2:32 AM - J. Baker: Some of the best chips anywhere
1/15/23, 2:08 AM - J. Baker: the defacto standard for Salt and Vinegar chips
1/15/23, 2:06 AM - J. Baker: Yummy!
1/15/23, 1:56 AM - J. Baker: Delicious!
1/15/23, 1:37 AM - J. Baker: Lightly salted, yet tasty
1/15/23, 1:32 AM - J. Baker: YUMMY!
1/15/23, 0:47 AM - J. Baker: Caution: Kettle Chips are addictive!
1/15/23, 0:41 AM - J. Baker: The chip with a kiss of salt
1/14/23, 10:06 PM - J. Baker: Crunch. Wow!
1/14/23, 5:41 PM - J. Baker: Great strong flavor
1/14/23, 3:17 PM - J. Baker: yummy for your tummy
1/15/23, 0:30 AM - J. Baker: Best Chips Out There!
1/14/23, 8:45 PM - J. Baker: These chips tasted good
1/14/23, 7:45 PM - J. Baker: awesome chips
1/14/23, 6:51 PM - J. Baker: I dont know if...
1/14/23, 3:51 PM - J. Baker: Delicious!
1/16/23, 2:51 AM - J. Baker: Kettle Foods Spicy Thai Chips
1/16/23, 0:31 AM - J. Baker: Expired stock
1/14/23, 2:24 PM - J. Baker: these potato chips are yummy....
1/16/23, 11:15 AM - J. Baker: ONLY awful because SOMETIMES they are awful
1/15/23, 8:31 PM - J. Baker: 4 Stars for price and taste
1/15/23, 9:50 AM - J. Baker: CRISPY, CRUNCHY, AND ROBUST
1/15/23, 9:33 AM - J. Baker: Tangy and delicious snack
1/15/23, 2:19 AM - J. Baker: Best Chip
1/14/23, 8:49 PM - J. Baker: Not low salt
1/14/23, 7:30 PM - J. Baker: Best Chips I've Ever Tasted
1/14/23, 6:56 PM - J. Baker: Tasty!
1/16/23, 3:05 PM - J. Baker: Love the smaller bags!
1/16/23, 2:16 PM - J. Baker: Things you need to know
1/16/23, 2:11 PM - J. Baker: I made a mistake.....
1/16/23, 1:35 PM - J. Baker: Ok but Miss Vickie's Are Better
1/16/23, 11:42 AM - J. Baker: Do they have to "bite back"?
1/16/23, 11:18 AM - J. Baker: These chips are awesome if not best but....
1/16/23, 11:16 AM - J. Baker: kettle chips
1/16/23, 11:11 AM - J. Baker: GREAT DEAL
1/16/23, 10:42 AM - J. Baker: What a great tea at this price
1/16/23, 8:28 AM - J. Baker: delicious
1/16/23, 7:13 AM - J. Baker: Great well balanced Earl Grey
1/16/23, 3:51 AM - J. Baker: Best Earl Grey ever
1/15/23, 11:52 PM - J. Baker: favorite Earl Grey tea
1/16/23, 0:10 AM - J. Baker: Delicious
1/16/23, 8:11 AM - J. Baker: The best
1/16/23, 3:38 AM - J. Baker: A HUGE Success
1/16/23, 7:36 AM - J. Baker: For your Health
1/16/23, 10:50 AM - J. Baker: Shrimp stir fry
1/16/23, 2:49 PM - J. Baker: Do not taste from bottle! Mix with vanilla for true flavor.
1/16/23, 0:47 AM - J. Baker: Bavarian Creme Flavor Oil
1/16/23, 9:36 AM - J. Baker: The oldest soft drink is still the best!
1/15/23, 11:31 PM - J. Baker: Made in Michigan since 1866
1/15/23, 1:46 PM - J. Baker: Caramel flavor, excellent for baking and toppings (tips for using agave, too)
1/15/23, 10:59 PM - J. Baker: These weigh 46 oz. NOT 46 fluid ounces
1/15/23, 3:27 PM - J. Baker: Great buy!
1/15/23, 9:57 PM - J. Baker: excellent sweetner
1/15/23, 9:31 PM - J. Baker: Agave syrup
1/15/23, 5:57 PM - J. Baker: Sugar Substitute
1/16/23, 2:15 PM - J. Baker: Good, but container could be better
1/16/23, 1:24 PM - J. Baker: Great stuff!
1/16/23, 0:54 AM - J. Baker: Healthy Sweetener
1/16/23, 0:37 AM - J. Baker: Great way replacing the sugar
1/16/23, 0:11 AM - J. Baker: Great substitute sweetener
1/16/23, 10:00 AM - J. Baker: My Go to sweetner
1/16/23, 9:54 AM - J. Baker: The Best
1/16/23, 9:17 AM - J. Baker: YUMMY
1/16/23, 8:31 AM - J. Baker: Healthy Stuff
1/16/23, 7:22 AM - J. Baker: Agave Nectar
1/16/23, 5:03 AM - J. Baker: Sweet success
1/16/23, 4:39 AM - J. Baker: great product
1/16/23, 4:12 AM - J. Baker: Best price on agave nectar that I've found
1/16/23, 3:25 AM - J. Baker: How this could be good?
1/15/23, 9:51 AM - J. Baker: Best tea I ever had
1/14/23, 3:28 PM - J. Baker: That's a spicy!
1/14/23, 3:11 PM - J. Baker: Who needs salsa when chips taste this good?
1/15/23, 2:25 PM - J. Baker: Delicious!
1/14/23, 11:44 PM - J. Baker: Organic yummy chips what more can you ask for
1/14/23, 11:26 PM - J. Baker: Very different flavor
1/14/23, 5:11 PM - J. Baker: These are the best widely available bbq chips!
1/14/23, 5:55 PM - J. Baker: My favorite chips from Kettle!!
1/14/23, 9:48 AM - J. Baker: Amazing Taste, Best Chip Ever!
1/15/23, 9:51 AM - J. Baker: tasty
1/15/23, 2:45 AM - J. Baker: Plocky's Sweet Smokey Chipotle Whole Grain Tortill...
1/15/23, 2:06 AM - J. Baker: Yummy chips
1/15/23, 1:30 AM - J. Baker: Tasty!
1/15/23, 0:01 AM - J. Baker: So Faboo: Dangerous for those prone to Chips Binges!!!
1/14/23, 4:59 PM - J. Baker: The spice will grow!
1/15/23, 0:59 AM - J. Baker: The best tortilla chips I have ever eaten!!
1/14/23, 9:56 PM - J. Baker: Such an excellent chip
1/16/23, 1:26 PM - J. Baker: WRONG FLAVOR - got Country BBQ instead of Chili Chipotle
1/15/23, 8:51 PM - J. Baker: Great
1/15/23, 7:10 PM - J. Baker: Plocky's Rice and Beans Tortilla Chips
1/15/23, 3:31 PM - J. Baker: Huge fan of these chips!
1/15/23, 0:56 AM - J. Baker: Plocky's tortilla chips--tasty and healthy
1/15/23, 11:13 AM - J. Baker: Plocky's Three Grain Tortilla Chips
1/15/23, 10:50 AM - J. Baker: Tasty, but make sure you have gum
1/15/23, 10:17 AM - J. Baker: Don't stop carrying these chips
1/15/23, 9:44 AM - J. Baker: OM NOM NOM NOM!
1/15/23, 9:33 AM - J. Baker: delicious and healthy
1/15/23, 8:45 AM - J. Baker: Unique schrumshist and tasty Tortilla Chips
1/15/23, 7:26 AM - J. Baker: Music to My Palate
1/15/23, 7:22 AM - J. Baker: yummy!
1/15/23, 5:49 AM - J. Baker: Kettle Organic Chipotle potato chips
1/15/23, 2:55 AM - J. Baker: Best kept secret.
1/15/23, 2:03 AM - J. Baker: Delicious and additive
1/15/23, 1:46 AM - J. Baker: FANFREAKINTASTIC
1/15/23, 1:17 AM - J. Baker: Smokin'
1/15/23, 0:34 AM - J. Baker: really good chips
1/15/23, 0:10 AM - J. Baker: Plocky's Tortilla Chips, Red Beans 'N Rice
1/15/23, 0:01 AM - J. Baker: "Simply THE BEST"
1/14/23, 9:47 PM - J. Baker: Addicted
1/14/23, 9:12 PM - J. Baker: Perfect tortilla chip goodness!
1/14/23, 9:01 PM - J. Baker: These chips are addictive!
1/14/23, 3:57 PM - J. Baker: Best tortilla chips ever!!!
1/15/23, 2:44 AM - J. Baker: Meh
1/14/23, 7:58 PM - J. Baker: The "Organic" Label is Misleading
1/15/23, 7:06 PM - J. Baker: Kind of Bland
1/15/23, 6:48 PM - J. Baker: Delicious chips
1/15/23, 0:01 AM - J. Baker: Broken chips but tasty
1/14/23, 11:55 PM - J. Baker: The best chips ever!!!
1/14/23, 10:23 PM - J. Baker: Excellent Tortilla chips
1/14/23, 10:13 PM - J. Baker: Black Beans Never Tasted So Good!!!
1/14/23, 2:03 PM - J. Baker: Not, my favorite chip
1/14/23, 5:38 PM - J. Baker: Very Timely Delivery
1/15/23, 7:52 AM - J. Baker: Very Tasty - BUT BEWARE
1/16/23, 1:52 PM - J. Baker: Great candy
1/16/23, 7:20 AM - J. Baker: Candy
1/16/23, 1:59 PM - J. Baker: cute ,cute, cute!
1/16/23, 0:21 AM - J. Baker: A Surprising Find
1/16/23, 2:11 AM - J. Baker: Unparalleled taste
1/16/23, 2:11 AM - J. Baker: Amazing
1/16/23, 2:36 PM - J. Baker: a bit on the stale side
1/16/23, 8:18 AM - J. Baker: Delicious!
1/16/23, 0:59 AM - J. Baker: Disappointed!
1/15/23, 3:01 PM - J. Baker: Perhaps something was wrong with the batch...
1/15/23, 4:46 PM - J. Baker: $4 down the drain
1/15/23, 3:21 PM - J. Baker: Big Disappointment
1/15/23, 9:31 PM - J. Baker: Worst Frosting Ever
1/15/23, 8:44 PM - J. Baker: worst frosting ever
1/15/23, 8:16 PM - J. Baker: Cherrybrook Kitchen Vanilla Frosting
1/15/23, 7:55 PM - J. Baker: Do Not Buy This "Frosting"
1/15/23, 6:38 PM - J. Baker: Dum Dums for all!!
1/16/23, 3:23 AM - J. Baker: Lots of pops!
1/16/23, 11:13 AM - J. Baker: when you have no fridge but want meat, what do you do?
1/16/23, 9:04 AM - J. Baker: Anti-Oxidant Smoothie
1/16/23, 10:40 AM - J. Baker: Perversion of taste
1/16/23, 2:29 PM - J. Baker: Annie's Homegrown Organic Whole Wheat Shells & White Cheddar Macaroni & Cheese - 6 oz.
1/16/23, 1:35 PM - J. Baker: The flavor of the gods
1/15/23, 3:05 PM - J. Baker: cuttiest gum of the century
1/16/23, 8:45 AM - J. Baker: City Steam, not much steam in this brew.
1/15/23, 8:34 PM - J. Baker: Good soy sauce, but not special. Mainly good as unique gift.
1/16/23, 2:34 AM - J. Baker: What a surprise
1/16/23, 5:08 AM - J. Baker: Gets My Vote
1/16/23, 2:41 PM - J. Baker: And I though kikkoman was good?
1/16/23, 2:38 PM - J. Baker: Better than anything in the supermarket!
1/16/23, 1:59 PM - J. Baker: Best Soy Sauce Ever!!!
1/16/23, 2:31 AM - J. Baker: Great sauce!
1/16/23, 7:00 AM - J. Baker: Outstanding Product!
1/16/23, 1:16 PM - J. Baker: non GMO
1/16/23, 3:17 PM - J. Baker: Amazingly true to flavors...
1/16/23, 3:04 PM - J. Baker: IT'S A LAXATIVE
1/16/23, 7:35 AM - J. Baker: Good Tasting cup o' joe
1/16/23, 8:32 AM - J. Baker: Best of the Tassimo's
1/16/23, 1:36 PM - J. Baker: great coffee - terrible price
1/16/23, 1:30 PM - J. Baker: One of the better T-Discs
1/16/23, 11:29 AM - J. Baker: Note: Rating both coffee and seller
1/16/23, 11:26 AM - J. Baker: Kona for Tassimo
1/16/23, 2:42 PM - J. Baker: Best wafers
1/16/23, 9:37 AM - J. Baker: Tao of Tea ...!Don't get it
1/15/23, 9:18 AM - J. Baker: Perfect Sampler of Milka Chocolate
1/16/23, 0:18 AM - J. Baker: Dad really liked these.
1/16/23, 11:36 AM - J. Baker: Great candy my family loved it
1/16/23, 0:23 AM - J. Baker: Yummy!
1/16/23, 2:39 PM - J. Baker: Horrible .. dont buy it
1/15/23, 3:44 PM - J. Baker: Kleri Tea works great!
1/16/23, 1:39 PM - J. Baker: Where are the cranberries?
1/16/23, 9:25 AM - J. Baker: Our ferret loves this...
1/16/23, 0:08 AM - J. Baker: Fantastic!
1/15/23, 8:26 PM - J. Baker: Great little treats
1/16/23, 9:00 AM - J. Baker: NOT edible!
1/15/23, 2:49 PM - J. Baker: speedy shipping
1/15/23, 10:37 AM - J. Baker: My sons 9 & 11 loved making this, as easy enough to do by themselves. With adult supervision any age can do this neat project.
1/15/23, 11:16 PM - J. Baker: Spongetastic!
1/15/23, 10:50 PM - J. Baker: not as easy as it looks
1/15/23, 2:44 PM - J. Baker: Not one but twice came broken.
1/15/23, 10:39 PM - J. Baker: Rudolph Gingerbread House
1/15/23, 10:17 PM - J. Baker: Fun to paint
1/15/23, 10:23 PM - J. Baker: disappointment
1/15/23, 10:20 PM - J. Baker: Cute Item... but expired!
1/14/23, 8:15 PM - J. Baker: If I could give a rating under one-star...
1/15/23, 3:31 PM - J. Baker: Horrid
1/14/23, 11:54 PM - J. Baker: delicious
1/16/23, 1:06 AM - J. Baker: I love this tea - to each her own taste buds!
1/15/23, 9:08 PM - J. Baker: There is none greater.
1/15/23, 8:58 PM - J. Baker: Caramel chocolate
1/16/23, 8:36 AM - J. Baker: Chocolate heaven
1/16/23, 8:35 AM - J. Baker: Heavenly Action
1/16/23, 8:08 AM - J. Baker: Great chocolate...
1/16/23, 5:25 AM - J. Baker: Great item
1/15/23, 6:33 PM - J. Baker: choclate
1/16/23, 10:50 AM - J. Baker: is this serious??? 10 bucks??
1/16/23, 9:40 AM - J. Baker: Yum!
1/16/23, 4:06 AM - J. Baker: Overpriced, Even on Gold Box
1/16/23, 4:00 AM - J. Baker: Even at $15 seems a little overpriced.
1/16/23, 4:12 AM - J. Baker: Quick arrival great basket!
1/16/23, 4:32 AM - J. Baker: Adorable basket-makes nice presentation
1/15/23, 10:20 PM - J. Baker: Specialty party item
1/16/23, 10:46 AM - J. Baker: Delicious!
1/16/23, 8:32 AM - J. Baker: Chocolate - How can you go wrong?
1/16/23, 7:59 AM - J. Baker: chocolate liquor cups
1/16/23, 7:36 AM - J. Baker: Scottie
1/16/23, 8:38 AM - J. Baker: has a very good flavor
1/15/23, 5:24 PM - J. Baker: Odd Fake Flavor - Not Recommended
1/16/23, 1:45 PM - J. Baker: Good sugarless gum, with stronger gum for better bubble blowing than other sugarless gums
1/16/23, 1:23 PM - J. Baker: Great Gum
1/15/23, 11:25 PM - J. Baker: Delicious IMO and.... helps weight loss
1/15/23, 10:03 PM - J. Baker: ROYAL CANIN COCKER
1/16/23, 7:04 AM - J. Baker: Perfect for Cockers!
1/16/23, 5:02 AM - J. Baker: My dog loves this food!
1/16/23, 3:14 AM - J. Baker: Great deal!
1/16/23, 2:19 AM - J. Baker: Great food!
1/16/23, 0:57 AM - J. Baker: Buster Loves this dog food
1/16/23, 10:13 AM - J. Baker: Happy Dogs
1/16/23, 6:21 AM - J. Baker: Fast and great service,
1/16/23, 3:14 PM - J. Baker: GOOD FOOD!
1/16/23, 3:01 PM - J. Baker: Happy Dog
1/15/23, 9:00 AM - J. Baker: Great way to order
1/15/23, 4:32 PM - J. Baker: Good quality, delivered on time, human edible.
1/16/23, 10:17 AM - J. Baker: Rave Review for Rolled Oats
1/16/23, 7:33 AM - J. Baker: Excellent
1/15/23, 6:05 PM - J. Baker: Very Different taste from the 'Made in UK' or 'Made in India' version.
1/15/23, 9:05 PM - J. Baker: Not like other countries Cadbury
1/14/23, 8:47 PM - J. Baker: Great deal on great tea
1/15/23, 5:08 PM - J. Baker: Best Breakfast Tea ever
1/16/23, 2:47 PM - J. Baker: great organic tea at a great price
1/16/23, 2:36 PM - J. Baker: Mediocre, but cheap
1/16/23, 1:58 PM - J. Baker: Delicious and consistently good quality
1/16/23, 2:36 AM - J. Baker: Nice flavorful tea for the purist black tea addict
1/16/23, 1:13 AM - J. Baker: the best tea
1/16/23, 1:03 AM - J. Baker: Great Tea
1/15/23, 4:48 PM - J. Baker: This is a very fine tasting full lea, a great value!
1/15/23, 2:38 PM - J. Baker: not creamy...
1/15/23, 6:40 AM - J. Baker: This caramel is fantastic!!!
1/15/23, 4:37 AM - J. Baker: Great caramels
1/15/23, 2:16 AM - J. Baker: Where Has This Candy Been?
1/15/23, 5:05 AM - J. Baker: not for traditional caramel lovers
1/16/23, 7:58 AM - J. Baker: soda
1/16/23, 1:56 PM - J. Baker: Aluminum Free!
1/16/23, 7:27 AM - Aaron De Leon: This baking soda is the 'bomb!'
1/16/23, 2:15 PM - Aaron De Leon: Interesting info about baking soda
1/15/23, 7:12 PM - Aaron De Leon: Excellent quality product, fast delivery...
1/16/23, 4:17 AM - Aaron De Leon: Good oatmeal, I'm on my second bag
1/16/23, 1:53 AM - Aaron De Leon: mm mm oats
1/16/23, 6:34 AM - Aaron De Leon: Loved the Oats!!
1/16/23, 4:23 AM - Aaron De Leon: Funny taste
1/15/23, 3:05 AM - Aaron De Leon: awsome
1/15/23, 11:57 PM - Aaron De Leon: Very Happy with Pocky Sticks
1/15/23, 11:39 PM - Aaron De Leon: These are great!
1/15/23, 10:55 PM - Aaron De Leon: I love this snack!
1/15/23, 8:31 PM - Aaron De Leon: Chocolate was all melt
1/15/23, 1:52 PM - Aaron De Leon: This Item Is Awesome!!!!
1/16/23, 3:33 AM - Aaron De Leon: Great tasting snack...if you get the Japanese Pocky
1/16/23, 3:31 AM - Aaron De Leon: Great product
1/15/23, 7:42 PM - Aaron De Leon: Delicious
1/15/23, 7:04 PM - Aaron De Leon: Fun "popping-crispy" sticks dipped in chocolate, special treat for manga fans, but find local or wait till fall
1/15/23, 11:45 AM - Aaron De Leon: Yummy
1/16/23, 3:18 PM - Aaron De Leon: Doesn't taste as it should
1/16/23, 2:05 PM - Aaron De Leon: Pocky!!
1/15/23, 6:01 AM - Aaron De Leon: Great Buy
1/14/23, 9:04 PM - Aaron De Leon: Good stuff
1/15/23, 6:53 PM - Aaron De Leon: Pocky sticks together
1/15/23, 6:37 PM - Aaron De Leon: Really wanted to like these...
1/15/23, 4:27 AM - Aaron De Leon: Good berry flavor, excellent price.
1/15/23, 1:39 AM - Aaron De Leon: The chocolate ones are much better
1/15/23, 11:22 PM - Aaron De Leon: Something has changed
1/14/23, 5:02 PM - Aaron De Leon: Good berry flavor
1/16/23, 0:17 AM - Aaron De Leon: great taste But size it smaller
1/16/23, 9:23 AM - Aaron De Leon: Cheaper Ingredients, Lowered Quality
1/16/23, 8:03 AM - Aaron De Leon: Not a Fan
1/16/23, 5:54 AM - Aaron De Leon: Perfect Size
1/16/23, 5:00 AM - Aaron De Leon: Pretty good overall
1/15/23, 10:43 PM - Aaron De Leon: My child LOVES them!
1/15/23, 6:07 PM - Aaron De Leon: small but good
1/15/23, 4:23 PM - Aaron De Leon: You can't go wrong
1/15/23, 4:19 PM - Aaron De Leon: Yummy, but small...
1/15/23, 3:59 PM - Aaron De Leon: Be Very Berry Wary.
1/15/23, 9:11 AM - Aaron De Leon: Highly recomended!
1/15/23, 7:14 AM - Aaron De Leon: Very Berry Snack Bars
1/15/23, 1:49 AM - Aaron De Leon: Great snack
1/14/23, 11:13 PM - Aaron De Leon: Great bars for gluten-free diets!
1/16/23, 3:33 AM - Aaron De Leon: ABSOLUTELY VILE!!!
1/16/23, 8:22 AM - Aaron De Leon: Fantastic Coffee!!  Best I've ever had
1/15/23, 8:51 PM - Aaron De Leon: Strictly the Best!
1/15/23, 8:49 PM - Aaron De Leon: Best Coffee!
1/15/23, 9:51 PM - Aaron De Leon: Beautiful presentation ...and a pretty good tea too!
1/14/23, 9:43 PM - Aaron De Leon: Break Easily
1/14/23, 9:01 PM - Aaron De Leon: Wonderful Tea!
1/16/23, 0:07 AM - Aaron De Leon: I can't take the smell
1/15/23, 10:55 AM - Citizen John: Our twins love this one. With the subscription, the price is fair
1/15/23, 0:47 AM - Citizen John: Dessert to Them.  But is it Nutritional Enough?
1/15/23, 0:47 AM - Citizen John: Repeated deliveries of broken jars.  Great product though
1/15/23, 9:28 PM - Citizen John: Good flavor, too runny though
1/15/23, 0:47 AM - Citizen John: 12% Protein and 50% Vitamin A
1/16/23, 11:35 AM - Citizen John: Baby Lilly says 2 thumbs up!
1/16/23, 7:50 AM - Citizen John: Earth's Best Rice & Lentil dinner
1/16/23, 6:59 AM - Citizen John: Plastic in the food!
1/16/23, 5:32 AM - Citizen John: My baby's favorite 2nd stage food so far and great for constipation!
1/16/23, 5:13 AM - Citizen John: Sons Favorite Dinner!!!
1/16/23, 3:02 AM - Citizen John: No Issues
1/16/23, 1:45 AM - Citizen John: Too thin
1/15/23, 10:17 PM - Citizen John: A great place to start
1/15/23, 9:46 PM - Citizen John: good for you but not best flavor
1/15/23, 8:45 PM - Citizen John: A favorite!
1/15/23, 7:14 PM - Citizen John: Runny and odd-tasting
1/15/23, 6:48 PM - Citizen John: Too runny...
1/16/23, 3:04 PM - Citizen John: Great taste for a picky baby, but very thin compared to others
1/16/23, 2:26 PM - Citizen John: Great stuff
1/16/23, 2:06 PM - Citizen John: Son loves it
1/16/23, 0:38 AM - Citizen John: Love it
1/16/23, 0:36 AM - Citizen John: FOUND SHREDDED PLASTIC IN THE BABY FOOD!!!!
1/16/23, 11:26 AM - Citizen John: My son loves it!
1/16/23, 6:07 AM - Citizen John: Meh.  My daughter eats most everything else... this isn't her thing.
1/16/23, 5:32 AM - Citizen John: Not as yummy as Earth's Best's other flavors
1/16/23, 5:13 AM - Citizen John: Son's 2nd Favorite Dish
1/16/23, 0:59 AM - Citizen John: Had to toss 9 out of 12 jars
1/16/23, 0:41 AM - Citizen John: One of our favorites
1/16/23, 0:21 AM - Citizen John: Our Baby Likes it
1/16/23, 0:21 AM - Citizen John: Our Baby's Favorite Dinner
1/16/23, 0:04 AM - Citizen John: My daughter's favorite jarred food
1/15/23, 11:24 PM - Citizen John: yum
1/15/23, 11:19 PM - Citizen John: the only jarred baby food my son ate
1/15/23, 10:40 PM - Citizen John: A little more watery than other 2nd foods for EB
1/15/23, 9:21 PM - Citizen John: 50 calories of yumminess
1/15/23, 4:53 PM - Citizen John: Organic and tasty.
1/15/23, 2:52 PM - Citizen John: One of my son's favorites
1/15/23, 2:44 PM - Citizen John: Great
1/15/23, 1:24 PM - Citizen John: They make the best baby food.
1/15/23, 11:02 AM - Citizen John: A favorite
1/15/23, 10:20 AM - Citizen John: Geat Product
1/16/23, 3:57 AM - Citizen John: the garbanzo beans in it give horrible gas
1/15/23, 11:35 PM - Citizen John: Baby didn't like it
1/15/23, 8:38 AM - Citizen John: My baby's favorite dinner
1/16/23, 4:37 AM - Citizen John: Baby loves it, but there is plastic in it
1/15/23, 9:28 PM - Citizen John: Baby likes this one
1/15/23, 4:53 PM - Citizen John: Organic and Tasty
1/16/23, 6:36 AM - Citizen John: My baby liked it
1/16/23, 1:40 AM - Citizen John: moms (and dads) beware of plastic in the food
1/16/23, 1:22 PM - Citizen John: Allday Energy
1/14/23, 2:32 PM - Citizen John: The best!
1/15/23, 3:08 PM - Citizen John: Tasty Fruit
1/15/23, 3:07 PM - Citizen John: Beautiful fresh and it came easrly!v Yey!!
1/15/23, 2:24 PM - Citizen John: Fresh Fruit, Dark Chocolate
1/15/23, 6:28 PM - Citizen John: Sassafras Tea Bags
1/16/23, 0:53 AM - Citizen John: sassafrass tea
1/15/23, 11:44 AM - Citizen John: Good tasten tea.
1/16/23, 8:29 AM - Citizen John: hard to find tea
1/16/23, 2:49 AM - Citizen John: Better Taste Than I Expected
1/16/23, 8:51 AM - Citizen John: lovely!
1/16/23, 2:25 PM - Citizen John: K
1/16/23, 11:45 AM - Citizen John: Great product.
1/16/23, 10:56 AM - Citizen John: Sass Tea
1/15/23, 10:17 AM - Citizen John: The most awful taste
1/15/23, 10:59 AM - Citizen John: These are good, but ...
1/16/23, 3:05 PM - Citizen John: Great product!
1/16/23, 2:09 PM - Citizen John: Great Paste BUT Way Overpriced like 3x more
1/16/23, 8:52 AM - Citizen John: so easy to use
1/16/23, 1:32 PM - Citizen John: OMG DO NOT BUY!!!
1/15/23, 5:09 AM - Citizen John: WONDERFUL gravy!
1/15/23, 2:00 PM - Citizen John: YEEEEE HAWWW!
1/14/23, 7:01 PM - Citizen John: Best white gravy !
1/15/23, 11:18 AM - Citizen John: Pioneer Gravy is GREAT!
1/14/23, 1:55 PM - Citizen John: Eco sugar
1/15/23, 3:34 PM - Citizen John: More expensive online
1/14/23, 7:56 PM - Citizen John: Very Convenient and far better than instant coffee
1/15/23, 9:28 AM - Citizen John: No-Pot Fresh Coffee
1/14/23, 4:20 PM - Citizen John: Simple. Convenient
1/15/23, 1:50 PM - Citizen John: Brews an excellent cup of coffee quickly and easily
1/15/23, 0:15 AM - Citizen John: Very Convenient
1/15/23, 11:58 AM - Citizen John: Great taste
1/14/23, 4:13 PM - Citizen John: DELISH!!!!
1/16/23, 0:30 AM - Citizen John: new to rooibos tea
1/16/23, 0:41 AM - Citizen John: Tasted better than loose leaf rooibos
1/16/23, 8:13 AM - Citizen John: Best matcha quality and price
1/16/23, 9:43 AM - Citizen John: The Best
1/16/23, 3:12 AM - Citizen John: Moore's Marinade, Gluten, low sodium and MSG Free!
1/16/23, 3:48 AM - Citizen John: Great Tasting Diet Tea with all Natural Ingredients
1/16/23, 8:28 AM - Citizen John: Awesome Sauce
1/16/23, 7:52 AM - Citizen John: love this hot sauce
1/16/23, 7:50 AM - Citizen John: Great hot sauce!
1/16/23, 7:46 AM - Citizen John: Love This Stuff
1/16/23, 7:42 AM - Citizen John: Best sauce around
1/16/23, 7:42 AM - Citizen John: Tasty hot sauce!
1/16/23, 7:42 AM - Citizen John: Best all around hot sauce
1/16/23, 7:42 AM - Citizen John: best hot sauce around
1/16/23, 9:57 AM - Citizen John: Hot & Flavorful
1/16/23, 8:55 AM - Citizen John: Great Hot Sauce and people who run it!
1/16/23, 7:50 AM - Citizen John: this sauce is the shiznit
1/16/23, 11:08 AM - Citizen John: Not Hot
1/16/23, 10:06 AM - Scottdrum: Not hot, not habanero
1/16/23, 0:02 AM - Scottdrum: best babka
1/16/23, 1:32 AM - Scottdrum: My dog loves these but....
1/15/23, 11:15 PM - Scottdrum: She loves them...
1/16/23, 4:49 AM - Scottdrum: Not healthy but they taste good
1/16/23, 3:51 AM - Scottdrum: My dog loves these!!!!
1/16/23, 2:47 AM - Scottdrum: The Puppy Dogs Love Them!
1/16/23, 2:29 AM - Scottdrum: A great price!
1/16/23, 2:48 PM - Scottdrum: Smells like roses but no safety or freshness seal.
1/16/23, 8:24 AM - Scottdrum: delicious truffle goodness!
1/16/23, 11:19 AM - Scottdrum: a little too sweet
1/15/23, 4:39 AM - Scottdrum: Way too salty
1/16/23, 0:50 AM - Scottdrum: Warm and Wonderful
1/16/23, 9:12 AM - Scottdrum: Not good
1/16/23, 8:15 AM - Scottdrum: BEst stuff ever
1/15/23, 9:41 AM - Scottdrum: An ideal breakfast
1/15/23, 8:25 PM - Scottdrum: Love, Love, Love my Mueslix!!
1/16/23, 2:12 AM - Scottdrum: Nothing like actual Muesli
1/16/23, 1:29 AM - Scottdrum: Contains trans fat and high fructose corn syrup
1/16/23, 1:52 PM - Scottdrum: SUPERIOR HARD-TO-FIND PRODUCT
1/16/23, 0:56 AM - Scottdrum: cereal
1/15/23, 9:31 PM - Scottdrum: This is good, but bring back "Just Right" cereal
1/16/23, 5:18 AM - Scottdrum: Favorite cereal
1/16/23, 5:05 AM - Scottdrum: AWESOME CEREAL
1/16/23, 4:40 AM - Scottdrum: Kellogg's Mueslix
1/16/23, 2:29 AM - Scottdrum: overall A+
1/16/23, 2:21 AM - Scottdrum: Wonderful for breakfast AND snacks!
1/16/23, 2:08 AM - Scottdrum: Great Cereal
1/16/23, 1:58 AM - Scottdrum: LOVE Mueslix
1/15/23, 7:04 PM - Scottdrum: Best cereal I have ever eaten!
1/15/23, 3:01 PM - Scottdrum: Hard to find cereal found!
1/15/23, 1:53 PM - Scottdrum: Great Taste - Healthy Cereal
1/15/23, 9:41 AM - Scottdrum: Kelloggs Muselix are GREAT
1/16/23, 8:21 AM - Scottdrum: Mueslix Cereal
1/16/23, 8:18 AM - Scottdrum: Great mix of fruit, nuts, and whole grain
1/16/23, 6:56 AM - Scottdrum: Not in grocery stores
1/16/23, 5:49 AM - Scottdrum: yummy for ur tummy
1/16/23, 5:15 AM - Scottdrum: My Mom's favorite ceral
1/16/23, 4:43 AM - Scottdrum: Finally
1/16/23, 2:28 AM - Scottdrum: Kellogg's Mueslix Cereal
1/16/23, 0:34 AM - Scottdrum: Cereal is great.  Price is awful.
1/16/23, 6:18 AM - Scottdrum: Buyer Beware!This product contains High Fructose Corn Syrup!
1/16/23, 8:44 AM - Scottdrum: Love It
1/15/23, 3:24 PM - Scottdrum: Great Stuff
1/16/23, 11:25 AM - Scottdrum: Delicate Asian salad dressing...
1/16/23, 3:53 AM - Scottdrum: Totally a great balance in flavors I expect from an Asian dressing!
1/15/23, 2:34 PM - Scottdrum: somewhat sweet
1/16/23, 3:17 PM - Scottdrum: coffee beans
1/15/23, 4:12 PM - Scottdrum: Jeremiah's Pick:  great coffee
1/16/23, 1:07 AM - Scottdrum: Good product - better price elsewhere
1/16/23, 1:20 PM - Scottdrum: Yuk!
1/16/23, 10:35 AM - Scottdrum: Great color
1/15/23, 8:22 PM - Scottdrum: Totally Fantastic
1/16/23, 8:45 AM - Scottdrum: Have not tried product.... however...
1/14/23, 9:44 AM - Scottdrum: Best Tea EVER!!
1/15/23, 4:39 AM - Scottdrum: Favorite Tea
1/14/23, 11:09 AM - Scottdrum: Makes everything better
1/15/23, 7:23 PM - Scottdrum: Great fat free and spicy!!!
1/16/23, 6:25 AM - Scottdrum: Not exactly as described
1/16/23, 5:09 AM - Scottdrum: Crumbled cookies are no fun to eat
1/15/23, 7:12 AM - Scottdrum: Heavenly!
1/16/23, 10:50 AM - Scottdrum: Nicely packaged for a serving
1/15/23, 11:21 AM - Scottdrum: Yummy!
1/15/23, 8:42 PM - Scottdrum: cookies were in crumbles
1/16/23, 2:48 AM - Scottdrum: WONDERFUL COOKIES
1/15/23, 10:01 AM - Scottdrum: Worth the cost due to the unique flavor - my favorite sugar!
1/16/23, 2:24 PM - Scottdrum: Best Brown Sugar Cubes
1/16/23, 2:19 PM - Scottdrum: Perfect for Espresso
1/15/23, 11:41 PM - Scottdrum: Too pricey
1/16/23, 0:57 AM - Scottdrum: Superior product, GMO Free
1/16/23, 9:25 AM - Scottdrum: THIS IS NOT THE PRODUCT THAT I RECEIVED. THE ACTUAL PRODUCT MAY CARRY HEALTH RISKS FOR SOME COMSUMERS..
1/16/23, 0:05 AM - Scottdrum: melted!!!
1/16/23, 2:06 PM - Scottdrum: Very Potent.
1/15/23, 3:48 PM - Scottdrum: Hands Down, Best Mint EVER.
1/16/23, 6:00 AM - Scottdrum: The BEST mint
1/15/23, 8:16 PM - Scottdrum: delicious
1/16/23, 3:18 PM - Scottdrum: Impossible to Find!
1/16/23, 0:36 AM - Scottdrum: Great Ingredients
1/16/23, 11:42 AM - Scottdrum: Great price-great quality.
1/16/23, 5:34 AM - Scottdrum: Good perker-upper
1/15/23, 11:06 PM - Scottdrum: Excellent green tea!
1/15/23, 2:41 PM - Scottdrum: Enjoyable Green Tea
1/15/23, 11:44 AM - Scottdrum: Excellent
1/16/23, 2:55 AM - Scottdrum: an excellent alternative to regular Gatorade
1/16/23, 0:20 AM - Scottdrum: Gold Plated Cereal
1/16/23, 9:43 AM - Scottdrum: awful
1/16/23, 0:20 AM - Scottdrum: No reaction....
1/16/23, 0:20 AM - Scottdrum: Not for my dogs...
1/16/23, 9:43 AM - Scottdrum: awful
1/16/23, 3:20 PM - Scottdrum: It is awesome.
1/16/23, 8:36 AM - Scottdrum: Award winning, awesome flavour!
1/16/23, 8:35 AM - Scottdrum: It's decent
1/15/23, 4:58 PM - Scottdrum: Good taste, just enough heat
1/15/23, 2:15 PM - Scottdrum: Great Taste, Okay Crunch
1/15/23, 4:49 PM - Scottdrum: Unbelievable deal on a hard to find pruduct!
1/15/23, 4:04 PM - Scottdrum: No more stale chips. Cheap!
1/15/23, 1:43 PM - Scottdrum: Zesty and Spiced
1/16/23, 2:12 PM - Scottdrum: Sooo Good!!
1/16/23, 11:08 AM - Scottdrum: These are soooo good!!
1/16/23, 11:03 AM - Scottdrum: OPEN BAG OF CHIPS!!!
1/16/23, 8:28 AM - Scottdrum: college student gourmet
1/16/23, 8:00 AM - Scottdrum: Uncle rays without much taste
1/16/23, 7:56 AM - Scottdrum: These sure don't taste like ketchup to me!
1/16/23, 6:02 AM - Scottdrum: Great Chips!!
1/16/23, 5:52 AM - Scottdrum: Where's the vinegar?
1/16/23, 5:24 AM - Scottdrum: Uncle Ray's Kosher Dill Potato chips
1/16/23, 2:19 AM - Scottdrum: uncle rays barbeque chips
1/16/23, 1:22 AM - Scottdrum: Not quite Old Dutch but much better than Herr's
1/16/23, 0:04 AM - Scottdrum: Tasty Chips
1/15/23, 11:47 PM - Scottdrum: Great chips!  Great flavor!
1/15/23, 9:25 PM - Scottdrum: Uncle Ray's BBQ chips are the best!
1/16/23, 4:53 AM - Scottdrum: They were so good until more people bought them and now meh
1/15/23, 11:57 PM - Scottdrum: Ketchup powdery coating excessive, overdone gritty
1/15/23, 2:49 PM - Scottdrum: Good chips--nothing special
1/15/23, 8:03 PM - Scottdrum: PLEASE!!!!!Don't waste your money
1/16/23, 0:51 AM - Scottdrum: Good brand of food
1/16/23, 6:12 AM - Scottdrum: Rave reviews for my favorite vegetable!
1/16/23, 7:16 AM - Scottdrum: Metallic & Pearl Sheen Airbrush colors
1/16/23, 4:03 AM - Scottdrum: Love these colors
1/16/23, 2:54 AM - Scottdrum: lovely
1/16/23, 2:22 AM - Scottdrum: Quality white tea with added unusual flavors
1/16/23, 6:08 AM - Scottdrum: Smells like Heaven...
1/15/23, 10:37 AM - Scottdrum: Sublime Fragrance and Taste
1/15/23, 7:40 PM - Scottdrum: one of the best
1/16/23, 8:19 AM - Scottdrum: Delicious
1/16/23, 10:12 AM - Scottdrum: All cherry - I couldn't find it in stores.
1/16/23, 9:40 AM - Scottdrum: Who could say no to a blow pop!
1/15/23, 11:24 PM - Scottdrum: Beefeaters Swizzles Tripe 7-8 inch PACK OF 6
1/15/23, 10:40 PM - Scottdrum: NOT 6 pieces.
1/16/23, 0:36 AM - Scottdrum: jolokia salsa review
1/16/23, 2:28 PM - Scottdrum: Spicy
1/16/23, 11:31 AM - Scottdrum: One of the best salsas!!
1/16/23, 11:21 AM - Scottdrum: The mouth is strong the anus is weaker
1/16/23, 9:30 AM - Scottdrum: My cats love it
1/16/23, 1:06 PM - Scottdrum: cat food
1/16/23, 10:53 AM - Scottdrum: Cat Digs It!
1/16/23, 3:14 PM - Scottdrum: Great Value
1/16/23, 3:11 PM - Scottdrum: 9 Lives Daily Essentials 15 pound bag cat food. Good food, good price.
1/16/23, 3:05 PM - Scottdrum: Great deal
1/16/23, 3:04 PM - Scottdrum: Low quality ingredients, but...
1/16/23, 3:01 PM - Scottdrum: Cats love it
1/16/23, 1:59 PM - Scottdrum: Cats Love this food.
1/16/23, 1:24 PM - Scottdrum: Hard to please kitty LOVES it
1/16/23, 3:05 PM - Scottdrum: My cat hates it..
1/16/23, 0:17 AM - Scottdrum: i love candy
1/14/23, 9:05 AM - Scottdrum: the best!
1/15/23, 8:32 AM - Scottdrum: Non Alcoholic..
1/15/23, 4:40 PM - Scottdrum: yummy!
1/16/23, 11:32 AM - Scottdrum: bland
1/16/23, 10:03 AM - Scottdrum: Tastes Great
1/16/23, 2:12 PM - Scottdrum: Raw, Organic, Fair Trade, Tastes Great
1/16/23, 6:57 AM - Scottdrum: Arrived broken and isn't eligible for return?
1/16/23, 10:04 AM - Scottdrum: Like tiny light flavored peanut halves....
1/16/23, 5:42 AM - Scottdrum: Items in this Gift Basket were bad -- old and stale
1/16/23, 10:39 AM - Scottdrum: Dried UP
1/16/23, 10:12 AM - Scottdrum: Mostly dry
1/16/23, 9:57 AM - Scottdrum: Like to gamble? Buying the St. Patty's Dried Fruit Basket is a Crap-Shoot
1/16/23, 9:48 AM - Scottdrum: Nice and Fresh
1/16/23, 8:35 AM - Scottdrum: Absolutely Delicious
1/16/23, 2:34 PM - Scottdrum: Just ok
1/16/23, 2:12 PM - Scottdrum: Best Iced tea
1/14/23, 4:52 AM - Scottdrum: Cats love it!
1/15/23, 9:11 PM - Scottdrum: Vendor ripped off all of their cultures from other vendors
1/15/23, 5:55 PM - Scottdrum: The BEST!!!!
1/16/23, 4:07 AM - Scottdrum: Perfect for hard licorice lovers!
1/16/23, 1:43 PM - Scottdrum: Not nearly as good as Bissinger's French Long
1/16/23, 1:39 PM - Scottdrum: dense licorice flavor
1/16/23, 8:16 AM - Scottdrum: Kind of stale
1/15/23, 9:50 AM - Scottdrum: Must Have Been Spoiled
1/15/23, 9:07 PM - Scottdrum: Bisphenol A
1/15/23, 10:04 PM - Scottdrum: Spectacular tomatoes
1/15/23, 11:44 AM - Scottdrum: Next best thing to fresh tomatoes
1/16/23, 7:32 AM - Scottdrum: Excellent tomatoes
1/16/23, 7:24 AM - Scottdrum: Ok
1/16/23, 8:34 AM - Scottdrum: Gummy Bears
1/16/23, 7:35 AM - Scottdrum: Too addicting
1/16/23, 5:47 AM - Scottdrum: Yummmmy
1/16/23, 8:34 AM - Scottdrum: False Advertising
1/16/23, 2:42 AM - Scottdrum: MADE IN CHINA
1/16/23, 1:37 AM - Scottdrum: Mini Lollipops
1/16/23, 4:49 AM - Scottdrum: Very Cute!
1/15/23, 11:49 PM - Scottdrum: Perfect Lollipops
1/16/23, 0:56 AM - Scottdrum: Not what I expected
1/16/23, 6:20 AM - Scottdrum: Great service
1/15/23, 8:02 PM - Scottdrum: Loved these
1/16/23, 1:46 PM - Scottdrum: Lollipops
1/16/23, 1:24 PM - Scottdrum: Not as pictured
1/16/23, 11:09 AM - Scottdrum: Slightly funny taste to begin with, but I can't stop eating them!
1/16/23, 8:15 AM - Scottdrum: Great for Birthday Themed Party
1/16/23, 8:12 AM - Scottdrum: Fun stuff
1/16/23, 6:43 AM - Scottdrum: Very cute pops
1/16/23, 6:28 AM - Scottdrum: Shipping
1/16/23, 6:20 AM - Scottdrum: small swirled lollipops
1/16/23, 5:24 AM - Scottdrum: Cute, small lollipops, a few arrived broken
1/16/23, 2:09 AM - Scottdrum: Great Product!
1/14/23, 2:15 PM - Scottdrum: Apple Cinnamon Muffins
1/15/23, 3:46 AM - Scottdrum: Excellent Product
1/14/23, 11:12 PM - Scottdrum: YUCK
1/16/23, 6:23 AM - Scottdrum: Marianne
1/16/23, 0:20 AM - Scottdrum: Favorite thing about Brazil
1/16/23, 7:46 AM - Season Balik: Delicious and easy
1/16/23, 8:49 AM - Season Balik: Love Taro
1/16/23, 2:00 PM - Season Balik: I was able to eat bread again!
1/16/23, 10:43 AM - Season Balik: Service was good
1/16/23, 2:24 PM - Season Balik: Mini Mini is right!
1/14/23, 1:35 PM - Season Balik: Yummy
1/13/23, 2:21 PM - Season Balik: The best twice baked potatoes you'll ever have!
1/15/23, 2:57 PM - Season Balik: Over Rated (way over priced)Frozen meats
1/14/23, 5:05 AM - Season Balik: I like these!
1/13/23, 6:15 PM - Season Balik: Actually pretty good
1/14/23, 7:26 AM - Season Balik: yum yum yum!
1/14/23, 11:08 PM - Season Balik: Not like the picture
1/14/23, 8:06 AM - Season Balik: Now this is my kind of Potato with Steak
1/14/23, 7:42 PM - Season Balik: Tasty and easy to make
1/14/23, 9:15 PM - Season Balik: Very Good
1/14/23, 9:23 AM - Season Balik: Potatoes
1/15/23, 9:40 PM - Season Balik: Tasty, and perfect sized.
1/14/23, 9:15 PM - Season Balik: Yum
1/14/23, 9:04 PM - Season Balik: Tasty
1/14/23, 10:07 AM - Season Balik: Quick, easy, taste great
1/16/23, 0:44 AM - Season Balik: A+
1/16/23, 10:52 AM - Season Balik: so good!
1/16/23, 9:18 AM - Season Balik: These are the best hash browns!!!!!!!!!!
1/16/23, 8:12 AM - Season Balik: Au Gratin Potatoes
1/16/23, 6:51 AM - Season Balik: So Good!
1/15/23, 11:09 PM - Season Balik: tasted ok.... a bit overpriced tho
1/14/23, 8:19 PM - Season Balik: They're pretty good.
1/16/23, 2:15 PM - Season Balik: Easy for a single lifestyle
1/16/23, 10:43 AM - Season Balik: Unimpressed
1/16/23, 7:59 AM - Season Balik: Mashed Taters
1/15/23, 9:30 PM - Season Balik: Taters ...
1/15/23, 7:32 PM - Season Balik: Omaha Chicken and Stuffed Baked Potatoies
1/15/23, 4:17 PM - Season Balik: Stuffed Baked Potatoes
1/16/23, 8:06 AM - Season Balik: Big fan!
1/16/23, 11:57 AM - Season Balik: MAXIMUM RAVE POWER
1/15/23, 9:34 AM - Season Balik: Shipping by price, not weight?
1/15/23, 9:08 PM - Season Balik: What?  No ingredient list?
1/15/23, 0:28 AM - Season Balik: Great Product! This is REAL Garlic Juice!
1/16/23, 1:07 PM - Season Balik: Spray garlic!
1/16/23, 4:50 AM - Season Balik: garlic juice
1/16/23, 3:00 PM - Season Balik: Now a staple
1/15/23, 0:20 AM - Season Balik: Delicious tea!!!
1/15/23, 11:47 AM - Season Balik: Can't detect the prickly pear
1/16/23, 2:42 AM - Season Balik: Maple Syrup
1/12/23, 3:17 AM - Season Balik: WOW Make your own 'slickers' !
1/12/23, 3:08 AM - Season Balik: Great Product
1/14/23, 11:11 PM - Season Balik: Too good to be true.
1/16/23, 11:48 AM - Season Balik: perfect size!
1/15/23, 10:26 PM - Season Balik: Great Deal and So Convenient
1/15/23, 6:05 PM - Season Balik: Spam for any meal
1/16/23, 4:32 AM - Season Balik: OMG! So Good!
1/15/23, 11:02 PM - Season Balik: Horrible!
1/15/23, 11:38 PM - Season Balik: Crab Cakes Delight
1/16/23, 11:03 AM - Season Balik: Just OK, I guess that all canned crab is not that great
1/14/23, 1:55 PM - Season Balik: VERY HEALTHFUL TREAT FOR DOGS
1/16/23, 5:58 AM - Season Balik: My yorkiepoo loves these.
1/15/23, 9:59 PM - Season Balik: Great choice for little dogs
1/14/23, 10:50 PM - Season Balik: Barb
1/15/23, 1:53 AM - Season Balik: The true, the classic custard for authentic, yummy English trifle
1/15/23, 0:36 AM - Season Balik: Delicious! Best custard ever!
1/16/23, 1:40 PM - Season Balik: Best vanilla custard ever
1/16/23, 11:51 AM - Season Balik: Bird's Custard Powder
1/16/23, 10:23 AM - Season Balik: happily home
1/16/23, 2:55 AM - Season Balik: Bird's Custard Powder
1/15/23, 11:52 PM - Season Balik: Hard to find - Bird's custard powder
1/15/23, 6:10 PM - Season Balik: Wonderful product!
1/16/23, 10:17 AM - Season Balik: Makes excellent biryani
1/15/23, 4:58 PM - Season Balik: Good tea, bad bag
1/16/23, 2:41 PM - Season Balik: Lifesaver!
1/16/23, 11:47 AM - Season Balik: Great tasting tea for Cold & Flu
1/16/23, 9:18 AM - Season Balik: A Healing Tea
1/15/23, 11:52 AM - Season Balik: Medicinal tea that really helps
1/16/23, 10:06 AM - Season Balik: Absolutely the Best
1/13/23, 3:33 PM - Season Balik: Healthy, non-fattening, just the right size and delicious!
1/16/23, 0:51 AM - Season Balik: Good training treat
1/14/23, 4:19 PM - Season Balik: My Dogs Love This Treat
1/13/23, 3:08 PM - Season Balik: 5 Woofs!
1/16/23, 4:48 AM - Season Balik: The best dog treat ever
1/16/23, 1:29 PM - Season Balik: Lucy's treats
1/16/23, 2:55 AM - Season Balik: Yummy Treats
1/16/23, 2:32 AM - Season Balik: bulldogs rule
1/16/23, 1:01 AM - Season Balik: Best Friend treats
1/16/23, 0:43 AM - Season Balik: Great for training!
1/15/23, 7:01 PM - Season Balik: great product
1/15/23, 4:42 PM - Season Balik: My dogs love 'em.
1/15/23, 1:22 PM - Season Balik: My dog loves liver biscotti.
1/15/23, 0:56 AM - Season Balik: Make your dog happy!
1/15/23, 11:57 AM - Season Balik: Great Treats!
1/15/23, 9:14 AM - Season Balik: Excellent dog treats.
1/15/23, 4:55 AM - Season Balik: Jack's treats
1/15/23, 1:00 AM - Season Balik: A GREAT TREAT, BUT WAY OVERPRICED SHIPPING CHARGES
1/15/23, 0:00 AM - Season Balik: Our dogs go crazy for this!
1/14/23, 9:33 AM - Season Balik: Liver Biscotti rules in our house
1/13/23, 7:20 PM - Season Balik: Rich J Wyzykoski
1/16/23, 4:30 AM - Season Balik: Waste of money
1/16/23, 6:01 AM - Season Balik: Deeee-licious!
1/14/23, 4:03 PM - Season Balik: u talked me into it  mr. beer nut
1/14/23, 11:52 AM - Season Balik: mmmmmmmm...beer...nuts!
1/16/23, 2:28 PM - Season Balik: jgk likes beer nuts
1/16/23, 6:20 AM - Season Balik: Just as I remembered.
1/16/23, 3:48 AM - RICHARD M WING: Mild Sweet And Salty Blend
1/16/23, 3:11 AM - RICHARD M WING: great customer service
1/16/23, 2:38 AM - RICHARD M WING: Hard to find Beer Nuts
1/15/23, 7:53 PM - RICHARD M WING: Beer Nuts
1/15/23, 1:01 PM - RICHARD M WING: The Best!
1/14/23, 9:21 PM - RICHARD M WING: Salty with a hint of sweetness
1/14/23, 6:53 PM - RICHARD M WING: What Happened
1/15/23, 3:20 PM - RICHARD M WING: beer nuts
1/16/23, 1:20 PM - RICHARD M WING: The flavor is gone
1/15/23, 0:12 AM - RICHARD M WING: Not my best experience
1/14/23, 1:48 PM - RICHARD M WING: Yum
1/14/23, 9:11 AM - RICHARD M WING: Beautiful and Delicious
1/14/23, 1:50 PM - RICHARD M WING: Superb Pasta!
1/16/23, 11:08 AM - RICHARD M WING: Expensive But Worth It!
1/16/23, 1:37 AM - RICHARD M WING: One of the best sweet hot sauces out there
1/15/23, 8:47 PM - RICHARD M WING: chocolot!
1/16/23, 1:14 AM - RICHARD M WING: Much better than milk chocolate!
1/16/23, 8:41 AM - RICHARD M WING: Great dipping chocolate right out from microwave!
1/16/23, 5:32 AM - RICHARD M WING: Warning: Reviews do not reflect actual product (Feb 19, 2012)
1/16/23, 5:09 AM - RICHARD M WING: Awesome cacao
1/16/23, 5:49 AM - RICHARD M WING: The Price is Right
1/16/23, 7:43 AM - RICHARD M WING: NOT what I originally ordered! BOO, amazon!
1/16/23, 6:02 AM - RICHARD M WING: great tasting cocoa powder
1/16/23, 5:57 AM - RICHARD M WING: outrageous
1/16/23, 5:34 AM - RICHARD M WING: Alive and Aware Organic Raw Cacao Powder
1/16/23, 2:38 PM - RICHARD M WING: Equidorian OJio Arriba Carillo "RAW Oranic" Cacao
1/16/23, 10:58 AM - RICHARD M WING: Poor quality product
1/16/23, 9:14 AM - RICHARD M WING: The best!
1/16/23, 7:53 AM - RICHARD M WING: Super Delicious!
1/15/23, 4:56 AM - RICHARD M WING: bread mixes
1/15/23, 9:10 PM - RICHARD M WING: GREAT
1/16/23, 11:54 AM - RICHARD M WING: What bacon is supposed to be
1/16/23, 2:36 PM - RICHARD M WING: Delicous
1/15/23, 2:00 PM - RICHARD M WING: DELICIOUS
1/16/23, 10:13 AM - RICHARD M WING: OMG COOKIES
1/15/23, 11:48 PM - RICHARD M WING: GOOD!
1/15/23, 11:42 PM - RICHARD M WING: Great Cookies
1/15/23, 0:37 AM - RICHARD M WING: Got a chest cold with a nasty cough?????
1/15/23, 6:01 AM - RICHARD M WING: Better than cherry nibs (the ones with gluten)
1/14/23, 4:49 PM - RICHARD M WING: Candy Tree Organic Cherry Bites
1/14/23, 4:06 PM - RICHARD M WING: a little to hard
1/16/23, 0:56 AM - RICHARD M WING: Gluten-free bliss!
1/15/23, 8:44 PM - RICHARD M WING: Gluten Free Licorice
1/15/23, 3:11 AM - RICHARD M WING: Instant Favorite!
1/15/23, 1:52 PM - RICHARD M WING: Thick and creamy; nice flavor
1/15/23, 1:23 AM - RICHARD M WING: Good dressing
1/14/23, 11:06 PM - RICHARD M WING: Wish bone Fat Free Ranch Dressing
1/16/23, 0:18 AM - RICHARD M WING: Its GOOD!!!
1/16/23, 6:24 AM - RICHARD M WING: Good price, good product
1/16/23, 7:20 AM - RICHARD M WING: Sorry, taste is not pleasing.
1/14/23, 11:26 PM - RICHARD M WING: GREAT FAT FREE RANCH
1/15/23, 5:16 PM - RICHARD M WING: Delicious tea- slight hints of almond and chocolate but not overpowering
1/16/23, 2:49 PM - RICHARD M WING: Great for multi-infusion.. Jasmine Dragon Pearl Green TEA
1/16/23, 7:35 AM - RICHARD M WING: Darn Good!
1/16/23, 8:32 AM - RICHARD M WING: Difficult to review.
1/16/23, 6:08 AM - RICHARD M WING: Yummy!
1/16/23, 5:05 AM - RICHARD M WING: Great product and good price
1/16/23, 9:34 AM - RICHARD M WING: Great flavor, shipped fast
1/16/23, 8:18 AM - RICHARD M WING: Delicious and hard to find
1/16/23, 8:16 AM - RICHARD M WING: Tic-Tac-Yum!
1/16/23, 7:55 AM - RICHARD M WING: Great tasting little treats
1/16/23, 0:20 AM - RICHARD M WING: Good
1/16/23, 0:02 AM - RICHARD M WING: Cherry good!
1/16/23, 8:38 AM - RICHARD M WING: tic tac
1/16/23, 7:16 AM - RICHARD M WING: tic tac solution
1/14/23, 11:11 PM - RICHARD M WING: easter basket
1/16/23, 1:29 PM - RICHARD M WING: Bars
1/16/23, 8:51 AM - RICHARD M WING: Another favorite!
1/16/23, 9:43 AM - RICHARD M WING: Good flour for gluten-free baking
1/15/23, 11:57 PM - RICHARD M WING: Great for GF Baking
1/16/23, 0:48 AM - RICHARD M WING: Perfect Treat!
1/16/23, 11:41 AM - RICHARD M WING: Best for Sweets :]
1/16/23, 5:34 AM - RICHARD M WING: Spectrum Naturals Walnut Oil, refined
1/14/23, 5:11 AM - RICHARD M WING: White Stevia 12 Oz Pwdr
1/15/23, 3:37 PM - RICHARD M WING: Great taste, safe & Natural
1/16/23, 1:43 PM - RICHARD M WING: Only 6.4% Stevia Extract, but very good flavor
1/16/23, 5:55 AM - RICHARD M WING: My new favorite sweetener
1/15/23, 4:32 PM - RICHARD M WING: best tasting stevia
1/15/23, 4:40 PM - RICHARD M WING: Get Healthy Live Better and Longer
1/15/23, 2:49 PM - RICHARD M WING: An Excellent Alternative to Artificial Sweetners
1/15/23, 10:42 AM - RICHARD M WING: Best tasting
1/14/23, 5:35 AM - RICHARD M WING: Also look for the packets
1/16/23, 11:31 AM - RICHARD M WING: used to be my favorite
1/15/23, 2:39 PM - RICHARD M WING: meh
1/16/23, 2:54 PM - RICHARD M WING: NuNaturals Nustevia is great
1/16/23, 2:34 PM - RICHARD M WING: I love this stuff
1/16/23, 2:29 PM - RICHARD M WING: Tastes great in iced drinks
1/16/23, 2:15 PM - RICHARD M WING: Great Product!  No bitter taste.  Won't spike your insulin!
1/16/23, 2:11 PM - RICHARD M WING: Great Taste and Zero Calories
1/16/23, 2:11 PM - RICHARD M WING: Sweeter than sugar!!
1/16/23, 2:03 PM - RICHARD M WING: Best alternative to sugar.
1/16/23, 1:19 PM - RICHARD M WING: Great taste and great value
1/16/23, 0:21 AM - RICHARD M WING: The World's Best Sweetener
1/16/23, 0:07 AM - RICHARD M WING: Best stevia product I've found
1/16/23, 11:38 AM - RICHARD M WING: Sweet stuff!
1/16/23, 10:50 AM - RICHARD M WING: great product
1/16/23, 10:30 AM - RICHARD M WING: The best I've ever had!
1/16/23, 8:05 AM - RICHARD M WING: Best taste ever!
1/16/23, 7:33 AM - RICHARD M WING: Great Product
1/16/23, 7:20 AM - RICHARD M WING: Perfectly, naturally sweet!
1/16/23, 6:36 AM - Linda S. Blyth: the best stevia
1/16/23, 6:36 AM - Linda S. Blyth: Love this stuff!
1/16/23, 6:30 AM - Linda S. Blyth: The Only Sweetener I Will Use
1/16/23, 4:36 AM - Linda S. Blyth: Great Sweetener!
1/16/23, 1:36 AM - Linda S. Blyth: Best stevia product I ever used
1/15/23, 11:28 PM - Linda S. Blyth: Sweetly satisfying...
1/15/23, 1:52 PM - Linda S. Blyth: The Best Stevia
1/15/23, 2:09 PM - Linda S. Blyth: great inexpensive caviar
1/15/23, 11:55 PM - Linda S. Blyth: Great red caviar, tasty and attractive on eggs
1/15/23, 6:31 PM - Linda S. Blyth: Another great experience with amazon
1/16/23, 7:01 AM - Linda S. Blyth: Worst Caviar Ever
1/16/23, 5:08 AM - Linda S. Blyth: Great as a topping on your culinary creations
1/16/23, 2:26 AM - Linda S. Blyth: fishy little devils
1/16/23, 9:14 AM - Linda S. Blyth: Disappointing...
1/16/23, 7:04 AM - Linda S. Blyth: too much red dye and too little taste.... other than that it is great-lol
1/16/23, 4:24 AM - Linda S. Blyth: All hail the Israelis!
1/16/23, 7:27 AM - Linda S. Blyth: Worthy Every $
1/16/23, 6:44 AM - Linda S. Blyth: Wow!!!! A great deal love,love , love it!!!!1
1/16/23, 10:19 AM - Linda S. Blyth: Yuck!
1/15/23, 11:28 AM - Linda S. Blyth: Great price, quality caviar.
1/16/23, 3:05 PM - Linda S. Blyth: the family loved it
1/16/23, 11:51 AM - Linda S. Blyth: Best for on the road snacks and health
1/16/23, 2:09 PM - Linda S. Blyth: Smaller Than Expected
1/16/23, 1:03 PM - Linda S. Blyth: For the price, these are great for all. Even a crowd. Much better than the smaller FlavorIce.
1/15/23, 4:04 PM - Linda S. Blyth: Costa Rican Export Coffee
1/14/23, 3:44 PM - Linda S. Blyth: Vintage Tasting Coffee
1/16/23, 9:12 AM - Linda S. Blyth: Coffee from Amazon.com
1/16/23, 5:31 AM - Linda S. Blyth: Best Coffee Ever
1/16/23, 3:43 AM - Linda S. Blyth: Great Coffee
1/16/23, 0:17 AM - Linda S. Blyth: Happy Customer
1/15/23, 8:31 PM - Linda S. Blyth: Great Taste!
1/15/23, 4:53 PM - Linda S. Blyth: Fantastic Coffee!
1/15/23, 3:23 PM - Linda S. Blyth: My aunt's favorite
1/15/23, 2:47 PM - Linda S. Blyth: Excellent Coffee
1/16/23, 7:42 AM - Linda S. Blyth: NOT 144 PACKETS!!  ONLY 12!!!!
1/14/23, 2:34 PM - Linda S. Blyth: Create Exquisite Cake Decorations
1/15/23, 1:17 AM - Linda S. Blyth: The Inexpensive Alternative to Gold Leaf!
1/15/23, 5:31 AM - Linda S. Blyth: shining star
1/15/23, 2:52 AM - Linda S. Blyth: gold dust is awesome
1/16/23, 2:47 PM - Linda S. Blyth: not edible
1/15/23, 11:28 AM - Linda S. Blyth: It's Fast.  It's Food.
1/15/23, 5:47 PM - Linda S. Blyth: Not Bad
1/15/23, 0:31 AM - Linda S. Blyth: Tasty, Quick Meal
1/16/23, 11:58 AM - Linda S. Blyth: I'm a fan
1/16/23, 11:57 AM - Linda S. Blyth: Neither great nor bad
1/16/23, 11:41 AM - Linda S. Blyth: Not very good
1/16/23, 9:33 AM - Linda S. Blyth: Chicken and Rice ???
1/16/23, 7:01 AM - Linda S. Blyth: THICK SOUP
1/16/23, 4:19 AM - Linda S. Blyth: Not a lot of flavor, not a lot of chicken
1/15/23, 8:19 PM - Linda S. Blyth: Hormel Compleats are simply wonderful
1/16/23, 5:49 AM - Linda S. Blyth: The best around
1/16/23, 10:37 AM - Linda S. Blyth: Okay price, fast easy meals
1/16/23, 11:44 AM - Linda S. Blyth: Good
1/16/23, 11:32 AM - Linda S. Blyth: A Good Choice
1/16/23, 5:57 AM - Linda S. Blyth: fantastic  hot meal
1/16/23, 7:12 AM - Linda S. Blyth: Chicken noodle
1/16/23, 2:21 AM - Linda S. Blyth: not good
1/16/23, 10:46 AM - Linda S. Blyth: So far, Donut Shop Classics are the best pods I've tried
1/16/23, 10:27 AM - Linda S. Blyth: Restaurant taste at home
1/15/23, 1:07 PM - Linda S. Blyth: Yum
1/15/23, 9:53 PM - Linda S. Blyth: YUM YUM!
1/16/23, 2:21 AM - Linda S. Blyth: why is this soup/entree so unpopular????
1/16/23, 1:24 AM - Linda S. Blyth: One of my favorites
1/16/23, 8:06 AM - Linda S. Blyth: LOVE THIS!
1/16/23, 9:36 AM - Linda S. Blyth: Quick, easy and tasty!
1/16/23, 8:32 AM - Linda S. Blyth: Yum!
1/16/23, 8:47 AM - Linda S. Blyth: Love it.
1/16/23, 7:37 AM - Linda S. Blyth: It's OK
1/16/23, 5:08 AM - Linda S. Blyth: Bent in Delivery
1/16/23, 2:00 PM - Linda S. Blyth: Great for a healthy, hot, great-tasting vegan meal on the go!
1/16/23, 0:43 AM - Linda S. Blyth: Glorified Cup of Noodles
1/16/23, 0:24 AM - Linda S. Blyth: not bad but not too much flavor
1/16/23, 8:25 AM - Linda S. Blyth: Noodles not good
1/16/23, 5:35 AM - Linda S. Blyth: HORRIBLE.
1/15/23, 5:25 PM - Linda S. Blyth: Delicious
1/16/23, 0:53 AM - Linda S. Blyth: Great
1/16/23, 1:59 PM - Linda S. Blyth: juicy jays
1/16/23, 1:23 PM - Linda S. Blyth: Love the soup
1/16/23, 1:50 PM - Linda S. Blyth: weak coffee not good for a premium product and price
1/15/23, 7:49 AM - Linda S. Blyth: Lindt Pistachio Chocolate
1/15/23, 2:45 AM - Linda S. Blyth: Best of the canned tomatoes
1/15/23, 11:49 AM - Linda S. Blyth: Best sauce tomato (canned or fresh) period
1/16/23, 10:17 AM - Linda S. Blyth: Margherita Pizza
1/15/23, 10:29 AM - Linda S. Blyth: We couldn't tell the difference in a blind taste test.
1/14/23, 0:20 AM - Linda S. Blyth: Applesauce Spice Cake
1/14/23, 0:34 AM - Linda S. Blyth: Can this really be gluten free?
1/15/23, 0:10 AM - Linda S. Blyth: Smells Great
1/15/23, 8:55 AM - Linda S. Blyth: Delicious black jelly beans
1/15/23, 9:47 PM - Linda S. Blyth: Fantastic!
1/15/23, 11:32 PM - Linda S. Blyth: BEST Licorice Jelly Beans EVER!
1/16/23, 1:23 PM - Linda S. Blyth: I never got it
1/14/23, 4:20 AM - Linda S. Blyth: Scrumptious
1/16/23, 0:17 AM - Linda S. Blyth: makes nasty loose poo!
1/16/23, 2:41 PM - Linda S. Blyth: Very good.
1/16/23, 2:16 PM - Linda S. Blyth: Da Vinci sugar free Blueberry syrup
1/15/23, 10:43 PM - Linda S. Blyth: Just OK
1/16/23, 6:36 AM - Linda S. Blyth: Prefer the whole slices
1/16/23, 3:53 AM - Linda S. Blyth: Nice to have in the pantry
1/15/23, 6:25 PM - Linda S. Blyth: Detailed reply from company over infant feeding and DHA/ARA
1/15/23, 5:35 PM - Linda S. Blyth: Colic/acid reflux babies...try this!
1/15/23, 4:55 PM - Epochx: A Great Product!!!
1/16/23, 3:57 AM - Epochx: BUY ELSEWHERE
1/15/23, 9:01 PM - Epochx: Best Organic milk out there..my baby switched from Similac Soy
1/15/23, 10:13 PM - Epochx: We are a fan
1/16/23, 0:17 AM - Epochx: Absolutely awesome!
1/15/23, 11:28 PM - Epochx: Pasta Lovers Dream
1/16/23, 6:18 AM - Epochx: Good!
1/16/23, 4:49 AM - Epochx: great calorie cutter
1/16/23, 2:52 PM - Epochx: Real Pasta With Half the Calories and Most of the Taste!
1/16/23, 2:35 PM - Epochx: Great Pasta
1/16/23, 1:09 PM - Epochx: Fabulous!
1/16/23, 11:26 AM - Epochx: FiberGourmet light penne
1/16/23, 10:37 AM - Epochx: Italian Born Pasta Lover Gives This 5 Stars!
1/16/23, 8:16 AM - Epochx: FANTASTIC
1/16/23, 7:20 AM - Epochx: Fabulous product
1/16/23, 6:25 AM - Epochx: Pasta
1/16/23, 5:48 AM - Epochx: I thought it was exceptional
1/16/23, 4:00 AM - Epochx: FiberGourmet Light Penne, 8-Ounce Boxes (Pack of 6)
1/15/23, 0:04 AM - Epochx: I will never go back to Senseo pods as long as these are available.
1/16/23, 2:22 PM - Epochx: Disgusting
1/16/23, 1:49 PM - Epochx: Big pods, great value, delicious decaf coffee!
1/16/23, 0:59 AM - Epochx: These are absolutely revolting
1/16/23, 10:52 AM - Epochx: Nice strength, maybe too much vanilla?
1/16/23, 10:14 AM - Epochx: Rich and Flavorful.
1/16/23, 5:19 AM - Epochx: Great taste!
1/14/23, 9:24 PM - Epochx: Great dessert
1/16/23, 8:03 AM - Epochx: Pudding
1/15/23, 3:44 PM - Epochx: cook & serve choc. fudge pudding
1/16/23, 9:28 AM - Epochx: Quick, Easy and Delicious
1/16/23, 2:12 PM - Epochx: easy to make also
1/16/23, 5:16 AM - Epochx: BEST MUFFINS IN THE WORLD !!!
1/16/23, 1:32 AM - Epochx: Martha White Chocolate Chocolate Chip Muffin Mix
1/16/23, 7:35 AM - Epochx: Worst cookies ever!!!!!
1/16/23, 4:29 AM - Epochx: Love it!!
1/15/23, 6:59 AM - Epochx: Good but way too expensive
1/14/23, 11:51 AM - Epochx: Not bad, but it really is just a taste of thai
1/14/23, 0:50 AM - Epochx: Good flavor but...
1/14/23, 0:15 AM - Epochx: artificial flavor
1/14/23, 11:32 AM - Epochx: Needs a little something
1/14/23, 11:05 AM - Epochx: Really good!
1/16/23, 11:32 AM - Epochx: Not so much...
1/16/23, 3:50 AM - Epochx: More than just a taste of Thai
1/15/23, 0:53 AM - Epochx: Taste of Thai Coconut Ginger soup
1/15/23, 9:59 AM - Epochx: Delicious!
1/15/23, 9:00 AM - Epochx: OKAY IN A PINCH...
1/15/23, 7:17 AM - Epochx: Now containing gluten!
1/14/23, 8:19 PM - Epochx: not bad, but I won't reorder
1/14/23, 2:05 PM - Epochx: Great gluten free quick fix meal
1/14/23, 11:29 AM - Epochx: Easy and delicious
1/14/23, 11:03 AM - Epochx: Gluten free goodness
1/14/23, 9:14 AM - Epochx: Tasty and Easy
1/14/23, 9:08 AM - Epochx: Quick, Yummy, Unusual Soup
1/14/23, 2:41 PM - Epochx: Eh...
1/14/23, 9:08 PM - Epochx: Horrible smell
1/14/23, 0:31 AM - Epochx: For $2.00 a box it's okay
1/14/23, 2:44 PM - Epochx: Tasteless mess
1/14/23, 1:20 PM - Epochx: Yum!
1/14/23, 3:40 PM - Epochx: tasty and so easy
1/14/23, 10:55 AM - Epochx: Hot Hot Hot
1/15/23, 6:17 PM - Epochx: Very Good Thai Green Curry!!!
1/15/23, 9:51 PM - Epochx: Curry Paste
1/15/23, 3:50 PM - Epochx: Tons of flavor, very spicy, excellent.
1/16/23, 2:16 PM - Epochx: House Blend is good coffee
1/16/23, 1:09 PM - Epochx: my order
1/15/23, 2:36 PM - Epochx: DELICIOUS!
1/15/23, 1:04 PM - Epochx: Soooooo good!!!
1/16/23, 11:51 AM - Epochx: New Favorite
1/16/23, 9:53 AM - Epochx: Nice tea...very strong cranberry flavor
1/16/23, 7:40 AM - Epochx: Best Tea Ever
1/16/23, 7:03 AM - Epochx: Delicious!
1/16/23, 5:03 AM - Epochx: Delicious Cup o' Tea
1/16/23, 3:04 PM - Epochx: product is great price is insane
1/15/23, 6:40 AM - Epochx: Jittery, lacks body
1/15/23, 1:50 PM - Epochx: High Quality My Dog Enjoys and My Budget Does Too!
1/15/23, 10:56 AM - Epochx: This is great dog food!
1/15/23, 5:09 PM - Epochx: I would give Harmony Farms extra stars if I could!
1/15/23, 4:55 PM - Epochx: Awesome!
1/15/23, 4:53 PM - Epochx: Quality dog food delivered to your door!
1/16/23, 4:07 AM - Epochx: Didn't do well for my dog
1/15/23, 3:21 PM - Epochx: The Cat likes it, too!
1/15/23, 2:42 PM - Epochx: My fussy Min. Dachshund loves the taste!
1/15/23, 1:14 PM - Epochx: My dogs love it!!!
1/16/23, 8:22 AM - Epochx: Passed the taste test!
1/15/23, 11:12 PM - Epochx: Our ten year old doxie
1/15/23, 7:10 PM - Epochx: Excellent for Wheaten Terrier's Sensitive Tummies!
1/16/23, 9:14 AM - Epochx: My dog now sheds less!
1/15/23, 5:38 PM - Epochx: My Dogs Love It
1/15/23, 9:56 AM - Epochx: Very Good
1/16/23, 0:30 AM - Epochx: Good Dog Food
1/16/23, 0:30 AM - Epochx: Hard to find locally
1/16/23, 9:17 AM - Epochx: Good product:
1/16/23, 9:11 AM - Epochx: My dog loves this dog food.
1/16/23, 7:32 AM - Epochx: Harmony Farms Review
1/16/23, 6:50 AM - Epochx: Both formulas are excellent for my dogs!
1/16/23, 6:23 AM - Epochx: Fabulous food!
1/16/23, 3:54 AM - Epochx: Great Dog Food
1/16/23, 2:18 AM - Epochx: Great dog food!
1/16/23, 1:37 AM - Epochx: Dog Likes It, Great Value
1/16/23, 0:59 AM - Epochx: Delighted with Amazon.com
1/16/23, 0:04 AM - Epochx: Great Dog Food :O)
1/15/23, 10:29 PM - Mission "Impossible": The best food for dogs!
1/16/23, 7:43 AM - Mission "Impossible": Solved 2 different digestive issues for 2 different dogs!
1/15/23, 8:54 PM - Mission "Impossible": No good . . .
1/16/23, 9:11 AM - Mission "Impossible": yummy
1/16/23, 9:11 AM - Mission "Impossible": Great Item
1/16/23, 9:10 AM - Mission "Impossible": Excellent chips
1/16/23, 9:08 AM - Mission "Impossible": Perfect for WW followers
1/16/23, 9:02 AM - Mission "Impossible": Variety pack, packed lunches
1/16/23, 9:02 AM - Mission "Impossible": Loved all the flavor except salt and pepper!
1/16/23, 9:02 AM - Mission "Impossible": chips
1/16/23, 8:58 AM - Mission "Impossible": Good as a sampler pack of the various flavors
1/16/23, 8:54 AM - Mission "Impossible": These tastes pretty good
1/16/23, 8:47 AM - Mission "Impossible": Didn't care for the variety selections
1/16/23, 8:35 AM - Mission "Impossible": BEWARE! THESE ARE ADDICTING!
1/16/23, 8:34 AM - Mission "Impossible": Yum yum love me POP Chips
1/16/23, 7:49 AM - Mission "Impossible": Can't beat the taste.
1/16/23, 7:35 AM - Mission "Impossible": Great chips - and tasty too
1/16/23, 7:35 AM - Mission "Impossible": Delicious alternative to greasy traditional chips!
1/16/23, 7:20 AM - Mission "Impossible": Great snacking alternative!
1/16/23, 7:13 AM - Mission "Impossible": Great Gluten-free snack and healthy
1/16/23, 7:13 AM - Mission "Impossible": I like all but one
1/16/23, 6:34 AM - Mission "Impossible": Pop Chips
1/16/23, 6:31 AM - Mission "Impossible": Yummy Yummies
1/16/23, 6:28 AM - Mission "Impossible": Great tasting chips alternative
1/16/23, 6:24 AM - Mission "Impossible": Mmm-Mmm-Mmm!!!
1/16/23, 6:24 AM - Mission "Impossible": Better than expected
1/16/23, 6:21 AM - Mission "Impossible": Great Snack!
1/16/23, 6:15 AM - Mission "Impossible": pretty good. not healthy like an apple but...
1/16/23, 6:08 AM - Mission "Impossible": Pop0chips
1/16/23, 5:54 AM - Mission "Impossible": Love them!
1/16/23, 5:51 AM - Mission "Impossible": Great product and at a great price
1/16/23, 5:35 AM - Mission "Impossible": Popchips Review
1/16/23, 5:29 AM - Mission "Impossible": Don't Defeat the Purpose by Eating Two Bags at Once!
1/16/23, 5:21 AM - Mission "Impossible": Great for diet
1/16/23, 5:08 AM - Mission "Impossible": Best Chips Ever
1/16/23, 4:55 AM - Mission "Impossible": Pop Chips
1/16/23, 4:55 AM - Mission "Impossible": A yummy alternative to high-fat chips!
1/16/23, 4:45 AM - Mission "Impossible": yummy popchips
1/16/23, 4:22 AM - Mission "Impossible": Taste yummy but watch out for yeast extract intolerance!
1/16/23, 4:20 AM - Mission "Impossible": Love Pop Chips!
1/16/23, 4:14 AM - Mission "Impossible": Pop Crisps
1/16/23, 4:14 AM - Mission "Impossible": GREAT PRODUCT!
1/16/23, 4:07 AM - Mission "Impossible": Did not care for these. Only liked bbq. Wondering why these are best-sellers
1/16/23, 3:57 AM - Mission "Impossible": OMG!  So delicious
1/16/23, 3:57 AM - Mission "Impossible": great chips
1/16/23, 2:19 AM - Mission "Impossible": Great product
1/16/23, 2:18 AM - Mission "Impossible": they grow on you!
1/16/23, 2:18 AM - Mission "Impossible": Yummy:)
1/16/23, 2:11 AM - Mission "Impossible": Best chips!
1/16/23, 1:59 AM - Mission "Impossible": Perfect Pop Chips
1/16/23, 1:58 AM - Mission "Impossible": Just my 2 cents...
1/16/23, 1:50 AM - Mission "Impossible": Quite delicious but not as good as real chips
1/16/23, 1:35 AM - Mission "Impossible": Interesting... however I've found something else...
1/16/23, 1:04 AM - Mission "Impossible": Love These Chips
1/16/23, 1:03 AM - Mission "Impossible": tast great less lard.
1/16/23, 0:51 AM - Mission "Impossible": OMG!!!! The Best Snack Ever!!!
1/16/23, 0:48 AM - Mission "Impossible": Great price; Great taste;
1/16/23, 0:43 AM - Mission "Impossible": yum
1/16/23, 0:38 AM - Mission "Impossible": O. M. G. These ROCK!
1/16/23, 0:38 AM - Mission "Impossible": Popchips
1/16/23, 0:24 AM - Mission "Impossible": The Snacker
1/16/23, 0:23 AM - Mission "Impossible": loooooooove them
1/16/23, 0:08 AM - Mission "Impossible": Pop chips are the best!!!!
1/16/23, 0:07 AM - Mission "Impossible": Great and unique chips!
1/16/23, 0:07 AM - Mission "Impossible": Some are REALLY tasty, others a little "chemical" tasting
1/16/23, 0:07 AM - Mission "Impossible": Tasty!
1/16/23, 0:04 AM - Mission "Impossible": Topchips!
1/16/23, 0:01 AM - Mission "Impossible": Yummy!
1/16/23, 0:00 AM - Mission "Impossible": Too salty
1/15/23, 11:45 PM - Mission "Impossible": I LOVE POPCHIPS!!!
1/15/23, 11:42 PM - Mission "Impossible": Awesome Snack
1/15/23, 11:34 PM - Mission "Impossible": YUM
1/15/23, 11:19 PM - Mission "Impossible": Loved the chips
1/15/23, 11:16 PM - Mission "Impossible": Gotta Love Em
1/15/23, 11:02 PM - Mission "Impossible": Popchips
1/15/23, 10:56 PM - Mission "Impossible": Fun Game
1/15/23, 10:52 PM - Mission "Impossible": Yum
1/15/23, 10:50 PM - Mission "Impossible": Love these!
1/15/23, 10:43 PM - Mission "Impossible": Healthy and Tasty
1/15/23, 10:39 PM - Mission "Impossible": POP Chips on the go
1/15/23, 10:16 PM - Mission "Impossible": Popchips - Love !
1/15/23, 10:06 PM - Mission "Impossible": Great Snack!
1/15/23, 10:04 PM - Mission "Impossible": Popchips  variety box
1/15/23, 10:04 PM - Mission "Impossible": Pop Chips Rule
1/15/23, 10:01 PM - Mission "Impossible": Pop Chips 6 flavor Variety Pack
1/15/23, 9:54 PM - Mission "Impossible": Pop chips...love them!
1/15/23, 9:33 PM - Mission "Impossible": THOUGHTS ON PRODUCT
1/15/23, 9:30 PM - Mission "Impossible": Love Love Love
1/15/23, 9:27 PM - Mission "Impossible": Delicious!
1/15/23, 9:27 PM - Mission "Impossible": Popchips Satisfy my Salt and Crunch Craving
1/15/23, 9:24 PM - Mission "Impossible": YUM!
1/15/23, 9:14 PM - Mission "Impossible": Very happy!
1/15/23, 9:10 PM - Mission "Impossible": Awesome Product
1/15/23, 9:08 PM - Mission "Impossible": Great Alternative to Fried
1/15/23, 9:00 PM - Mission "Impossible": Delicious!
1/15/23, 9:00 PM - Mission "Impossible": Yummy, healthy snack!
1/15/23, 8:58 PM - Mission "Impossible": Popchips are wonderfully tasty
1/15/23, 8:57 PM - Mission "Impossible": PopChips Are The Best!!
1/15/23, 8:54 PM - Mission "Impossible": Delish
1/15/23, 8:52 PM - Mission "Impossible": Different and yummy!
1/15/23, 8:52 PM - Shari S. Durham: Loved these chips!
1/15/23, 8:32 PM - Shari S. Durham: Great alternative to regular potato chips
1/15/23, 8:29 PM - Shari S. Durham: Pop Chips
1/15/23, 0:48 AM - Shari S. Durham: Yum!
1/15/23, 9:25 AM - Shari S. Durham: Awesome Chips!!!!!!!!!!!
1/15/23, 0:34 AM - Shari S. Durham: Popchips RULE!
1/15/23, 5:51 PM - Shari S. Durham: Definite POP - Not Baked or Fried
1/16/23, 8:36 AM - Shari S. Durham: Delicious! Even For Those Who Dont Enjoy Healthy Food
1/15/23, 2:32 PM - Shari S. Durham: Beware hidden ingredients
1/16/23, 9:25 AM - Shari S. Durham: Popchips for Weightwatchers
1/16/23, 4:59 AM - Shari S. Durham: Pringles, instant coffee, and Stephen Baldwin
1/16/23, 11:29 AM - Shari S. Durham: Barely any chips in the bag!
1/16/23, 10:10 AM - Shari S. Durham: Great Snack!
1/15/23, 8:26 PM - Shari S. Durham: Pretty delicious
1/15/23, 8:26 PM - Shari S. Durham: Great Snack!!
1/15/23, 8:26 PM - Shari S. Durham: Popchips are great!
1/15/23, 8:25 PM - Shari S. Durham: love this snack
1/15/23, 8:25 PM - Shari S. Durham: My kids and I ate these up!!
1/15/23, 8:13 PM - Shari S. Durham: Pop Chips...Yum!!!
1/15/23, 8:12 PM - Shari S. Durham: Short and Sweet
1/15/23, 8:06 PM - Shari S. Durham: Can I just say Yum?
1/15/23, 8:02 PM - Shari S. Durham: Perfect
1/15/23, 8:02 PM - Shari S. Durham: Great tasting
1/15/23, 7:58 PM - Shari S. Durham: Amazing
1/15/23, 7:53 PM - Shari S. Durham: Salt and Vinegar and BBQ rock!
1/15/23, 7:50 PM - Shari S. Durham: Watch out- they are addictive
1/15/23, 7:50 PM - Shari S. Durham: Def a good buy
1/15/23, 7:49 PM - Shari S. Durham: Scrumptious!
1/15/23, 7:48 PM - Shari S. Durham: Delish!
1/15/23, 7:45 PM - Shari S. Durham: Chips
1/15/23, 7:42 PM - Shari S. Durham: Very Happy Surprise
1/15/23, 7:42 PM - Shari S. Durham: Great chips, poor packaging
1/15/23, 7:42 PM - Shari S. Durham: What a treat!
1/15/23, 7:39 PM - Shari S. Durham: Best Healthy Potato Chip!
1/15/23, 7:37 PM - Shari S. Durham: I LUUUV me some POPCHIPS!!!
1/15/23, 7:37 PM - Shari S. Durham: Good crunch & light taste
1/15/23, 7:36 PM - Shari S. Durham: Pop Chips are great
1/15/23, 7:30 PM - Shari S. Durham: Good way to try the different flavors
1/15/23, 7:26 PM - Shari S. Durham: Yummy!!!!!
1/15/23, 7:26 PM - Shari S. Durham: GREAT PURCHASE
1/15/23, 7:24 PM - Shari S. Durham: excellent!
1/15/23, 7:19 PM - Shari S. Durham: Delicious
1/15/23, 7:04 PM - Shari S. Durham: Eat without feeling guilty!
1/15/23, 7:01 PM - Shari S. Durham: Pop chips variety
1/15/23, 7:00 PM - Shari S. Durham: Popchips
1/15/23, 6:57 PM - Shari S. Durham: These definately are 5 stars.  Deeelicious
1/15/23, 6:54 PM - Shari S. Durham: Love pop chips!
1/15/23, 6:31 PM - Shari S. Durham: pop chip goodness
1/15/23, 6:31 PM - Shari S. Durham: Delicious and The Right Amount
1/15/23, 6:25 PM - Shari S. Durham: BEST chips!!
1/15/23, 6:04 PM - Shari S. Durham: Love those chips
1/15/23, 5:54 PM - Shari S. Durham: LOVE THIS PRODUCT
1/15/23, 5:49 PM - Shari S. Durham: Everyone Should To Try These At Least Once
1/15/23, 5:36 PM - Shari S. Durham: Fully enjoyed
1/15/23, 4:56 PM - Shari S. Durham: Great low-cal snack!
1/15/23, 4:55 PM - Shari S. Durham: So good!
1/15/23, 4:46 PM - Shari S. Durham: these are awesome
1/15/23, 4:43 PM - Shari S. Durham: Great chips
1/15/23, 4:27 PM - Shari S. Durham: popchips hmmmm hmmm hmmm
1/15/23, 4:07 PM - Shari S. Durham: Loved it!
1/15/23, 4:04 PM - Shari S. Durham: Worth The Money!
1/15/23, 4:04 PM - Shari S. Durham: I love Pop Chips!
1/15/23, 3:54 PM - Shari S. Durham: Great chip substitute!
1/15/23, 3:25 PM - Shari S. Durham: Great low-fat no cholestrol snack
1/15/23, 3:21 PM - Shari S. Durham: Great Chips
1/15/23, 3:11 PM - Shari S. Durham: Entire family loves them
1/15/23, 3:07 PM - Shari S. Durham: YUM!!!
1/15/23, 3:07 PM - Shari S. Durham: CHIP LOVER
1/15/23, 3:02 PM - Shari S. Durham: BBQ is terrific!
1/15/23, 2:47 PM - Shari S. Durham: popchips r hella good
1/15/23, 2:47 PM - Shari S. Durham: Excellent
1/15/23, 2:29 PM - Shari S. Durham: Excellent Product
1/15/23, 2:29 PM - Shari S. Durham: Pop Chips - Better tasting and Better for you than regular chips
1/15/23, 2:29 PM - Shari S. Durham: Pop Chips
1/15/23, 2:29 PM - Shari S. Durham: Popchips 6 Flavor Variety
1/15/23, 2:29 PM - Shari S. Durham: Popchips
1/15/23, 2:22 PM - Shari S. Durham: Yummy!
1/15/23, 2:18 PM - Shari S. Durham: Great Natural Potatoe Chips With Low Calories!
1/15/23, 2:18 PM - Shari S. Durham: Taste great
1/15/23, 2:05 PM - Shari S. Durham: Love at first bite
1/15/23, 1:40 PM - Shari S. Durham: Fantastic Product !!!!!
1/15/23, 1:14 PM - Shari S. Durham: Sooo tasty
1/15/23, 1:09 PM - Shari S. Durham: absolutely delicious
1/15/23, 0:15 AM - Shari S. Durham: Healthier, better tasting option
1/15/23, 0:10 AM - Shari S. Durham: Deliciousness for little calories!
1/15/23, 0:08 AM - Shari S. Durham: Healthy yum.
1/15/23, 0:07 AM - Shari S. Durham: Excellent!!
1/15/23, 10:26 AM - Shari S. Durham: Popchips - The perfect snack to pop in your mouth
1/15/23, 10:09 AM - Shari S. Durham: LOVE THEM
1/15/23, 10:00 AM - Shari S. Durham: crunch without guilt
1/15/23, 9:51 AM - Shari S. Durham: great taste now in a 100 calorie bag
1/15/23, 9:44 AM - Shari S. Durham: Love this product!!
1/16/23, 2:54 AM - Shari S. Durham: Weird flavors....
1/16/23, 3:08 AM - Shari S. Durham: Can someone post some of the nutrition facts?
1/15/23, 8:44 PM - Shari S. Durham: These are a great snack
1/16/23, 0:31 AM - Shari S. Durham: pretty good  - but won't buy again
1/16/23, 11:42 AM - Shari S. Durham: Not impressed
1/16/23, 9:47 AM - Shari S. Durham: disgusting
1/16/23, 7:20 AM - Shari S. Durham: Pop Chips Are Tops
1/16/23, 3:48 AM - Shari S. Durham: I did not like the taste!
1/16/23, 3:47 AM - Mommy of Lily: Didn't like the taste
1/16/23, 3:41 AM - Mommy of Lily: Amazing!!
1/16/23, 3:41 AM - Mommy of Lily: popchips
1/16/23, 3:34 AM - Mommy of Lily: fantastic mix of Popchip goodness
1/16/23, 3:33 AM - Mommy of Lily: Popchips 6-flavor Variety Pack.
1/16/23, 3:25 AM - Mommy of Lily: Popchips
1/16/23, 2:51 AM - Mommy of Lily: Yummy PopChips
1/16/23, 2:36 AM - Mommy of Lily: YUM we love pop chips!
1/16/23, 2:34 AM - Mommy of Lily: pop chips
1/16/23, 2:25 AM - Mommy of Lily: Great Chip
1/16/23, 1:29 AM - Mommy of Lily: Great Chips - Love the Salt & Vinegar
1/16/23, 0:18 AM - Mommy of Lily: We really didn't like these!
1/15/23, 10:22 PM - Mommy of Lily: They're Okay.......
1/15/23, 10:17 PM - Mommy of Lily: Excellent 2 thumbs up !!!!
1/16/23, 1:50 AM - Mommy of Lily: Nothing special - Baked Lays taste better
1/16/23, 0:17 AM - Mommy of Lily: Cross between Pringles and a rice cake. The bonus is they're all natural
1/16/23, 11:16 AM - Mommy of Lily: Too strong of flavors
1/16/23, 9:28 AM - Mommy of Lily: If you're expecting full chip flavor reconsider getting another brand of chips.
1/16/23, 5:44 AM - Mommy of Lily: Great for losing weight!
1/16/23, 5:42 AM - Mommy of Lily: Good chips and not bad for you
1/16/23, 3:34 AM - Mommy of Lily: Over Priced - Cheaper at Costco
1/15/23, 9:27 PM - Mommy of Lily: Tasty but Salty
1/15/23, 8:34 PM - Mommy of Lily: Not as good as I was lead to believe
1/15/23, 5:21 PM - Mommy of Lily: GREAT CRUNCH SOLUTION!!!!!!!!!!!!!!
1/15/23, 4:06 PM - Mommy of Lily: Pop Chips, yum!
1/15/23, 2:29 PM - Mommy of Lily: Good but didn't receive what was ordered
1/16/23, 1:56 AM - Mommy of Lily: Popchips vs Baked Lays? Baked Lays taste MUCH better.
1/15/23, 5:15 PM - Mommy of Lily: weight?
1/16/23, 0:15 AM - Mommy of Lily: NOT worth the online order NOR is cheap $$$!
1/16/23, 5:11 AM - Mommy of Lily: Did not work for me
1/15/23, 3:00 PM - Mommy of Lily: good chips but....
1/16/23, 8:18 AM - Mommy of Lily: 'Healthy chips'
1/16/23, 0:47 AM - Mommy of Lily: Not so great
1/16/23, 0:24 AM - Mommy of Lily: They Have Been Around Forever But You Did Not Know It
1/15/23, 10:01 PM - Mommy of Lily: Hidden sources of MSG in the ingredients
1/15/23, 4:26 PM - Mommy of Lily: get the salt and pepper box instead
1/16/23, 8:47 AM - Mommy of Lily: Awful
1/15/23, 8:48 PM - Mommy of Lily: TASTE AVERAGE, INSANELY EXPENSIVE
1/15/23, 10:52 AM - Mommy of Lily: Low calorie snack
1/15/23, 5:35 PM - Mommy of Lily: Not My Type of Potato Chips.
1/16/23, 0:51 AM - Mommy of Lily: too salty
1/16/23, 10:10 AM - Mommy of Lily: Satisfies the salty snack craving
1/16/23, 9:15 AM - Mommy of Lily: 2 POINTS PLUS  on Weight Watchers
1/16/23, 7:20 AM - Mommy of Lily: So Good
1/16/23, 6:36 AM - Mommy of Lily: Melts In Your Mouth
1/16/23, 4:49 AM - Mommy of Lily: I only like the plain ones
1/16/23, 3:50 AM - Mommy of Lily: Ships to APO
1/16/23, 3:33 AM - Mommy of Lily: Tasty, Crunchy, and Filling
1/16/23, 3:12 AM - Mommy of Lily: Yum!
1/16/23, 2:29 AM - Mommy of Lily: Low in Calories, High in Taste
1/16/23, 2:09 AM - Mommy of Lily: zippy
1/16/23, 1:19 AM - Mommy of Lily: Buy them less from here!!! (While you can)
1/16/23, 1:14 AM - Mommy of Lily: delicious
1/16/23, 1:07 AM - Mommy of Lily: My new favorite chips!
1/16/23, 0:15 AM - Mommy of Lily: This picky eater loves them (most flavors)
1/15/23, 9:02 PM - Mommy of Lily: Pop Chips Rock!
1/15/23, 7:01 PM - Mommy of Lily: Great guiltless snack
1/15/23, 2:16 PM - Mommy of Lily: Tasty potato chips, low in calories, great flavor
1/15/23, 0:36 AM - Mommy of Lily: Love, love, love these chips!!
1/15/23, 0:36 AM - Mommy of Lily: All the taste, but where's the fat?
1/15/23, 5:35 PM - Mommy of Lily: Not bad, but not impressive! .8 oz equals about 15 chips.
1/16/23, 1:39 AM - Mommy of Lily: Yummm!
1/15/23, 6:12 PM - Mommy of Lily: Not bad But not great
1/16/23, 3:05 PM - Mommy of Lily: pop chips rock
1/16/23, 3:04 PM - Mommy of Lily: I love these chips!
1/16/23, 3:00 PM - Mommy of Lily: Great Snack
1/16/23, 2:58 PM - Mommy of Lily: Yum!
1/16/23, 2:49 PM - Mommy of Lily: taste is perfect....
1/16/23, 2:47 PM - Mommy of Lily: Good Snack Choice
1/16/23, 2:45 PM - Mommy of Lily: Delicious and healthy chips!
1/16/23, 2:44 PM - Mommy of Lily: Popchips!
1/16/23, 2:44 PM - Mommy of Lily: pop chips
1/16/23, 2:44 PM - Mommy of Lily: popchips
1/16/23, 2:26 PM - Mommy of Lily: Popchips! My new favorite snack
1/16/23, 2:24 PM - Mommy of Lily: Great Chips
1/16/23, 2:21 PM - Mommy of Lily: Low Calorie, Tasty Snack!
1/16/23, 2:19 PM - Mommy of Lily: healthy, texture good, flavor strange
1/16/23, 2:12 PM - Mommy of Lily: Great Taste, Crunchy
1/16/23, 2:12 PM - Mommy of Lily: YUM
1/16/23, 1:42 PM - Mommy of Lily: love em! so does my big fat belly
1/16/23, 1:35 PM - Mommy of Lily: New favorite munchies, found!
1/16/23, 1:35 PM - Mommy of Lily: Treat of the Day
1/16/23, 1:29 PM - Mommy of Lily: Yummy!!!
1/16/23, 1:16 PM - Mommy of Lily: Pop Chips = Great!!
1/16/23, 0:23 AM - Mommy of Lily: if you love them... you love them... popchips
1/16/23, 11:48 AM - Mommy of Lily: Not bad
1/16/23, 11:48 AM - Mommy of Lily: poor,poor packaging
1/16/23, 11:44 AM - Mommy of Lily: partially good
1/16/23, 11:25 AM - Mommy of Lily: Love these, good variety pack
1/16/23, 11:03 AM - Mommy of Lily: Popchips Does It for Me
1/16/23, 10:55 AM - Mommy of Lily: Snack of the hour!
1/16/23, 10:50 AM - Mommy of Lily: My kids only liked one flavor!
1/16/23, 10:42 AM - Mommy of Lily: Pop Chips...Yummy!
1/16/23, 10:42 AM - Mommy of Lily: Taste alright, but normal chips are better
1/16/23, 10:42 AM - Mommy of Lily: Love it! so tasty!
1/16/23, 10:33 AM - Mommy of Lily: Pop Delicious
1/16/23, 10:30 AM - Mommy of Lily: Like slightly charred popcorn
1/16/23, 10:23 AM - Mommy of Lily: Yummie!
1/16/23, 10:22 AM - Mommy of Lily: Delicious!
1/16/23, 10:19 AM - Mommy of Lily: Very good!!
1/16/23, 10:09 AM - babylou319: overrated
1/16/23, 10:01 AM - babylou320: Not for everyone.. but I love it!
1/16/23, 10:01 AM - babylou321: Most flavors are very good
1/16/23, 9:50 AM - babylou322: Great idea
1/16/23, 9:46 AM - babylou323: Healthy and Good, What?!?!
1/16/23, 9:41 AM - babylou324: Healthy and Delicious!
1/16/23, 9:33 AM - babylou325: Pop chips 6-flavor variety
1/16/23, 9:14 AM - babylou326: The Best Snack Food!
1/16/23, 10:09 AM - babylou327: Soo GOOD!
1/16/23, 9:48 AM - babylou328: Too good to continue for long.
1/16/23, 9:27 AM - babylou329: Delicious
1/16/23, 8:35 AM - babylou330: The best Cheetos out there
1/15/23, 11:15 PM - babylou331: Found the solution on how to open it
1/15/23, 9:48 AM - babylou332: WORKS FOR ME AND SAVES ME $$$$
1/15/23, 9:50 AM - babylou333: This thing is great!
1/15/23, 3:24 PM - babylou334: A little hard to open
1/15/23, 3:41 PM - babylou335: Great concept, poor product
1/16/23, 2:19 AM - babylou336: Too small, too hard to open
1/16/23, 9:46 AM - babylou337: can't open
1/16/23, 7:39 AM - babylou338: Great idea, such a pain to open and close
1/16/23, 4:10 AM - babylou339: Keeps basil on the counter...cat proof!
1/16/23, 2:31 AM - babylou340: Save your money!
1/16/23, 2:09 AM - babylou341: keeps herbs fresh, looks nice--awkward to use
1/16/23, 1:17 AM - babylou342: Would be a great product....if it was easier to open
1/16/23, 1:01 AM - babylou343: Works, but hard to open...Buy larger version instead of pod
1/15/23, 11:49 PM - babylou344: Sorry Oprah, not one of my 'favorite things'
1/15/23, 11:06 PM - babylou345: Wilted hopes
1/15/23, 5:52 PM - babylou346: just works
1/15/23, 4:06 PM - babylou347: WONDERFUL!!  This is perfect and saves me a fortune
1/15/23, 9:51 AM - babylou348: Stylish Saver
1/15/23, 8:48 AM - babylou349: Caveat emptor! Disappointing
1/15/23, 3:25 PM - babylou350: this gadget just doesn't do the job.
1/16/23, 2:29 PM - babylou351: Works great!
1/16/23, 1:23 PM - babylou352: The Picture is Misleading
1/16/23, 0:34 AM - babylou353: I am buying more!
1/14/23, 8:16 AM - babylou354: Inside of can corroded
1/15/23, 9:34 AM - babylou355: Not Safe!
1/15/23, 7:27 PM - babylou356: Tastes like mushy pineapple
1/16/23, 7:37 AM - babylou357: Rotten, spoiled taste and look!!
1/15/23, 8:13 AM - babylou358: Great Option for Keeping Fruit at Work
1/15/23, 6:02 AM - babylou359: Great Dessert!
1/15/23, 6:07 PM - babylou360: tropical fruit
1/15/23, 6:38 AM - babylou361: Best canned fruit I have ever eatten
1/14/23, 2:24 PM - babylou362: Organic Fruit Review
1/16/23, 1:29 PM - babylou363: Okay but some weird flavors
1/15/23, 10:20 AM - babylou364: So much easier!
1/15/23, 7:59 AM - babylou365: makes a quick,tasty martini
1/15/23, 10:13 AM - babylou366: Dirty Martini Olive Juice
1/15/23, 2:03 PM - babylou367: A good dirty martini
1/15/23, 4:22 PM - babylou368: White Flecks?
1/16/23, 3:10 PM - babylou369: Love this!
1/16/23, 11:52 AM - babylou370: Better than the real stuff
1/16/23, 10:12 AM - babylou371: This is the stuff !!
1/16/23, 7:33 AM - babylou372: My husband loves his Dirty Martinis...
1/16/23, 2:28 AM - babylou373: Dirty Martini Olive Juice
1/16/23, 0:48 AM - babylou374: olive juice
1/15/23, 10:16 PM - babylou375: Great Dirty Matinis
1/15/23, 7:46 PM - babylou376: Dirty Martini
1/16/23, 6:27 AM - babylou377: Not really olive juice
1/16/23, 8:41 AM - babylou378: It's not worth it!
1/16/23, 0:27 AM - babylou379: Morton Sea Salt
1/16/23, 0:04 AM - babylou380: Hard to control the quantity.
1/16/23, 6:40 AM - babylou381: Great Cooking Oil !
1/15/23, 5:02 PM - babylou382: Yum
1/15/23, 6:17 PM - babylou383: More Than A Little Mint
1/16/23, 4:52 AM - babylou384: Absolutely wonderful
1/16/23, 3:59 AM - babylou385: Great to feed others!
1/16/23, 2:11 PM - babylou386: Sugar Bomb
1/16/23, 7:30 AM - babylou387: These candies are delightful
1/16/23, 1:59 PM - babylou388: Great taste, less sodium
1/16/23, 11:38 AM - babylou389: sea salt
1/16/23, 9:53 AM - babylou390: Nice condiment
1/16/23, 5:09 AM - babylou391: Great product.
1/16/23, 0:38 AM - babylou392: A taste that needs to be acquired...
1/16/23, 4:37 AM - babylou393: Pok Chops
1/15/23, 11:08 PM - babylou394: So yummy-wonderful inexpensive gift item!
1/16/23, 8:16 AM - babylou395: Totally delicious and delightful!
1/16/23, 7:33 AM - babylou396: Excellent service!
1/16/23, 11:15 AM - babylou397: Great starting pack!
1/16/23, 9:01 AM - babylou398: ddjj
1/16/23, 8:55 AM - babylou399: Some Variety
1/16/23, 8:51 AM - babylou400: Disappointing
1/16/23, 9:10 AM - babylou401: Disappointed!!
1/16/23, 9:33 AM - babylou402: 20 of the 35 were decaf...Disapointed
1/16/23, 6:57 AM - babylou403: Teeny, Tiny Little Treats, But Good For What They Are, A Healthy Reward For Following Commands
1/16/23, 3:53 AM - babylou404: Great for training
1/16/23, 11:21 AM - babylou405: Just an FYI
1/15/23, 5:11 AM - babylou406: CAUTION!!!  ADDICTIVE CANDY&lt; VERY >
1/16/23, 5:51 AM - babylou407: Mmmmmmm....Sooo good!!!
1/15/23, 8:51 AM - babylou408: OUTSTANDING WERITHERS CANDY!!
1/16/23, 5:44 AM - babylou409: A close 2nd to the original hard candy
1/16/23, 9:37 AM - babylou410: Good taste, way too hard.
1/15/23, 0:27 AM - babylou411: This is great stuff
1/15/23, 0:02 AM - babylou412: Best waffle mix I had in my life
1/15/23, 7:40 AM - babylou413: Stonewall Kitchen Pancake and Waffle Mix Is Grrrrrreat!!!
1/14/23, 10:03 PM - babylou414: Delicious but pricey.
1/15/23, 3:37 PM - babylou415: Great Waffles for us non-cooks
1/15/23, 7:32 PM - babylou416: Excellent Fluffy Pancakes.....
1/15/23, 11:24 AM - babylou417: Good Basic Mix
1/15/23, 3:36 PM - babylou418: Good pancakes, lots of work
1/14/23, 11:13 PM - Mrs. G "B. Real": waffles, schmaffles !!
1/14/23, 3:21 PM - Mrs. G "B. Real": Awesome
1/14/23, 11:24 PM - Mrs. G "B. Real": Great tasting pancake  mix
1/15/23, 10:20 AM - Mrs. G "B. Real": Stonewall Pancake Mix
1/16/23, 8:29 AM - Mrs. G "B. Real": Delicious waffles!
1/15/23, 1:39 AM - Mrs. G "B. Real": Great taste and great price! A+++
1/15/23, 9:08 PM - Mrs. G "B. Real": Disappointed with my first farmhouse pancake
1/16/23, 1:33 PM - Mrs. G "B. Real": Maybe it was just my batch?
1/16/23, 9:44 AM - Mrs. G "B. Real": BEST PANCAKES OF MY LIFE
1/16/23, 5:38 AM - Mrs. G "B. Real": pretty darn good but at an increased cost
1/16/23, 4:39 AM - Mrs. G "B. Real": Best pancakes EVER!!
1/16/23, 4:29 AM - Mrs. G "B. Real": I'm a believer
1/16/23, 2:03 AM - Mrs. G "B. Real": Excellent
1/16/23, 1:46 AM - Mrs. G "B. Real": A great backup from scratch
1/16/23, 0:54 AM - Mrs. G "B. Real": We love Stonewall Kitchen
1/16/23, 0:43 AM - Mrs. G "B. Real": Great Waffle's every time
1/16/23, 0:12 AM - Mrs. G "B. Real": Perfect Waffles
1/15/23, 9:24 PM - Mrs. G "B. Real": Deeeeelicious!
1/15/23, 6:08 PM - Mrs. G "B. Real": Delicious waffles in minutes!
1/15/23, 5:48 PM - Mrs. G "B. Real": Great Belgian waffle batter!
1/15/23, 5:05 PM - Mrs. G "B. Real": Stonewall Kitchen pancake mix
1/15/23, 2:06 PM - Mrs. G "B. Real": Farmhouse Waffle Mix
1/15/23, 4:48 PM - Mrs. G "B. Real": Our favorite breakfast choice
1/15/23, 2:13 PM - Mrs. G "B. Real": Stonewall Pancake and Waffle Mix
1/15/23, 1:43 PM - Mrs. G "B. Real": Excellent choice for Belgian Waffles
1/15/23, 0:56 AM - Mrs. G "B. Real": Great Waffle Mix
1/16/23, 3:23 AM - Mrs. G "B. Real": Tasty mixture but
1/15/23, 3:30 PM - Mrs. G "B. Real": Our Favorite
1/14/23, 11:39 PM - Mrs. G "B. Real": Pancake Mix the best!
1/16/23, 3:07 PM - Mrs. G "B. Real": Mouthful in Name Only
1/16/23, 3:05 PM - Mrs. G "B. Real": great tasting pancakes and waffles
1/16/23, 3:04 PM - Mrs. G "B. Real": Best Belgian Waffles in No Time!
1/16/23, 2:58 PM - Mrs. G "B. Real": I love this pancake mix
1/16/23, 1:09 PM - Mrs. G "B. Real": Family  breakfast  (Grand Kids & Kids, 20 of us)
1/16/23, 1:07 PM - Mrs. G "B. Real": Delicious and Easy
1/16/23, 0:11 AM - Mrs. G "B. Real": Scrumptious!
1/16/23, 0:10 AM - Mrs. G "B. Real": BEST
1/16/23, 10:17 AM - Mrs. G "B. Real": great stuff
1/16/23, 9:21 AM - Mrs. G "B. Real": The best!
1/16/23, 8:06 AM - Mrs. G "B. Real": YUM!
1/16/23, 7:49 AM - Mrs. G "B. Real": yummmmmmmmmm!
1/16/23, 6:33 AM - Mrs. G "B. Real": pancake/waffle mix
1/16/23, 3:56 AM - Mrs. G "B. Real": The Best Waffle Mix
1/16/23, 3:30 AM - Mrs. G "B. Real": The best waffle mix you can find!
1/16/23, 1:45 AM - Mrs. G "B. Real": Not as sweet as other mixes
1/16/23, 0:59 AM - Mrs. G "B. Real": Hands Down the Best Pancakes Ever
1/15/23, 11:55 PM - Mrs. G "B. Real": best ever!
1/15/23, 10:40 PM - Mrs. G "B. Real": Really good but expensive
1/15/23, 9:43 PM - Mrs. G "B. Real": Banana recipe
1/15/23, 9:37 PM - Mrs. G "B. Real": perfect for the weekend
1/15/23, 8:51 PM - Mrs. G "B. Real": Tasty, texture great
1/15/23, 8:36 PM - Mrs. G "B. Real": Best waffle mix ever!
1/15/23, 7:35 PM - Mrs. G "B. Real": Yummy Yummy Yummy!!!
1/15/23, 7:33 PM - Mrs. G "B. Real": Tasty pancakes - best mix we've ever tried...
1/15/23, 6:28 PM - Mrs. G "B. Real": Best pancakes ever!
1/15/23, 6:23 PM - Mrs. G "B. Real": Addicted
1/15/23, 6:18 PM - Mrs. G "B. Real": Best Breakfast
1/15/23, 5:44 PM - Mrs. G "B. Real": Tasty pancakes, but a little flat
1/15/23, 5:32 PM - Mrs. G "B. Real": Crispy and soft all at once.
1/15/23, 5:25 PM - Mrs. G "B. Real": Does wonders for one's popularity in the kitchen
1/15/23, 5:12 PM - Mrs. G "B. Real": We love it.
1/15/23, 11:38 PM - Mrs. G "B. Real": 0 Stars if I could! YUK YUK YUK
1/14/23, 6:47 PM - Mrs. G "B. Real": The best waffles
1/15/23, 9:36 PM - Mrs. G "B. Real": Not So Great
1/15/23, 11:11 AM - Mrs. G "B. Real": Good but not great
1/15/23, 6:11 AM - Mrs. G "B. Real": Delicious, makes a great gift
1/16/23, 5:26 AM - Mrs. G "B. Real": Nothing special for what you pay
1/16/23, 3:48 AM - Mrs. G "B. Real": Just OK
1/16/23, 0:54 AM - Mrs. G "B. Real": Mine taste better
1/15/23, 5:29 PM - Mrs. G "B. Real": No better than Jiffy
1/16/23, 6:25 AM - Mrs. G "B. Real": processed taste
1/15/23, 6:05 PM - Mrs. G "B. Real": Nice Pancakes, But Not As Simple As "Just Add Water" Mix.
1/16/23, 11:44 AM - Mrs. G "B. Real": Delicious!  Very Yummy
1/15/23, 8:41 PM - Mrs. G "B. Real": Not sure what the hype is ...
1/14/23, 4:58 PM - Mrs. G "B. Real": our favorite pancake mix
1/16/23, 6:54 AM - Mrs. G "B. Real": Not too impressed
1/15/23, 7:29 PM - Mrs. G "B. Real": Price versus taste don't add up
1/15/23, 5:16 PM - Mrs. G "B. Real": Confused...
1/15/23, 3:20 PM - Mrs. G "B. Real": good, reliable results, expensive
1/14/23, 9:27 PM - Mrs. G "B. Real": Don't buy any other, this is the best!
1/16/23, 9:57 AM - Mrs. G "B. Real": Very unsatisfied!
1/16/23, 11:24 AM - Mrs. G "B. Real": Deceptive, more like a Christmas Sampler!
1/16/23, 11:22 AM - Mrs. G "B. Real": VERY Unsatisfied
1/16/23, 11:16 AM - Mrs. G "B. Real": Not what I ordered.
1/16/23, 10:07 AM - Mrs. G "B. Real": Extremely Disappointing
1/16/23, 9:46 AM - Mrs. G "B. Real": Not all Summer?
1/16/23, 11:25 AM - Mrs. G "B. Real": Recieved the Holiday Sampler with a Couple Summer Teas
1/16/23, 10:55 AM - Mrs. G "B. Real": Worst Summer EVER
1/16/23, 10:42 AM - Mrs. G "B. Real": Not Summer Items!
1/16/23, 2:13 PM - Mrs. G "B. Real": Are these all the k cups that come out of other packages?
1/16/23, 1:24 PM - Mrs. G "B. Real": Variety matches the (current) picture
1/16/23, 1:12 PM - Mrs. G "B. Real": Ok if you need to figure out what you like
1/16/23, 10:35 AM - Mrs. G "B. Real": kcup brewers pack 35
1/16/23, 10:13 AM - Mrs. G "B. Real": Received 2 iced coffee, 3 iced tea, 2 holiday coffee
1/16/23, 9:10 AM - Mrs. G "B. Real": Interesting assortment
1/16/23, 5:26 AM - Mrs. G "B. Real": Very Good Flavor
1/16/23, 1:06 PM - Mrs. G "B. Real": They should say just add milk....
1/16/23, 2:15 PM - Mrs. G "B. Real": Delicious
1/16/23, 11:54 AM - Mrs. G "B. Real": Great new GMO-free snack!
1/16/23, 8:19 AM - Mrs. G "B. Real": Perfect Gift
1/14/23, 7:24 AM - ARealAVFan: Excellent rice crackers
1/14/23, 3:57 PM - ARealAVFan: Best crackers ever!
1/15/23, 5:05 AM - ARealAVFan: Great for you
1/14/23, 6:46 PM - ARealAVFan: YOU CAN'T EAT JUST ONE!
1/14/23, 1:36 PM - ARealAVFan: Unavailable?!?!?
1/16/23, 2:44 PM - ARealAVFan: Loved!
1/15/23, 11:25 AM - ARealAVFan: Excellent non-gluten product
1/15/23, 6:07 AM - ARealAVFan: Mmmmmmmmm
1/16/23, 2:44 PM - ARealAVFan: Crisp and delicious / extreme price hike
1/16/23, 6:28 AM - ARealAVFan: Rice
1/16/23, 5:03 AM - ARealAVFan: Very good product, especially for gluten and dairy free friends
1/15/23, 3:57 PM - ARealAVFan: crispy crackers w/o Gluten
1/15/23, 3:50 PM - ARealAVFan: Excellent snack
1/15/23, 0:36 AM - ARealAVFan: Great Snack
1/15/23, 9:48 AM - ARealAVFan: Wrong product
1/15/23, 3:23 PM - ARealAVFan: Cheaper from Penta.com
1/16/23, 8:52 AM - ARealAVFan: Much Cheaper through Penta's Website
1/14/23, 6:44 PM - ARealAVFan: wow this stuff is incredible!
1/14/23, 2:24 PM - ARealAVFan: To wash my record collection
1/14/23, 9:54 AM - ARealAVFan: rejuvenating water
1/16/23, 8:44 AM - ARealAVFan: Don't waste your money
1/16/23, 5:35 AM - ARealAVFan: Get's old too quickly!
1/15/23, 6:38 AM - ARealAVFan: Best way to eat Sunflower seeds!
1/15/23, 6:56 PM - ARealAVFan: Awesome Candy!!
1/16/23, 3:01 PM - ARealAVFan: Great product, poor packaging.
1/16/23, 7:19 AM - ARealAVFan: I don't know what I'd do without this...
1/16/23, 8:16 AM - ARealAVFan: We LOVE these
1/16/23, 4:09 AM - ARealAVFan: Healthy snack
1/16/23, 3:02 AM - ARealAVFan: Super healthy and Baby loves them
1/16/23, 0:14 AM - ARealAVFan: good taste, baby love it
1/16/23, 11:58 AM - ARealAVFan: My son does not like it...
1/16/23, 9:51 AM - ARealAVFan: Great in a pinch...portable, healthy
1/16/23, 9:05 AM - ARealAVFan: Yummy healthy snack we love
1/16/23, 8:42 AM - ARealAVFan: Yummy!
1/16/23, 5:55 AM - ARealAVFan: Tastes good, lots of crumbs
1/16/23, 5:02 AM - ARealAVFan: Fantastic
1/16/23, 4:39 AM - ARealAVFan: my son LOVES these
1/16/23, 4:24 AM - ARealAVFan: great snacks
1/16/23, 5:05 AM - ARealAVFan: Crush very easily (dust everywhere!) and they don't taste as good as Gerber
1/16/23, 7:39 AM - ARealAVFan: Why I received only one?
1/15/23, 10:37 PM - ARealAVFan: Very tasty - just the right amount of salt and fresh flavor!
1/15/23, 7:37 PM - ARealAVFan: Great invention, tasty, healthy
1/16/23, 2:15 AM - ARealAVFan: Not impressed
1/15/23, 10:17 PM - ARealAVFan: Tasty and convenient!
1/15/23, 8:16 PM - ARealAVFan: Great idea! Yummy product!
1/16/23, 7:03 AM - ARealAVFan: Plum is the best!
1/16/23, 3:40 AM - ARealAVFan: Love it
1/16/23, 1:53 AM - ARealAVFan: Great for traveling or throwing in your diaper bag
1/16/23, 1:09 AM - ARealAVFan: Would buy again
1/16/23, 1:09 AM - ARealAVFan: Yum-Yum MishMash
1/16/23, 0:48 AM - ARealAVFan: what an awesome idea!
1/16/23, 0:47 AM - ARealAVFan: YUMMY and my son loves them!
1/16/23, 0:34 AM - ARealAVFan: Great for adults, too!
1/16/23, 0:21 AM - ARealAVFan: Great tasting Plum Tot
1/15/23, 11:58 PM - ARealAVFan: My 7 month old daughter and 18month old twin niece and nephew love these
1/15/23, 9:05 PM - ARealAVFan: great product/brilliant packaging!
1/15/23, 11:48 PM - ARealAVFan: Glorified baby food
1/16/23, 4:29 AM - ARealAVFan: Miam-Miam!!
1/16/23, 0:53 AM - ARealAVFan: goji cacao & maca yuck
1/16/23, 6:37 AM - ARealAVFan: These are amazing.
1/14/23, 9:33 PM - ARealAVFan: Half-empty cans and greasy inconsistent ingredients
1/14/23, 7:06 PM - ARealAVFan: unfilled cans
1/16/23, 1:37 AM - ARealAVFan: Please Think Twice...
1/14/23, 8:32 AM - ARealAVFan: Great
1/16/23, 8:26 AM - ARealAVFan: My dog love this!
1/14/23, 3:28 AM - ARealAVFan: We Love Grammy's!
1/16/23, 10:52 AM - ARealAVFan: my rat terriers love this stuff
1/14/23, 6:54 PM - ARealAVFan: MORE THAN A DOZEN STARS
1/16/23, 2:25 PM - ARealAVFan: Gets my picky dog eating...
1/15/23, 9:23 PM - ARealAVFan: More Grammy Pot Pie Please!!
1/15/23, 5:42 AM - ARealAVFan: Was surprised with the layer of fat on top of contents.
1/16/23, 0:54 AM - ARealAVFan: My Dog Loves This Food
1/16/23, 9:28 AM - ARealAVFan: CAUTION/DENTED CANS
1/14/23, 3:51 PM - ARealAVFan: Grammy's Pot Pie for Dogs - Dogs Love It!
1/16/23, 1:55 PM - ARealAVFan: 100 Calories BUT...
1/16/23, 5:34 AM - ARealAVFan: Great tea.
1/15/23, 11:28 PM - ARealAVFan: Tastes very good!!!
1/15/23, 8:51 PM - ARealAVFan: Wu-yi is
1/15/23, 4:17 PM - ARealAVFan: Fine Quality Tea!
1/15/23, 6:05 PM - ARealAVFan: Found at the dollar store
1/16/23, 6:41 AM - ARealAVFan: Not the same tea...
1/16/23, 0:57 AM - ARealAVFan: Nice flavor, great value!
1/15/23, 10:32 PM - ARealAVFan: Great oolong for the price
1/16/23, 7:16 AM - ARealAVFan: love this tea!
1/16/23, 7:12 AM - ARealAVFan: quality tea
1/16/23, 4:10 AM - ARealAVFan: ...eh
1/15/23, 3:48 PM - ARealAVFan: Tea is okay... teabag isn't.
1/16/23, 0:04 AM - ARealAVFan: Good 'ol Dubble Bubble Taste! :-)
1/14/23, 0:50 AM - ARealAVFan: Tasty but...
1/14/23, 0:31 AM - ARealAVFan: Satay Noodles
1/14/23, 0:24 AM - ARealAVFan: Too oily and lacks flavor
1/14/23, 0:15 AM - ARealAVFan: tatsy!
1/14/23, 9:54 AM - ARealAVFan: Really Good
1/16/23, 6:38 AM - ARealAVFan: pretty good stuff
1/16/23, 6:18 AM - ARealAVFan: Flavorless Sludge
1/15/23, 4:23 PM - ARealAVFan: Surprisingly Flavorful, But Dine With A Friend
1/15/23, 11:31 AM - ARealAVFan: Not Real Peanut Satay
1/16/23, 2:03 PM - ARealAVFan: Mild Taste, But Delicious.
1/15/23, 8:51 PM - ARealAVFan: Excellent taste
1/15/23, 9:24 AM - ARealAVFan: Wonderful condiment
1/15/23, 1:43 AM - Mary A. Parham: Exotic Pantry Stuff - Pomegranate Molasses
1/15/23, 4:22 PM - Mary A. Parham: satisfied
1/14/23, 5:57 PM - Mary A. Parham: Great Find!
1/15/23, 5:45 AM - Mary A. Parham: I would recommend this product.
1/16/23, 9:24 AM - Mary A. Parham: Love it! I use it for so many things including my mother's secret recipe
1/16/23, 8:12 AM - Mary A. Parham: Don't use this in place of regular molasses!
1/14/23, 11:08 PM - Mary A. Parham: Excellent by itself or in hummus/baba ganoush
1/15/23, 6:43 AM - Mary A. Parham: Krinos Tahini
1/15/23, 8:16 AM - Mary A. Parham: Best Tahini I have ever had. And we buy a lot of it.
1/16/23, 7:52 AM - Mary A. Parham: Best Tahini I've had!
1/16/23, 1:32 PM - Mary A. Parham: Good hummus as a result!
1/15/23, 9:08 PM - Mary A. Parham: Bitter
1/14/23, 11:55 PM - Mary A. Parham: Nice!
1/15/23, 8:51 PM - Mary A. Parham: It's A Boy Bubble Gum
1/16/23, 9:53 AM - Mary A. Parham: Buble Gun Cigars......real cigars might have tasted better
1/16/23, 9:48 AM - Mary A. Parham: stale cigars
1/15/23, 2:31 AM - Mary A. Parham: Great Announcement for Non-smokers
1/15/23, 6:10 PM - Mary A. Parham: Fun for our daughter
1/15/23, 1:52 PM - Mary A. Parham: Everything Iv'e ordered so far.
1/16/23, 2:13 AM - Mary A. Parham: Best value for the genuine article IF you have PRIME
1/16/23, 2:44 AM - Mary A. Parham: CHEAP IMITATION - DO NOT BUY
1/16/23, 6:05 AM - Mary A. Parham: False advertising!
1/16/23, 5:26 AM - Mary A. Parham: False advertising!
1/15/23, 2:44 PM - Mary A. Parham: Great Product, Awful Price
1/16/23, 1:58 AM - Mary A. Parham: You don't get what you order
1/16/23, 2:47 AM - Mary A. Parham: Different product than the photo
1/16/23, 1:01 AM - Mary A. Parham: All 12 cans were terribly banged up and dented!
1/16/23, 4:23 AM - Mary A. Parham: False and misleading product data, but they do taste good
1/16/23, 2:09 AM - Mary A. Parham: love it except for the price
1/16/23, 5:19 AM - Mary A. Parham: BEWARE--NOT D.O.P. certified
1/16/23, 1:26 PM - Mary A. Parham: NOT DOP Certified! But Organic!
1/16/23, 11:35 AM - Mary A. Parham: Not DOP
1/16/23, 9:24 AM - Mary A. Parham: CENTO SAN MARZANO
1/16/23, 8:02 AM - Mary A. Parham: The best
1/16/23, 7:43 AM - Mary A. Parham: The picture shows dop and they are not
1/16/23, 7:40 AM - Mary A. Parham: damaged cans
1/16/23, 7:27 AM - Mary A. Parham: D.O.P? Not really....
1/16/23, 7:20 AM - Mary A. Parham: GREAT ITALIAN
1/16/23, 5:12 AM - Mary A. Parham: a little disappointing
1/15/23, 9:17 PM - Mary A. Parham: Cento  Time
1/16/23, 2:51 AM - Mary A. Parham: Damaged merchandise
1/15/23, 11:21 PM - Mary A. Parham: dented can
1/15/23, 11:49 PM - Mary A. Parham: Too Expensive
1/16/23, 1:19 AM - Mary A. Parham: Not sure what I got
1/15/23, 11:52 PM - Mary A. Parham: Dented cans
1/16/23, 0:47 AM - Mary A. Parham: Squism needs help!
1/16/23, 9:51 AM - Mary A. Parham: It's a shame to use so much corn syrup for babies!
1/16/23, 8:38 AM - Mary A. Parham: FIRST INGREDIENT IS CORN SYRUP!!!
1/16/23, 2:03 AM - Mary A. Parham: Very useful with true Lactose Intolerance.  Be aware, this is mostly sugar, NOT made from milk.
1/15/23, 10:43 PM - Mary A. Parham: Reduced spit-up and a happier baby!
1/16/23, 9:53 AM - Mary A. Parham: This formula is terrible!
1/16/23, 0:40 AM - Mary A. Parham: Similac Sensitive
1/15/23, 11:54 AM - Mary A. Parham: Solves Colic Within One Day - But It's Corn Syrup-Based
1/16/23, 2:08 AM - Mary A. Parham: Costco B&M has it for $0.81/fl oz!!! Way cheaper.
1/16/23, 7:36 AM - Mary A. Parham: Worked well but had added sugar
1/15/23, 6:14 PM - Mary A. Parham: Great For Cakes
1/15/23, 10:17 PM - Mary A. Parham: Don't buy this product unless you are looking for shredded coconut
1/16/23, 7:24 AM - Mary A. Parham: Little Flavor
1/15/23, 3:30 PM - Mary A. Parham: Excellent service from vendor!!!
1/16/23, 6:00 AM - Mary A. Parham: Disappointing
1/16/23, 10:03 AM - Mary A. Parham: Great little conversation piece.
1/16/23, 8:42 AM - Mary A. Parham: Dispenser too small
1/15/23, 6:23 PM - Mary A. Parham: Por Kwan Chilli Paste w/ Sweet Basil Leaves Hits the Spot in Vegetarian Dishes
1/15/23, 5:51 PM - Mary A. Parham: Great to keep on hand for desserts!
1/16/23, 2:38 PM - Mary A. Parham: Good for cravings
1/16/23, 8:52 AM - Mary A. Parham: A wonderful dessert
1/16/23, 8:16 AM - Mary A. Parham: Excellent base mix
1/14/23, 8:08 PM - Mary A. Parham: pudding
1/16/23, 2:03 AM - Mary A. Parham: woof woof
1/15/23, 9:23 PM - Mary A. Parham: Good stuff.
1/16/23, 7:43 AM - Mary A. Parham: Dogs Love it!
1/16/23, 8:29 AM - Mary A. Parham: Wonderful fudge
1/15/23, 10:35 AM - Mary A. Parham: Extraordinary!
1/16/23, 2:58 PM - Mary A. Parham: Amazing! Worth every penny!
1/16/23, 2:42 PM - Mary A. Parham: Amazing Tea - My Favorite
1/16/23, 11:57 AM - Mary A. Parham: Delicious tea!
1/16/23, 11:39 AM - Mary A. Parham: Totally delicious
1/16/23, 11:26 AM - Mary A. Parham: Delicious tea with a great aftertaste
1/16/23, 10:20 AM - Mary A. Parham: Love it.
1/16/23, 10:12 AM - Mary A. Parham: Favorite Tea
1/16/23, 8:57 AM - Mary A. Parham: Great Spicy taste with hint of sweet
1/16/23, 8:49 AM - Mary A. Parham: Most delicious tea
1/16/23, 7:20 AM - Mary A. Parham: Excellent!
1/16/23, 0:56 AM - Mary A. Parham: Excellent tea
1/16/23, 0:25 AM - Mary A. Parham: A beautiful experience
1/15/23, 5:22 PM - Mary A. Parham: Just Mmmmmmmmmm
1/16/23, 2:28 PM - Mary A. Parham: Taste good
1/16/23, 1:55 PM - Mary A. Parham: Watch out for the FAT!
1/16/23, 2:16 PM - Mary A. Parham: Top quality Salsa
1/15/23, 11:11 PM - Mary A. Parham: The best healthy muffin
1/15/23, 10:19 PM - Mary A. Parham: Delicious, nutrient-packed, fast--
1/15/23, 7:32 PM - Mary A. Parham: The Muffin Tops Are Better
1/15/23, 7:20 PM - Mary A. Parham: Not a corn muffin for a Cornhusker
1/16/23, 11:16 AM - Mary A. Parham: spray mix
1/15/23, 9:43 PM - Mary A. Parham: its not what im used to...but hey its dietetic and healthy
1/16/23, 11:31 AM - Mary A. Parham: Avoid This Seloler
1/14/23, 1:13 AM - Mary A. Parham: Below standard
1/16/23, 2:29 PM - Mary A. Parham: WOW!  What a Deal!!
1/16/23, 2:19 PM - Mary A. Parham: Rishi Tea Loose Leaf Tea Bags, 100-count (Pack of 6)
1/16/23, 4:12 AM - Mary A. Parham: Rishi Tea Loose Leaf Tea Bags
1/16/23, 9:11 AM - Kat Freeman: SKIMPY for the price charged!!  Shocked!
1/16/23, 3:00 PM - Kat Freeman: Scrumptious!
1/16/23, 2:34 PM - Kat Freeman: Good Stuff
1/15/23, 8:45 AM - Kat Freeman: Charlee Bears
1/15/23, 10:03 AM - Kat Freeman: I feel good about giving these treats to my pups
1/15/23, 6:34 AM - Kat Freeman: Great low calorie treat for overweight dogs or for training treats!
1/16/23, 9:31 AM - Kat Freeman: The Best Training Treat
1/15/23, 5:31 PM - Kat Freeman: These are amazing!
1/15/23, 7:12 PM - Kat Freeman: Great Low Calorie Training Treats
1/15/23, 9:00 AM - Kat Freeman: Dog Treats
1/14/23, 1:13 AM - Kat Freeman: Below standard
1/16/23, 11:00 AM - Kat Freeman: Marathon Runner
1/16/23, 10:48 AM - Kat Freeman: Good Stuff
1/16/23, 0:07 AM - Kat Freeman: Really like it.
1/16/23, 11:03 AM - Kat Freeman: Great for running recovery
1/16/23, 1:49 PM - Kat Freeman: You bet your life!
1/16/23, 0:27 AM - Kat Freeman: Truly concentrated juice
1/16/23, 2:09 PM - Kat Freeman: Cheaper than other brands
1/16/23, 1:00 PM - Kat Freeman: Delicious tart cherry concentrate
1/16/23, 2:38 PM - Kat Freeman: Helps with sore joints and muscles
1/16/23, 0:44 AM - Kat Freeman: tart cherry concentrate
1/16/23, 0:37 AM - Kat Freeman: Excellent
1/16/23, 2:57 PM - Kat Freeman: tastes like fresh cherries
1/16/23, 0:50 AM - Kat Freeman: Does NOT Put me to sleep!!
1/14/23, 1:13 AM - Kat Freeman: Below standard
1/16/23, 2:05 AM - Kat Freeman: My favorite crackers
1/16/23, 2:47 PM - Kat Freeman: The best tasking crackers ever.
1/16/23, 2:19 PM - Kat Freeman: SKYFLAKES
1/15/23, 0:43 AM - Kat Freeman: Exactly what I ordered, plain and simple
1/15/23, 0:53 AM - Kat Freeman: Classic Candy
1/16/23, 1:46 AM - Kat Freeman: Mmm, Fresh Candy
1/16/23, 0:50 AM - Kat Freeman: Gotta love Wonka
1/15/23, 9:53 AM - Kat Freeman: great product at a great price
1/16/23, 7:36 AM - Kat Freeman: Excellent
1/16/23, 7:04 AM - Kat Freeman: Excellent
1/14/23, 6:43 PM - Kat Freeman: Chocolate Italian kisses - need I say more?
1/15/23, 11:06 PM - Kat Freeman: Incorrect packaging
1/14/23, 6:43 PM - Kat Freeman: Baci's are pure heaven - great gift, stocking stuffer!
1/15/23, 10:30 AM - Kat Freeman: Yum-o
1/15/23, 9:11 AM - Kat Freeman: What a treat
1/16/23, 6:21 AM - Kat Freeman: Great, healthy dog food for dogs with food allergies
1/16/23, 0:47 AM - Kat Freeman: Great for an allergy dog
1/16/23, 0:15 AM - Kat Freeman: I got the wrong food but dog ate it up
1/16/23, 8:41 AM - Kat Freeman: Great for Dogs that Chew their Food
1/16/23, 3:27 AM - Kat Freeman: JJA
1/15/23, 11:41 PM - Kat Freeman: Great alternative to "science diet" allegry diets
1/15/23, 11:16 PM - Kat Freeman: Best dog food--no ear infections
1/15/23, 9:43 PM - Kat Freeman: quality comes at high price
1/16/23, 1:42 PM - Kat Freeman: The best pizza I have ever had!
1/16/23, 1:12 AM - Kat Freeman: Pretty Good Dough
1/16/23, 11:19 AM - Kat Freeman: Yum!
1/16/23, 9:17 AM - Kat Freeman: Love it!
1/16/23, 11:22 AM - Kat Freeman: CHRISTMAS CANADIES
1/16/23, 7:46 AM - Kat Freeman: Love These!!
1/16/23, 7:24 AM - Kat Freeman: Great to be able to get this again
1/16/23, 9:33 AM - Kat Freeman: YUMMY Indian DHALL
1/16/23, 3:14 PM - Kat Freeman: Yellow split peas
1/15/23, 7:22 AM - Kat Freeman: No caf, but no taste, either
1/16/23, 6:01 AM - Kat Freeman: Great value
1/16/23, 7:06 AM - Kat Freeman: Happiness In A Deep Dark Cup
1/16/23, 7:29 AM - Kat Freeman: Finally! Something good from Gevalia
1/16/23, 7:20 AM - Kat Freeman: Gevalia Melange Maison Corse
1/16/23, 8:15 AM - Kat Freeman: good coffee - brews hot
1/16/23, 8:15 AM - Kat Freeman: This is THE Verona replacement
1/16/23, 7:52 AM - Kat Freeman: Great coffee, possibly the best for tassimo
1/16/23, 0:27 AM - Kat Freeman: Great coffee
1/16/23, 9:57 AM - Kat Freeman: good but pricy
1/15/23, 6:47 PM - Kat Freeman: Aunt Gussie's Pecan Meltaways
1/15/23, 5:35 PM - Kat Freeman: Absolutely loved them!!!
1/16/23, 2:24 AM - Kat Freeman: tasty, but stale (hard)
1/15/23, 7:23 PM - Kat Freeman: Good dessert for someone gluten sensitive, dairy sensitive and diabetic
1/16/23, 0:04 AM - Kat Freeman: A box of stale crumbs
1/15/23, 0:12 AM - Kat Freeman: Aunt Gussies Highfat Cookies
1/15/23, 1:35 AM - Kat Freeman: Just Great
1/15/23, 11:25 AM - Kat Freeman: Hippy Eucharist!
1/15/23, 0:12 AM - Kat Freeman: Chewy and Satisfying
1/16/23, 10:50 AM - Kat Freeman: Ehh
1/15/23, 6:01 PM - Kat Freeman: Great cookies - TERRIBLE PRICE
1/15/23, 5:44 PM - Kat Freeman: Good but not great
1/15/23, 5:16 PM - Kat Freeman: Best Healthy Cookie I've Ever Tasted!! Pretty sweet!!!!
1/16/23, 4:33 AM - Kat Freeman: Nice, Big Pieces & Big Almond Flavor
1/15/23, 11:02 PM - Kat Freeman: New Favorite Dark K-Cup
1/16/23, 1:33 AM - Kat Freeman: Oooh. I like this!
1/16/23, 0:20 AM - Kat Freeman: Great Coffee
1/16/23, 10:14 AM - Kat Freeman: Amazed
1/16/23, 3:48 AM - Kat Freeman: Yummy!
1/16/23, 4:39 AM - Kat Freeman: Caribou Coffee/Strong!
1/16/23, 9:25 AM - Kat Freeman: The Best Coffee for Depression and Lifting up Your Mood
1/16/23, 8:57 AM - Kat Freeman: Most Cozy flavor I have tried.
1/16/23, 7:26 AM - Kat Freeman: Wonderful dark coffee
1/16/23, 3:33 AM - Kat Freeman: the best k-cup
1/15/23, 11:16 PM - Kat Freeman: This is good coffee
1/16/23, 0:56 AM - Kat Freeman: Good Bold Coffee
1/16/23, 9:21 AM - Kat Freeman: nice flavor
1/16/23, 8:05 AM - Kat Freeman: Delicious
1/16/23, 2:29 AM - Kat Freeman: Wake Up Call
1/16/23, 4:00 AM - Kat Freeman: rich and delicious
1/16/23, 11:45 AM - Kat Freeman: Like it but hard to find
1/16/23, 11:34 AM - Kat Freeman: First impression: chocolate
1/16/23, 11:21 AM - Kat Freeman: Caribou Coffee, Mahogany
1/16/23, 11:09 AM - Ange: My favorite
1/16/23, 9:28 AM - Ange: Love it!
1/16/23, 8:38 AM - Ange: Smooth and tasty and an absolute dream come true for those who enjoy bold dark roasts...
1/16/23, 6:47 AM - Ange: Not like fresh but gettin better!
1/16/23, 3:10 PM - Ange: Caribou Mahogany
1/16/23, 3:10 PM - Ange: down to almost none ....
1/16/23, 2:57 PM - Ange: Coffee is good; name is good....
1/16/23, 2:51 PM - Ange: burnt toast
1/16/23, 2:24 PM - Ange: Love Caribou!
1/16/23, 1:40 PM - Ange: yum
1/16/23, 0:43 AM - Ange: great coffee
1/16/23, 0:37 AM - Ange: Great tasting coffee
1/16/23, 0:31 AM - Ange: Best Caribou
1/16/23, 0:20 AM - Ange: Great coffee
1/16/23, 0:12 AM - Ange: Yummy coffee
1/16/23, 0:02 AM - Ange: Excellent coffee!
1/16/23, 11:25 AM - Ange: Great coffee
1/16/23, 11:21 AM - Ange: Fantastic Stuff !!!
1/16/23, 11:06 AM - Ange: Great Coffee!
1/16/23, 11:00 AM - Ange: Nice smooth flavor - but not strong enough for me
1/16/23, 10:56 AM - Ange: Best K-Cup to Date
1/16/23, 10:52 AM - Ange: Caibou mahogany-k-cup
1/16/23, 10:35 AM - Ange: Excellent presence, not too smokey, smooth finish.
1/16/23, 10:17 AM - Ange: Best overall coffee
1/16/23, 9:08 AM - Ange: MY FAVE
1/16/23, 9:02 AM - Ange: Bold K-cups coffee
1/16/23, 9:00 AM - Ange: coffee lovers
1/16/23, 8:35 AM - Ange: We love this coffee.
1/16/23, 8:16 AM - Ange: A bit too strong for me
1/16/23, 8:09 AM - Ange: not my cup of coffee
1/16/23, 7:39 AM - Ange: Nice balanced taste
1/16/23, 7:37 AM - Ange: Great taste. Not bitter.
1/16/23, 7:36 AM - Ange: caribou
1/16/23, 6:59 AM - Ange: Mahogany k cups
1/16/23, 5:45 AM - Ange: Lives up to its appealing name
1/16/23, 5:32 AM - Ange: Yum
1/16/23, 3:24 AM - Ange: Great simple coffee
1/16/23, 2:38 AM - Ange: I love Caribou Mahogany!
1/16/23, 2:19 AM - Ange: Mellow, full bodied
1/16/23, 2:16 AM - Ange: SMOOOOTH!
1/16/23, 2:11 AM - Ange: Best K-cup out there.
1/16/23, 1:53 AM - Ange: Really excellent
1/16/23, 1:33 AM - Ange: Caribou Coffee's Mahogany Review
1/16/23, 6:27 AM - Ange: Good coffee
1/16/23, 10:52 AM - Ange: Disapointed
1/16/23, 8:42 AM - Ange: Full bodied but bitter
1/16/23, 7:48 AM - Ange: Best coffee
1/16/23, 7:37 AM - Ange: Best coffee ever
1/16/23, 6:07 AM - Ange: Smooth But Flat
1/16/23, 0:07 AM - Ange: Didn't like it
1/15/23, 4:17 PM - Ange: Sweet but not too sweet!
1/16/23, 5:48 AM - Ange: O.N.E. Coconut Water with a Splash of Pineapple
1/16/23, 3:28 AM - Ange: If you're looking for something a little more "Pina Colada" this is it
1/16/23, 3:04 PM - Ange: BEWARE...INGREDIENTS HAVE CHANGED
1/16/23, 3:00 PM - Ange: New formulation for 10/2012 is not good at all!
1/16/23, 4:58 AM - Ange: Delicious and refreshing
1/16/23, 4:45 AM - Ange: LOVE THIS STUFF
1/16/23, 4:32 AM - Ange: great taste, not too sweet, very refreshing.
1/16/23, 3:47 AM - Ange: O.N.E. Coconut Water!
1/15/23, 11:58 PM - Ange: Very tasty
1/15/23, 6:44 PM - Ange: THE BEST drink on earth!!!!!!!
1/15/23, 6:24 PM - Ange: Not a sports drink
1/15/23, 3:57 PM - Ange: Amazing (even if it is trendy)
1/15/23, 3:57 PM - Ange: Good Taste but Not for Everyone
1/15/23, 8:45 PM - Ange: why add sugar?
1/15/23, 5:51 PM - Ange: Coconut Water
1/15/23, 3:17 PM - Ange: Lots of flavor, but not too sweet
1/16/23, 2:42 PM - Ange: Terrible flavor
1/16/23, 0:57 AM - Ange: This stuff is delicious
1/16/23, 5:54 AM - Ange: Really a GOOD product!
1/16/23, 5:45 AM - Ange: Best ever!
1/16/23, 1:03 AM - Ange: Definitely Pineapple
1/15/23, 8:08 PM - Ange: Coconut Water w/a Splash of Pineapple
1/15/23, 2:26 PM - Ange: Plain is better
1/16/23, 3:23 AM - Ange: Bleh... cane juice is 3rd on ingred. list.
1/15/23, 3:47 PM - Ange: Maybe I just don't "get it" ...
1/15/23, 3:15 PM - Ange: If You REALLY Like Sweet...
1/15/23, 3:14 PM - Ange: Tasty.
1/16/23, 0:48 AM - Ange: Smaller-than-usual package size, overly-sweet taste
1/15/23, 3:17 PM - Ange: Not what I expected!  Interesting taste
1/15/23, 8:42 PM - Ange: Not as healthy as you would think
1/15/23, 8:09 PM - Ange: Just didn't taste good to me
1/15/23, 3:17 PM - Ange: Bland
1/15/23, 3:15 PM - Ange: Needs a bigger splash
1/15/23, 3:17 PM - Ange: Pineapple flavored coconut water from Indonesia... there's something we really need!
1/16/23, 2:55 PM - Ange: The prime rib of beef jerky!
1/15/23, 0:33 AM - Ange: Healthy Alternative to Kibble, Canned or Raw Diets
1/15/23, 10:00 AM - Ange: This food is not unbalanced.
1/15/23, 3:25 PM - Ange: Great food
1/16/23, 0:02 AM - Ange: GREAT food
1/15/23, 6:44 PM - Ange: Great product if you are willing to do the work
1/16/23, 9:36 AM - Ange: Otto likes it!
1/16/23, 6:12 AM - Ange: picky puppy...
1/16/23, 11:58 AM - Ange: Sojos original
1/14/23, 11:31 AM - Ange: Caution - poorly balanced nutrition!
1/16/23, 2:45 PM - Ange: My Dogs are Wild About These Treats!
1/16/23, 4:07 AM - Ange: IT'S OK FOR SOMETHING DIFFERENT
1/15/23, 10:52 PM - Ange: Decent Light Roast Organic
1/15/23, 4:35 PM - Ange: Just like the restaurant!
1/15/23, 5:36 PM - Ange: Authentic taste, easy to prepare!
1/16/23, 2:08 PM - Jo-ann Albano "Jodelpa3": Good value, good taste
1/15/23, 7:43 PM - Jo-ann Albano "Jodelpa3": theres better curry paste out there
1/16/23, 11:51 AM - Jo-ann Albano "Jodelpa3": Diet Peach  Snapple Delivered Safely & Quickly
1/15/23, 10:03 AM - Jo-ann Albano "Jodelpa3": "Yep--it's a diet !!!"
1/16/23, 0:07 AM - Jo-ann Albano "Jodelpa3": Good quality for a good price.
1/15/23, 10:00 AM - Jo-ann Albano "Jodelpa3": good stuff!
1/15/23, 8:11 AM - Jo-ann Albano "Jodelpa3": Highest in protein
1/14/23, 10:52 AM - Jo-ann Albano "Jodelpa3": Yummy
1/14/23, 4:56 PM - Jo-ann Albano "Jodelpa3": Mrs. May's Pumpkin Crunch  is terrific
1/14/23, 4:56 PM - Jo-ann Albano "Jodelpa3": Tasty and Light
1/14/23, 3:44 PM - Jo-ann Albano "Jodelpa3": good snack for everyone
1/16/23, 10:07 AM - Jo-ann Albano "Jodelpa3": I Want More!
1/16/23, 9:51 AM - Jo-ann Albano "Jodelpa3": Addictive
1/16/23, 0:18 AM - Jo-ann Albano "Jodelpa3": yum
1/16/23, 11:19 AM - Jo-ann Albano "Jodelpa3": Tasty
1/16/23, 1:29 PM - Jo-ann Albano "Jodelpa3": goody good
1/15/23, 9:10 AM - Jo-ann Albano "Jodelpa3": Combo Rose Food/Systemic Insecticide
1/15/23, 0:00 AM - Jo-ann Albano "Jodelpa3": Easy Rose Care and great product
1/14/23, 4:37 PM - Jo-ann Albano "Jodelpa3": Excellent Product
1/16/23, 3:47 AM - Jo-ann Albano "Jodelpa3": Misleading product!!! If you want no bees, then use it.
1/16/23, 0:28 AM - Jo-ann Albano "Jodelpa3": Good for the leaves not for the Flowers
1/16/23, 11:31 AM - Jo-ann Albano "Jodelpa3": A Must for the Gardener
1/16/23, 2:16 AM - Jo-ann Albano "Jodelpa3": Avoid like the plague---contains product killing honeybees
1/16/23, 3:51 AM - Jo-ann Albano "Jodelpa3": Fisher Pecan Chips
1/15/23, 11:35 PM - Jo-ann Albano "Jodelpa3": hot mustard
1/15/23, 8:24 PM - Jo-ann Albano "Jodelpa3": Thomy Mustard Maniac
1/15/23, 11:16 PM - Jo-ann Albano "Jodelpa3": Thomy Scharfer Senf
1/15/23, 11:11 PM - Jo-ann Albano "Jodelpa3": Ummm Ummm Good...
1/16/23, 3:08 PM - Jo-ann Albano "Jodelpa3": Best. Mustard. Ever.
1/16/23, 10:09 AM - Jo-ann Albano "Jodelpa3": Hot
1/15/23, 10:59 PM - Jo-ann Albano "Jodelpa3": Super mustard
1/14/23, 9:38 AM - Jo-ann Albano "Jodelpa3": Wonderful!
1/14/23, 2:54 PM - Jo-ann Albano "Jodelpa3": Delicious low cal treat
1/15/23, 10:56 AM - Jo-ann Albano "Jodelpa3": Awesome fresh tasting Lobster Soup. Perfect just out of can, heat an serve.
1/15/23, 3:17 PM - Jo-ann Albano "Jodelpa3": Tastes ok but has bits of shells
1/15/23, 1:53 PM - Jo-ann Albano "Jodelpa3": Unlisted ingredient of Baxter Lobster Bisque
1/15/23, 7:01 AM - Jo-ann Albano "Jodelpa3": Too watery
1/14/23, 9:28 PM - Jo-ann Albano "Jodelpa3": Baxter's canned soups rule!
1/14/23, 10:56 AM - Jo-ann Albano "Jodelpa3": It's good for canned soup.
1/15/23, 1:45 AM - Jo-ann Albano "Jodelpa3": Disgusting, nasty, inedible
1/14/23, 10:39 PM - Jo-ann Albano "Jodelpa3": Pretty Good
1/16/23, 2:25 PM - Jo-ann Albano "Jodelpa3": ugh
1/16/23, 4:59 AM - Jo-ann Albano "Jodelpa3": I've had worse but I've had better too.
1/15/23, 7:09 PM - Jo-ann Albano "Jodelpa3": As far as canned soups go
1/15/23, 3:40 PM - Jo-ann Albano "Jodelpa3": Bad tasting soup
1/14/23, 1:27 PM - Jo-ann Albano "Jodelpa3": Lobster Tomalley=health risk
1/14/23, 11:12 AM - Jo-ann Albano "Jodelpa3": Lovely seeds for your cereal, baking or yogurt
1/14/23, 8:58 PM - Jo-ann Albano "Jodelpa3": The best flaxseeds I've ever had
1/14/23, 3:54 PM - Jo-ann Albano "Jodelpa3": Fiber packed and nutrient rich
1/14/23, 11:12 PM - Jo-ann Albano "Jodelpa3": Great source for omega3's!
1/15/23, 0:05 AM - Jo-ann Albano "Jodelpa3": Organic Golden i
1/15/23, 3:07 AM - Jo-ann Albano "Jodelpa3": Good product
1/15/23, 1:58 AM - Jo-ann Albano "Jodelpa3": Great on Conflakes
1/14/23, 11:24 PM - Jo-ann Albano "Jodelpa3": good in almost anything
1/14/23, 11:03 PM - Jo-ann Albano "Jodelpa3": So good for you!!
1/16/23, 5:25 AM - Jo-ann Albano "Jodelpa3": Healthy Goodness
1/16/23, 3:10 AM - Jo-ann Albano "Jodelpa3": Great stuff
1/15/23, 0:53 AM - Jo-ann Albano "Jodelpa3": Very happy with this purchase!
1/15/23, 4:01 AM - Jo-ann Albano "Jodelpa3": Great Flaxseed and Delivery Service
1/15/23, 2:38 AM - Jo-ann Albano "Jodelpa3": Very healthy!
1/16/23, 0:46 AM - Jo-ann Albano "Jodelpa3": It would be a 5 if it weren't for the rocks.
1/16/23, 0:08 AM - Jo-ann Albano "Jodelpa3": red mill did it again
1/16/23, 10:59 AM - Jo-ann Albano "Jodelpa3": They're Good Seeds.
1/16/23, 8:21 AM - Jo-ann Albano "Jodelpa3": good seeds but gravel bits
1/16/23, 3:53 AM - Jo-ann Albano "Jodelpa3": A must have for healthy life
1/15/23, 11:11 PM - Jo-ann Albano "Jodelpa3": good stuff
1/15/23, 6:47 PM - Jo-ann Albano "Jodelpa3": Excellent Quality!
1/15/23, 6:23 PM - Jo-ann Albano "Jodelpa3": Bob's Red Mill Organic Golden Flaxseed
1/15/23, 4:37 AM - Jo-ann Albano "Jodelpa3": a little expensive
1/15/23, 4:55 PM - Jo-ann Albano "Jodelpa3": flax seed, recommended brand
1/14/23, 9:14 PM - Jo-ann Albano "Jodelpa3": the product itself is fine...
1/14/23, 5:44 PM - Jo-ann Albano "Jodelpa3": It's bird seed.
1/15/23, 10:20 AM - Jo-ann Albano "Jodelpa3": Tastes great but pkg says "Made in China" so I won't buy it again
1/15/23, 0:47 AM - Jo-ann Albano "Jodelpa3": "Health food" from China? Doubtful
1/14/23, 8:41 AM - Jo-ann Albano "Jodelpa3": Delicious
1/14/23, 8:51 AM - Jo-ann Albano "Jodelpa3": Great Taste without High Fructose Corn Syrup!
1/15/23, 3:21 PM - Jo-ann Albano "Jodelpa3": What is the carbon footprint of this product?
1/14/23, 1:07 PM - Jo-ann Albano "Jodelpa3": Fantastic!
1/16/23, 5:52 AM - Jo-ann Albano "Jodelpa3": Product not made in China!
1/14/23, 2:44 PM - Jo-ann Albano "Jodelpa3": The Best of the Best nut cluster snacks I've ever had
1/14/23, 10:58 AM - Jo-ann Albano "Jodelpa3": Mrs. Mays almond crunch
1/14/23, 4:06 PM - Jo-ann Albano "Jodelpa3": But quality seems to be slipping
1/14/23, 0:50 AM - Jo-ann Albano "Jodelpa3": DELICIOUS!
1/14/23, 0:34 AM - Jo-ann Albano "Jodelpa3": Sweet & nutty
1/15/23, 6:48 AM - Jo-ann Albano "Jodelpa3": Made in China, but I still enjoy it
1/16/23, 11:16 AM - Jo-ann Albano "Jodelpa3": Made in China?!
1/16/23, 8:25 AM - Jo-ann Albano "Jodelpa3": great snack
1/14/23, 3:53 PM - Jo-ann Albano "Jodelpa3": Mrs Mays Anonymous
1/14/23, 3:28 PM - Jo-ann Albano "Jodelpa3": Love Mrs. May's Products
1/14/23, 2:13 PM - Jo-ann Albano "Jodelpa3": Delicious, addictive and healthy too!
1/14/23, 1:43 PM - Jo-ann Albano "Jodelpa3": Delicious healthy snack
1/14/23, 1:04 PM - Jo-ann Albano "Jodelpa3": They're So Good They Evaporate
1/15/23, 4:09 AM - Jo-ann Albano "Jodelpa3": This product is made in China
1/14/23, 9:43 PM - Jo-ann Albano "Jodelpa3": Love the nut!!
1/14/23, 4:16 PM - Jo-ann Albano "Jodelpa3": Great Almond Crunch!!
1/16/23, 2:49 AM - Jo-ann Albano "Jodelpa3": Great taste - but honestly what goes inside ?  read on ...
1/15/23, 10:59 AM - Jo-ann Albano "Jodelpa3": quality
1/15/23, 9:14 AM - Jo-ann Albano "Jodelpa3": Mrs. May's Almonds make my days!
1/16/23, 2:32 PM - Jo-ann Albano "Jodelpa3": lacey
1/16/23, 9:11 AM - Jo-ann Albano "Jodelpa3": Best flavor!
1/15/23, 10:14 PM - LC: Perfect gift with a touch of the Southwest
1/16/23, 9:47 AM - LC: It is okay
1/16/23, 4:58 AM - LC: Italy's best pasta and its organic
1/15/23, 0:51 AM - LC: Noticablely tastey!
1/16/23, 2:18 PM - LC: Wow. Excellent.
1/16/23, 11:28 AM - LC: Tastes just like it was home made.
1/16/23, 2:36 PM - LC: Good
1/15/23, 9:18 AM - LC: What can you say, there chiclets
1/16/23, 8:16 AM - LC: Chiclets--Fond memories and a taste of the past--fresh as new!
1/15/23, 1:10 AM - LC: Finally, an affordable, delicious green tea powder
1/15/23, 3:43 AM - LC: great alternative to bottled green tea
1/15/23, 4:19 AM - LC: nice substitute for soda or sugary tea
1/15/23, 1:52 AM - LC: Flavorful and refreshing
1/15/23, 0:44 AM - LC: Very Reasonably Priced and Delicious
1/16/23, 1:16 AM - LC: lots of uses for this green tea...
1/15/23, 7:39 PM - LC: Crushed up leaves!
1/15/23, 8:41 AM - LC: My Experience
1/15/23, 7:12 AM - LC: VERY CONVIENENT!
1/16/23, 2:42 AM - LC: Handy but not to tasty
1/16/23, 1:48 AM - LC: Stash Instant Green Tea
1/16/23, 5:25 AM - LC: Stash Premium Mint Green Iced Tea Powder
1/16/23, 3:31 AM - LC: No Flavor - Not Authentic
1/15/23, 9:47 PM - LC: Good tea
1/15/23, 9:27 PM - LC: Stash Green Tea Powder
1/15/23, 7:32 PM - LC: Love it!
1/15/23, 7:32 PM - LC: For ginger fans
1/15/23, 4:49 PM - LC: Great for on the go!  Makes water a little less boring!
1/15/23, 2:58 AM - LC: Great health benefits
1/15/23, 1:32 AM - LC: Good for on the go
1/16/23, 5:06 AM - LC: Good tea taste, not sweet
1/16/23, 4:49 AM - LC: Tastes GREAT!!
1/16/23, 4:45 AM - LC: Way too weak for my tastes
1/16/23, 3:56 AM - LC: Mild taste, easy to mix, will buy again
1/15/23, 11:32 PM - LC: Trying this product for the first time
1/15/23, 6:28 AM - LC: got me off the diet soda
1/15/23, 2:41 AM - LC: Nice Green Iced Tea Beverage
1/15/23, 2:35 AM - LC: YUM....Yum, Yum!!!!
1/16/23, 4:45 AM - LC: Way too weak for my tastes
1/15/23, 2:24 PM - LC: Mom of 5
1/16/23, 2:31 PM - LC: Best Instant Green Tea Ever
1/16/23, 2:06 PM - LC: Not for Me
1/16/23, 0:21 AM - LC: ice tea
1/16/23, 11:13 AM - LC: Great tea
1/16/23, 9:33 AM - LC: Great tasting and easy to use
1/16/23, 6:37 AM - LC: Perfect summer tea
1/16/23, 6:12 AM - LC: Just had a glass today
1/16/23, 5:25 AM - LC: Doesn't have taste...
1/16/23, 4:45 AM - LC: Of al the Stash iced teas this is the best, and it is still not all that good
1/16/23, 4:45 AM - LC: way too weak for my tastes
1/16/23, 4:45 AM - LC: Awful
1/16/23, 4:14 AM - LC: Makes great drinks but you have to use a lot!
1/16/23, 3:31 AM - LC: Not bad.  A bit light.
1/16/23, 2:47 AM - LC: Great product!
1/16/23, 1:29 AM - LC: First time purchaser!
1/16/23, 1:16 AM - LC: quality lightly sweetened green tea powder
1/16/23, 0:33 AM - LC: not too sweet, not too strong, just right
1/15/23, 10:53 PM - LC: Great pick me up on the go - hot or cold!
1/15/23, 9:47 PM - LC: Good stuff
1/15/23, 9:02 PM - LC: Wonderfully refreshing drink
1/15/23, 8:15 PM - LC: Easy and tasty for better health
1/15/23, 7:39 PM - LC: Very refreshing!
1/15/23, 6:17 PM - LC: Love it!
1/15/23, 6:15 PM - LC: Refreshing addition to water
1/15/23, 6:12 PM - LC: Powdered Green Tea by Stash
1/15/23, 8:22 AM - LC: Refreshing flavor
1/15/23, 8:05 AM - LC: Just as expected
1/15/23, 3:21 AM - LC: Great taste and convenient
1/15/23, 2:48 AM - LC: Tea
1/15/23, 1:52 AM - LC: Refreshing summer beverage
1/16/23, 6:30 AM - LC: waste of money
1/15/23, 4:19 PM - LC: Great product - at last!
1/15/23, 2:32 PM - LC: Lightly sweet and cheeper than an Jamba Juice Matcha Shot!
1/15/23, 0:33 AM - LC: Terrible
1/16/23, 1:52 PM - LC: Beware, if you have a corn allergy!!
1/16/23, 0:46 AM - LC: lightly sweetened green iced tea powder
1/16/23, 11:57 AM - LC: Great Product
1/16/23, 4:52 AM - LC: Not So Much!
1/16/23, 11:41 AM - LC: Pretty good stuff, with the right sweetener
1/16/23, 0:48 AM - LC: Don't bother
1/16/23, 0:48 AM - LC: Not worth it!
1/16/23, 0:47 AM - LC: I wouldn't bother.
1/15/23, 8:22 AM - LC: powdered tea
1/15/23, 2:16 AM - LC: mona lisa
1/15/23, 6:01 PM - LC: stash tea powder review
1/15/23, 1:24 AM - LC: The mint tea I bought
1/15/23, 10:53 AM - LC: Real Rose petals and all  the delicious flavor!
1/16/23, 0:33 AM - LC: eliminate the "natural flavor" additive
1/15/23, 7:26 PM - LC: I hope I just got a bad batch
1/16/23, 1:06 AM - LC: Not Too "Rosey"
1/15/23, 3:36 PM - LC: rosematic
1/16/23, 4:20 AM - LC: NO MORE PEPSI FOR ME!!
1/15/23, 11:02 PM - LC: pleased
1/15/23, 8:38 PM - LC: Perfect!
1/15/23, 7:45 PM - LC: Davidson's Rose Congou Leaf Tea
1/15/23, 6:12 PM - LC: Lovely Tea
1/15/23, 4:45 AM - LC: Yum.
1/15/23, 5:38 PM - LC: Adzuki beans
1/15/23, 7:12 AM - LC: yummy
1/15/23, 9:56 PM - LC: beans
1/16/23, 2:41 PM - LC: Works for me!
1/16/23, 2:13 PM - S. Petersen "budget mama": decent but Monin is better...
1/16/23, 10:00 AM - S. Petersen "budget mama": Don't waste your money
1/16/23, 2:34 AM - S. Petersen "budget mama": Koala Crisps rock!
1/14/23, 9:21 PM - S. Petersen "budget mama": Lemonylicious
1/15/23, 2:35 PM - S. Petersen "budget mama": the best ever
1/16/23, 1:58 PM - S. Petersen "budget mama": Easy Summer dessert
1/14/23, 1:19 PM - S. Petersen "budget mama": A Caveat
1/14/23, 7:52 AM - S. Petersen "budget mama": Great Popcorn
1/14/23, 1:13 PM - S. Petersen "budget mama": Keep poppin!
1/13/23, 7:59 PM - S. Petersen "budget mama": Tender
1/14/23, 0:54 AM - S. Petersen "budget mama": Shipping is INSANE!!!
1/14/23, 10:43 PM - S. Petersen "budget mama": Our Favorite Popcord
1/15/23, 4:20 PM - S. Petersen "budget mama": good popcorn
1/15/23, 6:43 AM - S. Petersen "budget mama": Too small, too much shell & not enough white fluffy part
1/14/23, 11:48 PM - S. Petersen "budget mama": Tasty popcorn but kernels too small for a hot air popcorn popper
1/14/23, 1:27 PM - S. Petersen "budget mama": Small pops
1/15/23, 11:38 PM - S. Petersen "budget mama": The Best
1/15/23, 3:51 AM - S. Petersen "budget mama": Amish Baby White Popcorn
1/16/23, 1:12 AM - S. Petersen "budget mama": POPCORN DON'T GET ANY BETTER THAN THIS
1/16/23, 0:20 AM - S. Petersen "budget mama": Best Popcorn
1/15/23, 6:30 AM - S. Petersen "budget mama": baby white popcorn is tasty and has no hulls to get into teeth
1/15/23, 0:40 AM - S. Petersen "budget mama": Enjoy
1/14/23, 10:20 PM - S. Petersen "budget mama": Best Popcorn Ever
1/14/23, 8:57 PM - S. Petersen "budget mama": GREAT
1/14/23, 2:42 PM - S. Petersen "budget mama": Good Stuff
1/14/23, 0:34 AM - S. Petersen "budget mama": Popcorn lovers love this popcorn!
1/16/23, 11:57 AM - S. Petersen "budget mama": dissappointed
1/16/23, 3:28 AM - S. Petersen "budget mama": Very good popocorn
1/16/23, 1:49 AM - S. Petersen "budget mama": good stuff
1/15/23, 10:37 PM - S. Petersen "budget mama": Crispy & light!
1/15/23, 7:12 PM - S. Petersen "budget mama": Spoiled me for other popcorn
1/15/23, 9:15 AM - S. Petersen "budget mama": Heed the advice on hot air poppers
1/15/23, 2:05 AM - S. Petersen "budget mama": Amish Country Baby White Popcorn
1/15/23, 0:01 AM - S. Petersen "budget mama": average taste
1/16/23, 3:12 PM - S. Petersen "budget mama": Great little mini popcorn!
1/16/23, 2:58 PM - S. Petersen "budget mama": Tops in the Popcorn World
1/16/23, 1:49 PM - S. Petersen "budget mama": GREAT HULL LESS POPCORN
1/16/23, 0:40 AM - S. Petersen "budget mama": Poor product
1/16/23, 11:21 AM - S. Petersen "budget mama": Rip off Alert
1/16/23, 10:40 AM - S. Petersen "budget mama": Okay but there's much better
1/16/23, 8:38 AM - S. Petersen "budget mama": Good but----
1/16/23, 7:36 AM - S. Petersen "budget mama": very good
1/16/23, 7:24 AM - S. Petersen "budget mama": This is not hull-less popcorn! Or even close.
1/16/23, 6:10 AM - S. Petersen "budget mama": Received wrong product
1/16/23, 1:56 AM - S. Petersen "budget mama": Pops well, not much flavor
1/15/23, 11:00 PM - S. Petersen "budget mama": Wow, it's worth the cost for tender white hulless
1/15/23, 8:42 PM - S. Petersen "budget mama": Amish Country Baby White
1/15/23, 5:24 PM - S. Petersen "budget mama": wonderful
1/15/23, 4:52 PM - S. Petersen "budget mama": yummy
1/15/23, 4:13 PM - S. Petersen "budget mama": Best Popcorn Ever
1/15/23, 3:20 PM - S. Petersen "budget mama": Microwave Popcorn
1/15/23, 3:12 PM - S. Petersen "budget mama": wonderful
1/15/23, 3:11 PM - S. Petersen "budget mama": Just a tad too small for my wife's taste, but kids and I love it
1/15/23, 1:48 PM - S. Petersen "budget mama": small but good
1/15/23, 0:27 AM - S. Petersen "budget mama": Love it
1/15/23, 0:25 AM - S. Petersen "budget mama": great popcorn
1/15/23, 11:22 AM - S. Petersen "budget mama": The best popcorn I've ever tasted...
1/15/23, 8:45 AM - S. Petersen "budget mama": fabulous popcorn
1/15/23, 3:21 AM - S. Petersen "budget mama": Yummy popcorn.
1/15/23, 3:14 AM - S. Petersen "budget mama": great product, a little pricy, but worth it.
1/15/23, 0:36 AM - S. Petersen "budget mama": A great popcorn for small children!
1/16/23, 5:12 AM - S. Petersen "budget mama": the worst popcorn on the planet
1/16/23, 1:46 AM - S. Petersen "budget mama": Excellent popcorn
1/16/23, 0:53 AM - S. Petersen "budget mama": popcorn
1/15/23, 8:26 PM - S. Petersen "budget mama": Wabash  Valley Farms Amish Country Baby White Popcorn
1/15/23, 7:04 PM - S. Petersen "budget mama": Popcorn was alright
1/15/23, 2:12 PM - S. Petersen "budget mama": Nonthing but deadheads
1/15/23, 8:31 AM - S. Petersen "budget mama": Small Kernals
1/15/23, 7:29 AM - S. Petersen "budget mama": amish popcorn
1/15/23, 7:07 AM - S. Petersen "budget mama": Delicious Popcorn
1/15/23, 0:08 AM - S. Petersen "budget mama": Baby White Popcorn
1/15/23, 0:05 AM - S. Petersen "budget mama": great popcorn  terrible price for shipping
1/15/23, 6:24 AM - S. Petersen "budget mama": Amish County Baby White Popcorn not really in stock
1/16/23, 11:22 AM - S. Petersen "budget mama": Yummy!
1/15/23, 8:22 PM - S. Petersen "budget mama": thirty bucks?
1/15/23, 7:50 PM - S. Petersen "budget mama": Flies Begone
1/15/23, 3:18 PM - S. Petersen "budget mama": In my opinion, the best clam chowder out there!  A perfect winter meal.
1/15/23, 4:53 PM - S. Petersen "budget mama": Yes, it's from a can...
1/16/23, 0:07 AM - S. Petersen "budget mama": I, too, am perplexed
1/15/23, 11:58 AM - S. Petersen "budget mama": Bar Harbor All Natural New England Clam Chowder, 15-Ounce Cans (Pack of 6)
1/15/23, 11:45 PM - S. Petersen "budget mama": Tasteless
1/15/23, 11:21 PM - S. Petersen "budget mama": Clam Chowder
1/15/23, 9:10 PM - S. Petersen "budget mama": Clam Chowda Pizza! It's Awesome! And Simple to make!
1/15/23, 10:50 PM - S. Petersen "budget mama": Decent canned clam chowder
1/15/23, 6:54 PM - S. Petersen "budget mama": Bar Harbor News England clam chowder
1/15/23, 10:48 PM - S. Petersen "budget mama": Possibly the best canned clam chowder available.
1/16/23, 2:26 AM - S. Petersen "budget mama": What Is This "Stuff?"
1/16/23, 3:15 PM - S. Petersen "budget mama": Simplicity at it's best
1/16/23, 2:00 PM - S. Petersen "budget mama": Not very good
1/16/23, 10:03 AM - S. Petersen "budget mama": Nothing Special
1/16/23, 9:33 AM - S. Petersen "budget mama": Bar Harbor where are the clams????
1/16/23, 8:42 AM - S. Petersen "budget mama": the best
1/16/23, 8:39 AM - S. Petersen "budget mama": will buy again
1/16/23, 8:35 AM - S. Petersen "budget mama": Clam it up
1/16/23, 7:23 AM - S. Petersen "budget mama": Rather Have Chunky
1/16/23, 7:22 AM - S. Petersen "budget mama": Bit of a disappointment on two fronts
1/16/23, 4:12 AM - S. Petersen "budget mama": Can't find the clams
1/16/23, 2:48 AM - S. Petersen "budget mama": Best Canned Chowder
1/16/23, 0:53 AM - S. Petersen "budget mama": Clam 'Chowdah' Hog Heaven!
1/15/23, 11:38 PM - S. Petersen "budget mama": Best canned Clam chowder I've ever had
1/16/23, 6:11 AM - Peter Besenbruch: Lacks Certain "Key" Ingredients
1/16/23, 0:40 AM - Peter Besenbruch: Not great, not bad
1/15/23, 11:45 PM - Peter Besenbruch: Very Good, Lots of Clams and Natural Recipe
1/15/23, 10:39 PM - Peter Besenbruch: Dropped from a plane?
1/16/23, 1:33 AM - Peter Besenbruch: MMMMMM
1/16/23, 0:28 AM - Peter Besenbruch: bar harbor clam chowder
1/16/23, 11:55 AM - Peter Besenbruch: I love cashew butter!
1/16/23, 10:09 AM - Peter Besenbruch: Decent, but not great
1/16/23, 1:24 AM - Peter Besenbruch: Dog loves this stuff but...
1/16/23, 0:20 AM - Peter Besenbruch: My Dog really likes Iams Savory Sauce
1/16/23, 1:56 PM - Peter Besenbruch: Not full leaf, 1 pound, not 20 pounds
1/15/23, 6:02 PM - Peter Besenbruch: USA Chicken Stix
1/16/23, 0:28 AM - Peter Besenbruch: MADE IN THE USA
1/15/23, 5:32 PM - Peter Besenbruch: a favorite
1/15/23, 3:17 AM - Peter Besenbruch: Happy Camper!
1/16/23, 2:03 PM - Peter Besenbruch: Makes a good gift
1/15/23, 8:12 PM - Peter Besenbruch: great cereal, but too expensive online yet
1/15/23, 6:47 PM - Peter Besenbruch: Better Tasting Than Most Healthier (or High-Fiber) Cereals
1/15/23, 9:01 PM - Peter Besenbruch: BEST CEREAL EVER!
1/15/23, 8:35 PM - Peter Besenbruch: Love this cereal!
1/15/23, 7:22 PM - Peter Besenbruch: Ambrosia.
1/16/23, 0:50 AM - Peter Besenbruch: Great coconut water in just the right size!
1/16/23, 0:27 AM - Peter Besenbruch: Good taste
1/16/23, 8:42 AM - Peter Besenbruch: a great product, and convenient shipment
1/16/23, 4:33 AM - Peter Besenbruch: Best tasting coconut water I have found!
1/15/23, 7:37 PM - Peter Besenbruch: like it
1/15/23, 7:07 PM - Peter Besenbruch: Hydrating, Refreshing, Great-Tasting Drink
1/15/23, 6:28 PM - Peter Besenbruch: My favorite flavor!!
1/15/23, 6:14 PM - Peter Besenbruch: Just as advertised
1/15/23, 4:35 PM - Peter Besenbruch: Awesome tasting!
1/16/23, 0:43 AM - Peter Besenbruch: Um package change from 17oz to 16.9oz??
1/15/23, 10:14 AM - Peter Besenbruch: vita coco
1/16/23, 3:10 PM - Peter Besenbruch: I was addicted to this stuff for a while, but wore myself out
1/16/23, 2:44 PM - Peter Besenbruch: The answer to all your Cramping problems.
1/16/23, 2:44 PM - Peter Besenbruch: Vita Coco with Pineapple - the BEST yet!
1/16/23, 2:35 PM - Peter Besenbruch: vita coco
1/16/23, 2:25 PM - Peter Besenbruch: Refreshing and Delicious
1/16/23, 2:24 PM - Peter Besenbruch: My Favorite
1/16/23, 1:39 PM - Peter Besenbruch: Best Flavor- Light but Refreshing
1/16/23, 0:34 AM - Peter Besenbruch: cold and refreshing
1/16/23, 11:34 AM - Peter Besenbruch: Not the greatest.
1/16/23, 11:29 AM - Peter Besenbruch: Yummy!
1/16/23, 10:59 AM - Peter Besenbruch: Same Great Taste, just More of it!
1/16/23, 10:46 AM - Peter Besenbruch: Best coconut water flavor and size
1/16/23, 10:30 AM - Peter Besenbruch: Unusual flavor......
1/16/23, 10:26 AM - Peter Besenbruch: My afternoon pick-up
1/16/23, 8:26 AM - Peter Besenbruch: thirst quenching
1/16/23, 8:18 AM - Peter Besenbruch: Coconut Water with Pineapple...Yummy!
1/16/23, 7:55 AM - Peter Besenbruch: Finally, a coconut water I like
1/16/23, 7:40 AM - Peter Besenbruch: delicious!!!
1/16/23, 5:13 AM - Peter Besenbruch: Coconut Water
1/16/23, 5:13 AM - Peter Besenbruch: Yummy
1/16/23, 4:56 AM - Peter Besenbruch: Good for use in smoothies
1/16/23, 4:46 AM - Peter Besenbruch: Awesome
1/16/23, 4:40 AM - Peter Besenbruch: Vita Coco Water is Awsome
1/15/23, 1:42 PM - Peter Besenbruch: EXCELLENT
1/15/23, 1:30 PM - Peter Besenbruch: Delicious and Rejuvenating
1/15/23, 0:33 AM - Peter Besenbruch: great taste. nice fruit flavor. serve chilled
1/15/23, 11:54 AM - Peter Besenbruch: Vita coco is best
1/16/23, 4:35 AM - Peter Besenbruch: Nutritional content of this brand does not live up to what's on the label.
1/16/23, 11:16 AM - Peter Besenbruch: GROSS
1/15/23, 5:34 PM - Peter Besenbruch: So Addicted
1/15/23, 10:53 PM - Peter Besenbruch: well ...
1/15/23, 10:52 AM - Peter Besenbruch: yuck
1/16/23, 0:10 AM - Peter Besenbruch: Amazon won't live up to their end
1/15/23, 4:39 PM - Peter Besenbruch: Safety Instructions for coca tea
1/16/23, 8:36 AM - Peter Besenbruch: My pug loves them but I got a different hartz treat.
1/16/23, 8:08 AM - Peter Besenbruch: My Sheltie Adores Them!
1/16/23, 2:45 PM - Peter Besenbruch: Great treats
1/16/23, 11:45 AM - Peter Besenbruch: Wrong Product displayed for order
1/16/23, 10:35 AM - Peter Besenbruch: piggie skins
1/16/23, 9:27 AM - Peter Besenbruch: Extremely Disappointed
1/16/23, 3:07 AM - Peter Besenbruch: my favorite sugarless flavor
1/16/23, 1:29 AM - Peter Besenbruch: Love this gum
1/16/23, 4:49 AM - Peter Besenbruch: Best cinnamon gum out there!
1/16/23, 9:21 AM - Peter Besenbruch: another great Green Mountain coffee
1/16/23, 4:20 AM - Peter Besenbruch: greatest coffee
1/16/23, 1:48 PM - Peter Besenbruch: great deal!
1/16/23, 1:36 PM - Peter Besenbruch: Best in show for K-cup French Roast
1/16/23, 0:54 AM - Peter Besenbruch: Great coffee, great price
1/16/23, 0:54 AM - Peter Besenbruch: One of my favorite coffees
1/16/23, 0:10 AM - Peter Besenbruch: Great cup of Coffee
1/16/23, 8:38 AM - Peter Besenbruch: excellent choice
1/16/23, 8:26 AM - Peter Besenbruch: Green Mountain K Cups
1/16/23, 7:33 AM - Peter Besenbruch: Green Mountain compared with Tully's French Roast
1/16/23, 6:24 AM - Peter Besenbruch: My FAVORITE K-Cup
1/16/23, 5:32 AM - Peter Besenbruch: This is great French Roast
1/15/23, 11:58 PM - Peter Besenbruch: Love this coffee
1/15/23, 11:11 PM - Peter Besenbruch: Tastes like...
1/15/23, 1:20 AM - Peter Besenbruch: Yummy Cookies
1/14/23, 9:23 AM - Peter Besenbruch: 3.5* snack for a non-chocophile
1/14/23, 9:46 PM - Peter Besenbruch: Peanut Butter Cookies
1/14/23, 3:36 PM - Peter Besenbruch: Good buy
1/14/23, 1:39 PM - Peter Besenbruch: The portable and edible Oreo
1/14/23, 11:38 PM - Peter Besenbruch: Very good snack!
1/14/23, 11:24 PM - Peter Besenbruch: These are ok.....
1/14/23, 3:36 PM - Peter Besenbruch: Very Good
1/14/23, 9:17 AM - Peter Besenbruch: Flavor in, Calories Down, Fat Nearly Out
1/14/23, 9:14 AM - Peter Besenbruch: Now we have the Oreo transformed into a baked chocolate wafer snack
1/15/23, 8:49 AM - Peter Besenbruch: not as good as the 100-calorie Oreos
1/14/23, 10:56 PM - T. Saad "T-bone": Great Taste!!!
1/14/23, 7:13 PM - T. Saad "T-bone": Seemingly impossible...
1/14/23, 9:28 AM - T. Saad "T-bone": THESE ARE TRUE 'MAINSTREAM' DIET SNACKS --
1/14/23, 9:14 AM - T. Saad "T-bone": Chocolate Wafers in an Identity Crisis as Oreos...But If Deception Helps Monitor Calories, Why Not?
1/16/23, 2:57 PM - T. Saad "T-bone": Oreo Crisps
1/16/23, 6:41 AM - T. Saad "T-bone": Not The Best Cookies I've Ever Had!
1/16/23, 3:25 AM - T. Saad "T-bone": Yummy
1/15/23, 11:52 PM - T. Saad "T-bone": very yummy
1/15/23, 6:46 PM - T. Saad "T-bone": Oreo Dipped Delight Bars
1/15/23, 11:58 AM - T. Saad "T-bone": teaching cookies
1/15/23, 11:49 AM - T. Saad "T-bone": 100 calorie Cakesters
1/15/23, 11:42 AM - T. Saad "T-bone": They're not bad
1/15/23, 9:28 AM - T. Saad "T-bone": Fantastic little treats!
1/15/23, 7:04 AM - T. Saad "T-bone": 100 Calorie Pack, Chips Ahoy Cookies
1/15/23, 6:56 AM - T. Saad "T-bone": Great 100 Calorie Treat!!
1/15/23, 6:10 AM - T. Saad "T-bone": Good, and just enough to satisfy you.
1/15/23, 6:01 AM - T. Saad "T-bone": Good snack
1/15/23, 3:28 AM - T. Saad "T-bone": Cookie chips were not very tasty
1/15/23, 3:23 AM - T. Saad "T-bone": Yummers!
1/15/23, 3:18 AM - T. Saad "T-bone": Good snacks
1/15/23, 2:47 AM - T. Saad "T-bone": Oreo Thin Crisps 100 Calorie Packs
1/15/23, 0:05 AM - T. Saad "T-bone": Oreo Thin Crisps work for me
1/14/23, 10:42 PM - T. Saad "T-bone": Yummy!
1/14/23, 10:35 PM - T. Saad "T-bone": Chocolate Wafers in an Identity Crisis as Oreos...But If Deception Helps Monitor Calories, Why Not?
1/14/23, 4:45 PM - T. Saad "T-bone": I'm a fan...
1/14/23, 9:27 AM - T. Saad "T-bone": Oreo flavored crackers without the creme filling
1/14/23, 9:25 AM - T. Saad "T-bone": Not impressed
1/14/23, 9:14 AM - T. Saad "T-bone": CRISPY, CRUNCHY, AND CHOCOLATEY
1/15/23, 7:00 AM - T. Saad "T-bone": Delicious Mini Chocolate Treats Help Weight Loss Efforts!
1/14/23, 10:39 PM - T. Saad "T-bone": Delicious
1/15/23, 5:54 AM - T. Saad "T-bone": I agree with P. Lucas
1/15/23, 5:54 AM - T. Saad "T-bone": Good? You CAN'T be serious
1/14/23, 11:51 PM - T. Saad "T-bone": these ain't oreo's
1/14/23, 3:37 PM - T. Saad "T-bone": Good product but not fresh
1/16/23, 11:11 AM - T. Saad "T-bone": I love these!!!
1/16/23, 11:57 AM - T. Saad "T-bone": Not so great
1/15/23, 11:36 PM - T. Saad "T-bone": nt
1/16/23, 0:59 AM - T. Saad "T-bone": Amazing
1/15/23, 4:12 AM - T. Saad "T-bone": Worked very well
1/16/23, 6:25 AM - T. Saad "T-bone": Keeps my cats happy and healthy
1/16/23, 2:58 PM - T. Saad "T-bone": All 3 of my cats refused to eat it
1/15/23, 9:11 PM - T. Saad "T-bone": The worst snap-lock reseal ever made?
1/15/23, 10:43 PM - T. Saad "T-bone": Filler food is empty, leaves your cat always needing more
1/16/23, 1:29 AM - T. Saad "T-bone": She Loves It
1/16/23, 4:06 AM - T. Saad "T-bone": Kitty Junk Food
1/15/23, 11:42 AM - T. Saad "T-bone": Not minced, this is ground beef
1/16/23, 10:16 AM - T. Saad "T-bone": Not minced
1/16/23, 4:06 AM - T. Saad "T-bone": Kitty Junk Food
1/15/23, 10:43 PM - T. Saad "T-bone": Filler food is empty, leaves your cat always needing more
1/15/23, 6:27 PM - T. Saad "T-bone": All By-Product & Corn -- Don't Waste Your Money!
1/15/23, 5:09 PM - T. Saad "T-bone": Quanty????
1/15/23, 10:49 PM - T. Saad "T-bone": Best Green Tea Ever!
1/14/23, 1:55 PM - T. Saad "T-bone": Looks better than it tasted, I'm told
1/15/23, 7:35 PM - T. Saad "T-bone": Wow!!!!!!!!!!
1/15/23, 4:20 PM - T. Saad "T-bone": I love, love, love, coffee!!!
1/16/23, 8:31 AM - T. Saad "T-bone": Parmesan Heaven
1/15/23, 0:38 AM - T. Saad "T-bone": fantastic product
1/15/23, 1:36 PM - T. Saad "T-bone": Not happy with the product!
1/16/23, 2:52 PM - T. Saad "T-bone": these beans were wonderful
1/15/23, 11:34 PM - T. Saad "T-bone": Great Peanuts!
1/16/23, 2:19 AM - T. Saad "T-bone": Much better than tea bags
1/16/23, 2:45 AM - T. Saad "T-bone": Love this stuff!!
1/16/23, 0:48 AM - T. Saad "T-bone": totally satisfying!
1/14/23, 2:00 AM - T. Saad "T-bone": Superlative store bought cookies: very hard to find!
1/16/23, 0:15 AM - T. Saad "T-bone": Awful
1/16/23, 6:44 AM - T. Saad "T-bone": Love this dressing! - Wild Thymes Products: Meyer Lemon Dressing
1/16/23, 10:01 AM - T. Saad "T-bone": almost expired seaweed
1/16/23, 2:22 AM - T. Saad "T-bone": Deliciously seasoned, lite and crispy!
1/15/23, 11:31 PM - T. Saad "T-bone": contains MSG
1/16/23, 3:02 PM - T. Saad "T-bone": seaweed and rice
1/16/23, 11:51 AM - T. Saad "T-bone": Great for snacking
1/16/23, 10:39 AM - T. Saad "T-bone": Tasty
1/16/23, 3:15 PM - T. Saad "T-bone": hard to find in New York, glad amazon can deliver it
1/16/23, 0:41 AM - T. Saad "T-bone": 1 star for price, 5 stars for taste
1/15/23, 6:11 AM - T. Saad "T-bone": Best tasting wheat free, gluten free cake mix available
1/16/23, 7:33 AM - T. Saad "T-bone": gluten free basic mix
1/16/23, 6:18 AM - T. Saad "T-bone": Could have been better
1/15/23, 0:20 AM - T. Saad "T-bone": strange flavor
1/16/23, 3:08 PM - T. Saad "T-bone": Awesome with some changes
1/16/23, 5:34 AM - T. Saad "T-bone": A cake for all occassions.
1/15/23, 8:44 PM - T. Saad "T-bone": Namaste Foods, Gluten Free Vanilla cake Mix
1/15/23, 8:36 PM - T. Saad "T-bone": yummy as cupcakes
1/15/23, 8:47 AM - T. Saad "T-bone": Tasty
1/15/23, 8:02 AM - T. Saad "T-bone": 2nd Birthday Saviour!
1/15/23, 7:32 PM - T. Saad "T-bone": Just awful
1/16/23, 9:18 AM - T. Saad "T-bone": Large Quanity, discontinued seasonal delicious tea
1/16/23, 9:11 AM - T. Saad "T-bone": SWEET DREAMS
1/16/23, 7:32 AM - T. Saad "T-bone": The best for a winter tea party!
1/15/23, 11:28 PM - T. Saad "T-bone": Wonderful
1/15/23, 1:43 PM - T. Saad "T-bone": Love the tea!
1/14/23, 0:24 AM - T. Saad "T-bone": Fun, Intense Holiday Tea
1/15/23, 6:24 AM - T. Saad "T-bone": Fast shipping good company to buy from
1/14/23, 4:06 PM - T. Saad "T-bone": A very pleased customer
1/15/23, 7:00 AM - T. Saad "T-bone": Great cookie and lots of fun
1/14/23, 9:07 PM - T. Saad "T-bone": ...while in bed
1/14/23, 8:51 PM - T. Saad "T-bone": Fortune Cookies
1/16/23, 1:24 PM - T. Saad "T-bone": Color Discrepancy
1/16/23, 0:31 AM - T. Saad "T-bone": crispy fresh
1/16/23, 10:39 AM - T. Saad "T-bone": they are soooo tiny!
1/16/23, 7:32 AM - T. Saad "T-bone": Excellent service and product
1/16/23, 8:00 AM - Dicey: boring boring boring
1/16/23, 0:59 AM - Dicey: feliciaflan
1/16/23, 0:18 AM - Dicey: Fortune Cookies
1/16/23, 10:06 AM - Dicey: Very good
1/16/23, 8:31 AM - Dicey: awsome!!
1/16/23, 8:18 AM - Dicey: PERFECT
1/16/23, 8:32 AM - Dicey: satisfied customer
1/16/23, 8:06 AM - Dicey: great product--but a rip-off on this site
1/16/23, 8:11 AM - Dicey: Great aroma, and I don't like coffee
1/16/23, 7:39 AM - Dicey: Jarred Paradise
1/14/23, 1:46 PM - Dicey: Yummy!
1/16/23, 10:01 AM - Dicey: Tastes Like Wint-O-Green Life Savers
1/15/23, 6:21 PM - Dicey: Good popcorn, poor shipping
1/15/23, 8:51 PM - Dicey: It's like Buttah!
1/15/23, 5:24 PM - Dicey: Awesome snack, great product.
1/16/23, 3:17 PM - Dicey: Handy Size
1/16/23, 2:35 PM - Dicey: My cats love this tuna
1/16/23, 5:45 AM - Dicey: Good Nutrition and Right Size.
1/16/23, 4:45 AM - Dicey: convenient, filling, 70 calories and lots o protein = great work lunch item
1/15/23, 9:20 AM - Dicey: Quick wild rice is ok
1/16/23, 11:58 AM - Dicey: Best Quick Cook Wild Rice.
1/15/23, 1:35 PM - Dicey: Great Quality and convenient quick cooking
1/16/23, 3:47 AM - Dicey: Very good corral for 1 horse, maybe 2 with additional electric tape
1/16/23, 4:00 AM - Dicey: Easy and portable...but a few issues
1/16/23, 4:39 AM - Dicey: Easy Assembly - Great for Alpacas!
1/16/23, 6:38 AM - Dicey: Nicely thought out kit for temporary grazing etc
1/16/23, 4:49 AM - Dicey: Easy Setup, Nice Design
1/16/23, 4:19 AM - Dicey: Works for us
1/16/23, 4:13 AM - Dicey: Great for short term fencing!
1/16/23, 4:53 AM - Dicey: It is very easy to set up.
1/16/23, 4:14 AM - Dicey: Good
1/15/23, 7:13 PM - Dicey: Love it!
4/5/22, 7:09 AM - Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Tap to learn more.
2/15/22, 11:54 AM - Ishroop created group "M1 Official Group"
2/15/22, 11:54 AM - You were added
4/5/22, 9:11 AM - Shalin: @Prerna keh rhi ,hame bhi deni hai ai/ML ki assignment
4/5/22, 9:11 AM - Shalin: Prr ek baar confirm kr lena
4/5/22, 9:11 AM - Gursharan Kaur✨: XD
4/5/22, 9:11 AM - Gursharan Kaur✨: Agar prerna ne btaya toh achhe se krlena 😂
4/5/22, 9:15 AM - Shalin: Ok ✌
4/5/22, 9:15 AM - Shalin: Confirm krke bta dena
😄😄
4/5/22, 9:16 AM - Shalin: @Himank aur @prerna  dono keh rhe deni hai
4/5/22, 9:16 AM - Shalin: ++
4/5/22, 9:49 AM - Ishroop changed the group description
4/5/22, 10:15 AM - Yashwin: Agar koi doosri branches mei kisi ko jaanta hai assignment bhejdena
4/5/22, 10:45 AM - Ishroop changed this group's icon
4/5/22, 10:44 AM - Gursharan Kaur✨: M1 M2 M3 has to submit their manufacturing practical files by next week and prerpare for viva as well in your respective manufacturing labs
4/5/22, 10:44 AM - Gursharan Kaur✨: Bs yahi bcha tha 😭😭😭😭
4/5/22, 10:44 AM - Ishroop: Ye dukh kaahe khatam nahi hota 😭
4/5/22, 10:55 AM - Arihan Mech: Practical lagana hai?
4/5/22, 10:58 AM - Yashwin: Me nd Kshitiz in lab aajao
4/5/22, 10:59 AM - Yashwin: Waise bhi jaldi free hojate hai
4/5/22, 10:59 AM - Arihan Mech: Roto block?
4/5/22, 10:59 AM - Yashwin: Yup
4/5/22, 11:11 AM - Yashwin: <Media omitted>
4/5/22, 11:18 AM - Sagar: <Media omitted>
4/5/22, 11:47 AM - Yashwin: <Media omitted>
4/5/22, 12:00 PM - Yashwin: .
4/5/22, 3:42 PM - Sagar: Yeh check kr lena submit krne se pehle ki yeh correct hai ya nahi
4/5/22, 8:11 PM - Yashwin: Desirable Properties of an Ideal Refrigerant
We have discussed above that there is no ideal refrigerant. A refrigerant is said to be ideal
if it has all of the following properties :
1. Low boiling and freezing point,
2. High critical pressure and temperature,
3. High latent heat of vaporisation,
4. Low specific heat of liquid, and high specific heat of vapour,
5. Low specific volume of vapour,
6. High thermal conductivity,
7. Non-corrosive to metal,
8. Nonflammable and non-explosive,
9. Non-toxic,
10. Low cost,
11. Easily and regularly available,
12. Easy to liquify at moderate pressure and temperature,
13. Easy of locating leaks by odor or suitable indicator,
14. Mixes well with oil,
15. High coefficient of performance, and
16. Ozone friendly.
The standard comparison of refrigerants, as used in the refrigeration industry, is based on
an evaporating temperature of - 15°C and a condensing temperature of + 30° C.
4/5/22, 8:11 PM - Yashwin: Ans 1
4/5/22, 8:24 PM - Yashwin: Yaar Ai/ml ki assignment karni submit ya nahi ?
4/5/22, 8:31 PM - Ishroop: Btao
4/5/22, 8:31 PM - Ishroop: Questions done
Ans 1
4/5/22, 8:32 PM - Yashwin: Ans 14 send kar rha
4/5/22, 8:32 PM - Ishroop: Ruko
4/5/22, 8:33 PM - Ishroop: Ans 1,2,4,5,7,8,9,11
4/5/22, 8:33 PM - Ishroop: I have all these
4/5/22, 8:33 PM - Ishroop: Inke alaawa bhejo
4/5/22, 8:33 PM - Yashwin: 14 mei kar rha
4/5/22, 8:33 PM - Yashwin: Send
4/5/22, 8:33 PM - Ishroop: Ok
4/5/22, 8:33 PM - Ishroop: I'll send all after dinner
4/5/22, 8:33 PM - Yashwin: 2 nd bhejde
4/5/22, 8:34 PM - Ishroop: Khaana kha ke bhejti yaar. I literally just reached home 🥲
4/5/22, 8:36 PM - YUDHISHTER RANA Pec Mech: .
4/5/22, 8:36 PM - YUDHISHTER RANA Pec Mech: M2 ka to postpone ho gaya
4/5/22, 8:36 PM - Ishroop: 1. Arihan Q3
2. Gautam Q6
3. Gursharan Q15
4. Ishroop Q2,4,5,7,8,9,11
5. Kshitiz Q10
6. Mohak Q12
7. Priyanshu Q13
8. Rohit Q15
9.Sagar Q3
10.Sankalp Q6
11.Shalin Q10
12.Sparsh Q15
13.Yashwin Q1,14
14. Yudhishter Q12
4/5/22, 8:37 PM - Ishroop: @918427563125 @919814484499 @918699133946 @916239412997 @917710715181 @919467734085 @919478379030 @918146907246 @919779772164 @919877113830 @918054349284 @916239902903
4/5/22, 8:37 PM - Ishroop: Bhai 10 baje tak sab answers bhejo
4/5/22, 8:37 PM - Ishroop: Aaj rac khatam krke sona
4/5/22, 8:37 PM - Kshitiz Sharma Mech: Okay
4/5/22, 8:38 PM - Rohit Pec Mech: 👍🏼
4/5/22, 8:38 PM - Yashwin: Phir humari bhi postpone
4/5/22, 8:38 PM - YUDHISHTER RANA Pec Mech: Par aisa kuch Hua ni tha decision.Ya to saare hi M1 wale submit na karein
4/5/22, 8:39 PM - Yashwin: Ha matlab wohi
4/5/22, 8:39 PM - Ishroop: Dekho ai ml copy paste hai
4/5/22, 8:39 PM - Ishroop: Agar submit krni hai to ek banda complete krke group mein bhejdo
4/5/22, 8:39 PM - Ishroop: Wrna rehne do
4/5/22, 8:40 PM - Yashwin: Brines are secondary refrigerants and are generally used where temperatures are required to
be maintained below the freezing point of water i.e. O°C. In case the temperature involved is above
the freezing point of water (0°C), then water is commonly used as a secondary refrigerant.
The mass of the salt in the solution
expressed as the percentage of the mass of the
solution is known as concentration of the solution.
As the concentration of the solution increases, its
freezing point decreases. But if the concentration of
the salt is increased beyond a certain point, the
freezing point increases instead of decreasing. The
point at which the freezing temperature is minimum,
is
known
as cutectic temperature
and
the
concentration at this point is known as eutectic
concentration.
The brine used in
a particular
application should have a concentration for which
the freezing point of the brine is at least 5°C to 8°C
lower than the brine temperature required.
The brines commonly used are calcium chloride (CaCl,), sodium chloride i.e. common salt
(NaC1) and glycols such as ethylene glycol, propylene glycol etc.
The calcium chloride brine has the eutectic temperature of - 55°C at salt concentration of
30% by mass. This brine is primarily used where temperatures below - 18°C are required. It is
generally used in industrial process cooling and product freezing. The chief disadvantages of
calcium chloride brine are its dehydrating effect and its tendency to impart a bitter taste to food
products.
The sodium chloride brine has the eutectic temperature of - 21.1°C at salt concentration of
23% by mass. This brine is used in chilling and freezing of meat and fish.
Both of the above two brines are corrosive in nature for metallic containers which put
limitation on their use. Also the thermal properties of the above two brines are less satisfactory.
Other water soluble compounds known as antifreeze are also used for decreasing the
freezing point of water for certain refrigeration uses. Ethylene and propylene glycol have a number
of good properties. Since they are non-corrosive and non-electrolytic even in the presence of water,
therefore, these brines are most extensively used as antifreeze elements. The following table shows
typical applications of various brines.
4/5/22, 8:40 PM - Yashwin: 14
4/5/22, 8:41 PM - Gursharan Kaur✨: Yaar abhi mepe book h ni na hi pdf h
4/5/22, 8:41 PM - Gursharan Kaur✨: Toh kal subah bhejdungi m krke
4/5/22, 8:41 PM - Gursharan Kaur✨: Asap
4/5/22, 8:41 PM - Ishroop: Q15 tujhe n sparsh ko likha hai
4/5/22, 8:41 PM - Ishroop: Sparsh kr dega koini
4/5/22, 8:41 PM - Ishroop: @918054349284
4/5/22, 8:42 PM - Gursharan Kaur✨: Mne konsa krna ?
4/5/22, 8:42 PM - Gursharan Kaur✨: 😂
4/5/22, 8:42 PM - Ishroop: Main saare meine yashwin ne kr diye
4/5/22, 8:42 PM - Ishroop: Thode se bache thei
4/5/22, 8:42 PM - Ishroop: Har ques 2 logo ko diya hai
4/5/22, 8:42 PM - Ishroop: Aapas mein sort krlo
4/5/22, 8:42 PM - Ishroop: Jo bach gye thei mtlb
4/5/22, 8:43 PM - Yashwin: 15 not 14 😅
4/5/22, 8:44 PM - Ishroop: @918054349284 do 14 then
4/5/22, 9:15 PM - Shalin: Carbon dioxide : The principle refrigeration use of carbon dioxide is dry ice .
The boiling point of this refrigerant is so extremely low (-73.6 degrees) that is -15 degrees , a pressure of well over 20.7 bar is required to prevent its evaporation . At condenser temperature of 30 degree , a pressure of approx 70 bar is required to liquefy the gas , due to high operating pressure , the compressor of a carbon dioxide refrigerator unit is very small even for a comparatively large ref capacity,  also due to low efficiency as compared to other common refrigerant , it is seldom used in household units , but is used in some industrial applications and ships but is not highly economical for usage
4/5/22, 9:16 PM - Shalin: Q10 (a)part
4/5/22, 9:37 PM - Ishroop: ..
4/5/22, 9:41 PM - YUDHISHTER RANA Pec Mech: Iska kya scene hai??
4/5/22, 9:42 PM - Yashwin: Nahi karni
4/5/22, 9:42 PM - Yashwin: Refregeration ke ans bhejde
4/5/22, 9:47 PM - Rohit Pec Mech: <Media omitted>
4/5/22, 9:47 PM - Rohit Pec Mech: <Media omitted>
4/5/22, 9:47 PM - Rohit Pec Mech: Q 15 - only underlined part to be written
4/5/22, 9:47 PM - Kshitiz Sharma Mech: bhai aise ni chlegaa
4/5/22, 9:47 PM - Kshitiz Sharma Mech: likh ke bhej
4/5/22, 9:48 PM - Rohit Pec Mech: Likh ke subah tak bhej dunga
4/5/22, 9:50 PM - Sagar: <Media omitted>
4/5/22, 9:51 PM - Kshitiz Sharma Mech: <Media omitted>
4/5/22, 9:52 PM - Kshitiz Sharma Mech: yrr 10 ka exact ans to milna mushkil h
4/5/22, 9:52 PM - Kshitiz Sharma Mech: ye dekhlo agr thik lge to krlena
4/5/22, 9:53 PM - Rohit Pec Mech: Kal koi submission to nhi hai na ?
4/5/22, 9:53 PM - Kshitiz Sharma Mech: nope
4/5/22, 9:53 PM - Rohit Pec Mech: 👍🏼
4/5/22, 9:53 PM - Rohit Pec Mech: Aiml ki to aaj raat se pehle karni hai na
4/5/22, 9:53 PM - Rohit Pec Mech: Agar wo hai kisipe to bhejdo
4/5/22, 9:53 PM - Kshitiz Sharma Mech: yrr cnfrm krdo aiml ka
4/5/22, 9:53 PM - Yashwin: Ai ml postpone hojayegi mat lo tension
4/5/22, 9:53 PM - Rohit Pec Mech: Pkka ?
4/5/22, 9:53 PM - Rohit Pec Mech: Kisne bola ?
4/5/22, 9:54 PM - Yashwin: Ha Himank se kaafi logo ki baat hogayi
4/5/22, 9:54 PM - Rohit Pec Mech: Okok
4/5/22, 9:57 PM - Yashwin: @916239579405 send karde answers
4/5/22, 10:02 PM - Gautam Pec: <Media omitted>
4/5/22, 10:02 PM - Gautam Pec: <Media omitted>
4/5/22, 10:02 PM - Ishroop: On it
4/5/22, 10:05 PM - Ishroop: Desirable Properties of an ideal Refrigerant


1. Thermodynamic Properties:
               (i) Low boiling point
              (ii) Low freezing point
             (iii) Positive pressures (but not very high) in condenser and evaporator.
             (iv) High saturation temperature
              (v) High latent heat of vapourization

2. Chemical Properties:
               (i) Non-toxicity
              (ii) Non-flammable and non-explosive
             (iii) Non-corrosiveness
             (iv) Chemical Stability in reacting
              (v) No effect on the quality of stored (food and other) products

3. Physical Properties:
               (i) Low specific volume of vapour
              (ii) Low specific heat
             (iii) High thermal conductivity
             (iv) Low viscosity
              (v) High electrical insulation

4. Others Properties:
               (i) Ease of leakage location
              (ii) Availability and low cost
             (iii) Ease of handling
             (iv) High COP
              (v) Low power consumption per tonne of refrigeration
             (vi) Low pressure ratio and pressure difference
4/5/22, 10:05 PM - Ishroop: ans 1
4/5/22, 10:05 PM - Ishroop: An azeotrope (/əˈziːəˌtroʊp/)[1] or a constant boiling point mixture is a mixture of two or more liquids whose proportions cannot be altered or changed by simple distillation.[2] This happens when an azeotrope is boiled, the vapour has the same proportions of constituents as the unboiled mixture. Because their composition is unchanged by distillation, azeotropes are also called (especially in older texts) constant boiling point mixtures.

Some azeotropic mixtures of pairs of compounds are known,[3] and many azeotropes of three or more compounds are also known.[4] In such a case it is not possible to separate the components by fractional distillation. There are two types of azeotropes: minimum boiling azeotrope and maximum boiling azeotrope. A solution that shows greater positive deviation from Raoult's law forms a minimum boiling azeotrope at a specific composition. For example, an ethanol–water mixture (obtained by fermentation of sugars) on fractional distillation yields a solution containing at most 97.2% (by volume) of ethanol. Once this composition has been achieved, the liquid and vapour have the same composition, and no further separation occurs. A solution that shows large negative deviation from Raoult's law forms a maximum boiling azeotrope at a specific composition. Nitric acid and water is an example of this class of azeotrope. This azeotrope has an approximate composition of 68% nitric acid and 32% water by mass, with a boiling point of 393.5 K (120.4 °C).
4/5/22, 10:05 PM - Ishroop: ans 7
4/5/22, 10:05 PM - Ishroop: Ammonia Gas or Refrigerant R717
Ammonia is amongst the oldest of all the refrigerants and still used widely in the refrigeration applications. It is also the only refrigerant outside the halocarbons group, still being used to a great extent. Ammonia refrigerant is commonly known as R717 and its chemical formula is NH3. Its molecular weight is 17 and boiling point is -28 degree F (-2.22 degree C).


Ammonia has highest refrigerating capacity per pound of any refrigerant and a number of other excellent thermal properties that make it popular for a number of refrigeration applications in spite of its being toxic, explosive and flammable within certain conditions. Ammonia is used as refrigerant prominently in the refrigeration systems of food industry like dairies, ice creams plants, frozen food production plants, cold storage warehouses, processors of fish, poultry and meat and number of other applications.

Properties and Advantages of Ammonia Refrigerant
1) Small piston displacement: Ammonia has the highest refrigerating effect per pound compared to all the refrigerants being used including the halocarbons. Even though the specific volume of ammonia is high, the compressor displacement required per ton of refrigeration is quite small, due to this small compressor is required per ton of the refrigeration capacity. This saves lots of power in the long run.



2) Compressor used with ammonia refrigerant: Since the specific volume of ammonia is high it is used mostly with rotary and the centrifugal compressors though it can be used with open type of reciprocating compressor as well.

3) Condensers used with ammonia refrigerant: The condensers used in the refrigeration systems using ammonia gas as the refrigerant are of water cooled type or evaporative type. This again is mainly because of the high volume of the gas handled by the refrigeration system. Air cooled condensers are used in the systems that have rotary screw compressors.

4) Chillers used with ammonia refrigerant: Ammonia can be used with direct expansion types of chillers as well as flooded chillers. In flooded chillers there is higher heat transfer that results in higher refrigerating effect for ammonia refrigerant.


5) Environment friendly: One of the biggest advantages of ammonia gas as the refrigerant is that it is safe to the environment and does not cause any depletion of the ozone layer. Due to this it won’t not have to be replaced with any alternative refrigerants as is the case with number of chlorofluorocarbons (CFCs). Ammonia is the oldest of all the refrigerants being used and it will compete with the new refrigerants for a number of years to come.

6) Materials used in the refrigeration system: For the standard conditions of say, -15 degree C in the evaporator, the condenser and the evaporator pressures are 2.37 bar and 11.67 bar respectively, which are quite moderate. Since the pressures are not very high, lightweight materials can be used for the construction of the equipment. The pressure in the evaporator is quite high so it is not necessary to expand the gas to very low pressure. This also enables high suction pressure for the compressor and lower compression ratio.

7) High discharge temperature of ammonia gas: The discharge temperature of the ammonia refrigerant from the compressor is high, hence water cooling of the cylinder heads and the cylinders of the compressor is very important. If high discharge pressure is required, it is advisable to use the multi-cylinder compressors instead of the single cylinder compressor to avoid overheating of the compressor.

8) Corrosive nature of ammonia: Anhydrous ammonia is non-corrosive in nature, however, in presence of moisture it tends to become corrosive to copper, brass and other non-ferrous materials. Thus while in halocarbon systems, copper is used predominantly in the refrigeration equipment, its use should be avoided in the ammonia refrigeration systems.

9) Miscibility with oil: Ammonia refrigerant is non-miscible with oil so it does not mix with the oil in the crankcase of the compressor. The ammonia refrigerant leaving the compressor picks up oil particles and carries them to the condenser and then the evaporator. Here these oil particles tend to reduce the heat transfer efficiency from the refrigerant. The oil separator should be installed in the evaporator to remove the oil and return it back to the crankcase.


10) Leak testing of ammonia: The leak testing of ammonia from the refrigeration system can be done either by using sulfur sticks or soap solution. When ammonia reacts with sulfur, a dense smoke is formed. To detect the leakage of ammonia from the refrigeration system, the stick is dipped into sulfur and moved around in the whole plant. The location where the dense smoke is formed can be further traced to find exact point of leakage of the refrigerant. The leak testing can also be done by applying the soap solution at the various joints of the pipeline. At the point of leakage bubbles are formed in the solution.

11) Ammonia is cheap and available readily: Ammonia is available almost everywhere and is the cheapest of all the commonly used refrigerants. These coupled with the chemical stability of ammonia, its high refrigerant effect, and non-miscibility make it ideal refrigerant for the applications and places where toxicity is not a major factor.
4/5/22, 10:05 PM - Ishroop: ans 9
4/5/22, 10:07 PM - Yashwin: 3rd ka bhi same hi hoga ans
4/5/22, 10:08 PM - Ishroop: Wohi lag raha tha mujhe bhi
4/5/22, 10:22 PM - YUDHISHTER RANA Pec Mech: <Media omitted>
4/5/22, 10:22 PM - YUDHISHTER RANA Pec Mech: <Media omitted>
4/5/22, 10:22 PM - YUDHISHTER RANA Pec Mech: <Media omitted>
4/5/22, 10:22 PM - YUDHISHTER RANA Pec Mech: <Media omitted>
4/5/22, 10:22 PM - YUDHISHTER RANA Pec Mech: <Media omitted>
4/5/22, 10:22 PM - YUDHISHTER RANA Pec Mech: <Media omitted>
4/5/22, 10:23 PM - YUDHISHTER RANA Pec Mech: Q12
4/5/22, 10:41 PM - Ishroop: Bhai ye kya hai?
4/5/22, 10:41 PM - Ishroop: 6 pages 🥲🥲🥲
4/5/22, 10:41 PM - Rohit Pec Mech: Bc yudhishthir
4/5/22, 10:41 PM - Rohit Pec Mech: 😭
4/5/22, 10:41 PM - YUDHISHTER RANA Pec Mech: har 1 table mein se 3-4 examples
4/5/22, 10:42 PM - Rohit Pec Mech: Kal final answer likhke bhejdio bhai
4/5/22, 10:42 PM - Rohit Pec Mech: Itne pages ki total assignment banti hai 😓
4/5/22, 10:42 PM - YUDHISHTER RANA Pec Mech: kal subah tak pakka
4/5/22, 10:42 PM - Rohit Pec Mech: Oki 🫂
4/5/22, 11:04 PM - Priyanshu Mech: 13)

a) R600A:
 R134A:
 R22:
 R12:

b) Ammonia:
 R22:
 R23:
 R508B:
 R449A:

c) Liquid Ammonia

d) R-410A
 R-22
 R-32
 R-290
 R-134A
 R-600A

e) R11
 R113
 R12
 R134a
 R245fa
4/5/22, 11:04 PM - Priyanshu Mech: Ismein saare refrigerants ke operating pressures nhi mil rhe aur book mein pressure of evaporator, condesor aur critical pressure given h. Toh wohi add kardu?
4/5/22, 11:17 PM - Ishroop: p.s. i have 14-15 copies aaj ke mv ke practical ki. jis jis ko chahiye mere se le lena warna apne aap print nikalwa lena rohit graphics se
4/5/22, 11:17 PM - Yashwin: Ok 👍
4/5/22, 11:17 PM - Ishroop: *IMPORTANT*
4/6/22, 6:21 PM - Sagar: Ai /ml mein 4, 5 ques mein data set wrong hai
4/6/22, 6:21 PM - Sagar: <Media omitted>
4/6/22, 6:39 PM - YUDHISHTER RANA Pec Mech: THERMODYNAMIC PROPERTIES OF REFRIGERANTS:-
1.BOILING TEMPERATURE-Boiling temperature should be low at atmosphericpressure,if it is high then compressor should be operated in high vacuum.
Eg.(i)R-11 - +23.77°C
     (ii)R-134a - -26.15°C
      (iii)R-30 - +39.8°C

2.Evaporator and Condensor pressure-Both evaporation and condensation pressures should be positive and near to atmospheric pressure but not too high.Easier detection of leaks is there due to positive pressures.
Eg.(i)R-134a - Evaporator pressure(Pe) at -15°C is 1.6397 and Condensor pressure(Pc) at same temperature is 7.7008,Pc/Pe=6.72
(ii)R-11 - Evaporator pressure(Pe) at -15°C is 0.2021 and Condensor pressure(Pc) at same temperature is 1.2607,Pc/Pe=6.24
Reciprocating compressor has low specific volumes and high operating pressures  while centrifugal has high specific volumes and low operating pressures.

3.LATENT HEAT OF VAPOURISATION- A refrigerant should have high latent heat of vaporization which leads to high refrigerating effect per kg of air and less mass circulation.
Eg.(i)R-12 has 116.5 KJ/Kg refrigerating effect for standard cycle of -15°C to 30°C.
(ii)R-717 has 1105.4 KJ/Kg refrigerating effect for standard cycle of -15°C to 30°C.
(iii)R-113 has 125.1 KJ/Kg refrigerating effect for standard cycle of -15°C to 30°C.

(4)Critical temperature and pressure-The highest temperature at which refrigerant is condensed to a liquid,irrespective of higher pressure.Critical temperature should be above highest condensing temperature.
Eg.(i)R-744 has critical temperature 31°C(<normal condensing temperature) and critical pressure 73.8 bar
(ii)R12 has critical temperature 112°C and critical pressure 41.2 bar.

PHYSICAL PROPERTIES OF A REFRIGERANT:-
(1)Thermal conductivity-Refrigerant in liquid and vapour states should have high value.Thermal conductivity is useful in finding heat transfer coefficients in Evaporators and condensors.Eg.(i)R-12 in vapour state has thermal conductivity 9.705×10^-3 W/mK at 30°C and in liquid state has thermal conductivity 0.0814 W/mK at 40°C.
(ii)R-22 in vapour state has thermal conductivity 11.784×10^-3 W/mK at 30°C and in liquid state has thermal conductivity 0.097 W/mK at 40°C.

(2)Corrosive property-Corrosive property is important while selecting refrigerant.Freon group of refrigerants are non-corrosive with almost every metal while Ammonia with only iron/steel.

(3)Viscocity-Refrigerant in liquid and vapour states should have low viscosity,which is better as pressure drops in passing through liquid and suction lines are small.Eg.(i)R-12 has Viscosity 0.328 at -15°C and 0.242 at 37.5°C in liquid state while 0.0114 at-15°C and 0.0136 at 30°C in vapour state.

(ii)R-22 has Viscosity 0.286  at -15°C and 0.223 at 37.5°C in liquid state while 0.0114 at-15°C and 0.0143 at 30°C in vapour state.

(4)-Dielectric strength-Relative dielectric strength of refrigerant is ratio of dielectric strength of nitrogen and refrigerant vapour mixture to dielectric strength of nitrogen at atmospheric pressure and room temperature.
Eg-R-11 has dielectric strength 3,R-22 has dielectric strength 1.31,R-744 has dielectric strength 0.88.
4/6/22, 6:39 PM - YUDHISHTER RANA Pec Mech: Q12
4/6/22, 6:40 PM - Yashwin: Yaar ismei which is more imp by giving specific examples ka ans nahi hai
4/6/22, 6:46 PM - Sagar: Data sahi hai mein galat hu
4/6/22, 7:22 PM - Sagar: 4(a)
4/6/22, 7:22 PM - Sagar: import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
df=pd.read_csv("/content/drive/MyDrive/regression.csv")
X = df.iloc[:,0 ].values
X = np.array(X)
X = X.reshape(len(X), 1)
Y = df.iloc[:,5 ].values
Y = np.array(Y)
Y = Y.reshape(len(Y), 1)
X_train = X[:80]
X_test  = X[80:]
Y_train = Y[:80]
Y_test  = Y[80:]
plt.scatter(X_test, Y_test, color = 'black')
plt.title('Test Data')
plt.show()
regr = linear_model.LinearRegression()
regr.fit(X_train, Y_train)
plt.plot(X_test, regr.predict(X_test), color = 'red', linewidth = 1)
plt.scatter(X_test, Y_test, color = 'black')
plt.show()
4/6/22, 7:23 PM - Sagar: <Media omitted>
4/6/22, 7:23 PM - Sagar: Code apne according change kr lena
4/6/22, 7:23 PM - Sagar: File name vagera
4/6/22, 7:36 PM - Sagar: x = df.iloc[:, 2:3].values
y = df.iloc[:, 5].values
x = np.array(x)
y = np.array(y)
from sklearn.linear_model import LinearRegression
lin = LinearRegression()
lin.fit(x, y)
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree = 2)
x_poly = poly.fit_transform(x)
poly.fit(x_poly, y)
lin2 = LinearRegression()
lin2.fit(x_poly, y)
plt.scatter(x, y, color = 'blue')
plt.plot(x, lin.predict(X), color = 'red')
plt.scatter(X, y, color = 'blue')
plt.plot(X, lin2.predict(poly.fit_transform(X)), color = 'red')
plt.show()
4/6/22, 7:36 PM - Sagar: 4(b) ka code
4/6/22, 7:36 PM - Sagar: yeh 90% sure hai
4/6/22, 9:30 PM - Ishroop: Q12???
4/6/22, 9:30 PM - Ishroop: Rac...
4/6/22, 9:33 PM - YUDHISHTER RANA Pec Mech: Specific examples ni mile as such
4/6/22, 9:34 PM - Ishroop: Kisi ne saare compile krke likh liye hain to bhejdo
4/6/22, 9:34 PM - Ishroop: Likhna asaan ho jaayega
4/6/22, 9:38 PM - YUDHISHTER RANA Pec Mech: Kal submission ki timings kya hain iski?
4/6/22, 9:38 PM - YUDHISHTER RANA Pec Mech: Rac ki assignment ki
4/6/22, 9:38 PM - Yashwin: Rac ki class
4/6/22, 9:38 PM - YUDHISHTER RANA Pec Mech: 2
4/6/22, 9:40 PM - YUDHISHTER RANA Pec Mech: It's been postponed at least till tomorrow
4/6/22, 9:41 PM - YUDHISHTER RANA Pec Mech: Atleast?
4/6/22, 9:41 PM - Gursharan Kaur✨: Yaar kl atd ka viva h kya??
4/6/22, 9:41 PM - YUDHISHTER RANA Pec Mech: Haan
4/6/22, 9:41 PM - Gursharan Kaur✨: 🤦‍♀️🤦‍♀️🥺🥺🥺
4/6/22, 9:42 PM - Gursharan Kaur✨: Kisiko kuchh ata ??
4/6/22, 10:03 PM - Ishroop: Wtf
4/6/22, 10:03 PM - Ishroop: Kaunsa viva bc
4/6/22, 10:03 PM - Ishroop: Acha file waala
4/6/22, 10:04 PM - Ishroop: Ek sec kal kya kya hai??
1. Atd prac file n viva
2. Rac assignment
Anything else???
4/6/22, 10:04 PM - Rohit Pec Mech: Aur kal 9:45 pe aa rahe hai na saare ?
4/6/22, 10:04 PM - Kshitiz Sharma Mech: Nope
4/6/22, 10:04 PM - Rohit Pec Mech: 9 ?
4/6/22, 10:04 PM - Kshitiz Sharma Mech: Sir ne kaha thaa agli class me jldi ana
4/6/22, 10:04 PM - Kshitiz Sharma Mech: Hnn
4/6/22, 10:04 PM - Rohit Pec Mech: Okok
4/6/22, 10:04 PM - Rohit Pec Mech: Theek hai
4/6/22, 10:04 PM - Ishroop: Yaar majorly sab pahunch jao on time
4/6/22, 10:05 PM - Ishroop: EK do log late bhi honge to koi scene nahi
4/6/22, 10:05 PM - Ishroop: Also atd file mein kitne practicals likhne????
4/6/22, 10:05 PM - Kshitiz Sharma Mech: 3 and layout
4/6/22, 10:05 PM - YUDHISHTER RANA Pec Mech: .
4/6/22, 10:05 PM - YUDHISHTER RANA Pec Mech: Iska bata do kuch
4/6/22, 10:06 PM - Sankalp Singla: Isse chodh abhi
4/6/22, 10:07 PM - Ishroop: Layout if atd only right???
4/6/22, 10:08 PM - Yashwin: <Media omitted>
4/6/22, 10:09 PM - Kshitiz Sharma Mech: This message was deleted
4/6/22, 10:09 PM - YUDHISHTER RANA Pec Mech: 👍👍
4/6/22, 10:11 PM - Kshitiz Sharma Mech: Hnn
4/6/22, 10:22 PM - Ishroop: Oki
4/6/22, 10:27 PM - Sagar: 11ques bhejna koi rac ki assignment ka
4/6/22, 10:28 PM - YUDHISHTER RANA Pec Mech: 8th bhi bhejna
4/6/22, 11:01 PM - Sagar: @916239579405 yaar tune bhejne the 5and 8
4/6/22, 11:01 PM - Sagar: 8 and 11
4/6/22, 11:19 PM - Ishroop: Book se hain wo direct
4/6/22, 11:19 PM - Ishroop: Legit topic ka naam hi wohi likha hai
4/6/22, 11:25 PM - Sagar: Ok
4/6/22, 11:49 PM - Shalin: <Media omitted>
4/6/22, 11:50 PM - Shalin: Compile krke assignment hai Ai/ML ki
4/6/22, 11:51 PM - Shalin: Khi se Mille the answers
Pta nhi kha se 😄😄
4/7/22, 8:56 AM - Gursharan Kaur✨: @everyone suno .....
Yaar koi bhi jaale sir ko ye mat bol dena k file check koge ya kuchh bhi ...
4/7/22, 8:56 AM - Shalin: 9:10-- 9:15  ke skte hai
traffic jam hai
4/7/22, 8:57 AM - Gursharan Kaur✨: Bs yahi bolna h k sir next exp krwa do
4/7/22, 8:57 AM - Ishroop: Bhai suno
4/7/22, 8:57 AM - Ishroop: Practical bahut peechey hain hamaare
4/7/22, 8:57 AM - Gursharan Kaur✨: Since baaki sbke 5 exp hogaye hain ...
4/7/22, 8:57 AM - Ishroop: Yess
4/7/22, 8:57 AM - Ishroop: Yesss
4/7/22, 8:58 AM - Gursharan Kaur✨: Aur jab rac lab aajaoge toh text krdena ..
4/7/22, 8:59 AM - Shalin: Ok
4/7/22, 9:25 AM - Yashwin: .
4/7/22, 12:45 PM - YUDHISHTER RANA Pec Mech: @918699133946 @919779772164 @919877113830 @919814484499 Jana hai aaj 4:30??
4/7/22, 12:46 PM - Sparsh Pec: Yess
4/7/22, 12:46 PM - Gursharan Kaur✨: Yup!!
4/7/22, 12:59 PM - Kshitiz Sharma Mech: <Media omitted>
4/7/22, 1:13 PM - Sagar: Yes
4/7/22, 1:39 PM - Shalin: Uniform nhi hai mere paas
To mera pta nhi
4/7/22, 1:42 PM - Gursharan Kaur✨: Compulsory nhi h aaj k liye uniform ..
4/7/22, 2:40 PM - Shalin: Ok thanks
4/7/22, 10:01 PM - Ishroop: Mv
4/7/22, 10:01 PM - Ishroop: Assignment
4/7/22, 10:01 PM - Ishroop: Anyone
4/7/22, 10:01 PM - Ishroop: Please
4/7/22, 10:01 PM - Ishroop: 😭
4/7/22, 10:01 PM - Ishroop: 😭
4/7/22, 10:01 PM - Ishroop: 😭
4/7/22, 10:01 PM - Ishroop: 😭
4/7/22, 10:01 PM - Ishroop: 😭
4/7/22, 10:17 PM - Gursharan Kaur✨: @919876326716 hui yaar assignment ??
4/7/22, 10:17 PM - Gursharan Kaur✨: @918054349284 @916239412997
4/7/22, 10:18 PM - Yashwin: Abhi start kari hai
4/7/22, 10:18 PM - Yashwin: Subah tak bhejdunga
4/7/22, 10:18 PM - Yashwin: Pls wait karlo
4/7/22, 10:19 PM - Kshitiz Sharma Mech: Same
4/7/22, 10:39 PM - Gursharan Kaur✨: Yaar jaise jaise krte jaoge saath saath mein bhejte rehna plzzzzz 🥲😭😭😭
4/7/22, 10:42 PM - Ishroop: +++
4/8/22, 7:44 AM - Ishroop: Bhejdo bc ab assignment
4/8/22, 7:45 AM - Ishroop: Please 😭😭😭
4/8/22, 7:51 AM - Ishroop changed the group description
4/8/22, 7:54 AM - Gursharan Kaur✨: ++++
4/8/22, 7:55 AM - Ishroop: Mujhe lag raha hum dono ke paas hi nahi hai. Ye saare complete krke beithe
4/8/22, 7:57 AM - Sparsh Pec: Teeno*
4/8/22, 7:57 AM - Gautam Pec: +1
4/8/22, 8:01 AM - Gursharan Kaur✨: +1
4/8/22, 8:03 AM - Shalin: Mere paas bhi nhi hai koi assignment
4/8/22, 8:04 AM - YUDHISHTER RANA Pec Mech: +1
4/8/22, 8:04 AM - Shalin: Please Send kr do
4/8/22, 8:04 AM - Gursharan Kaur✨: @919876326716 huyi assignment ?? 🥲🥲
4/8/22, 9:01 AM - Yashwin: Yaar starting ke kuch huye hai
4/8/22, 9:01 AM - Yashwin: College aakar fair karunga phir bhejta
4/8/22, 9:01 AM - Gursharan Kaur✨: Bhejde yaar fir .... 🥲
4/8/22, 9:02 AM - Yashwin: Raaste mei hu abhi
4/8/22, 9:02 AM - Gursharan Kaur✨: Okie okie cool  !
Aake bhejdio yaar
4/8/22, 9:41 AM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 9:41 AM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 9:41 AM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 9:41 AM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 9:41 AM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 9:41 AM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 10:23 AM - Gursharan Kaur✨: Baaki questions .. 🥲??
4/8/22, 10:23 AM - Gursharan Kaur✨: 1st k baad seedhe 12,13 .... 🥲🥲
4/8/22, 10:42 AM - YUDHISHTER RANA Pec Mech: Aur koi question?
4/8/22, 11:06 AM - Shalin: This message was deleted
4/8/22, 11:06 AM - Gursharan Kaur✨: Theek h na ye ??
4/8/22, 11:06 AM - Shalin: This message was deleted
4/8/22, 11:06 AM - Shalin: This message was deleted
4/8/22, 11:07 AM - Shalin: This message was deleted
4/8/22, 11:09 AM - Shalin: <Media omitted>
4/8/22, 11:09 AM - Shalin: <Media omitted>
4/8/22, 11:09 AM - Shalin: <Media omitted>
4/8/22, 11:09 AM - Shalin: Q2
4/8/22, 11:19 AM - Shalin: Tino page q2 ke hain
Glt to nhi lgra
4/8/22, 1:01 PM - Shalin: Q3
4/8/22, 1:01 PM - Shalin: <Media omitted>
4/8/22, 1:01 PM - Shalin: <Media omitted>
4/8/22, 1:01 PM - Shalin: <Media omitted>
4/8/22, 2:55 PM - YUDHISHTER RANA Pec Mech: Krre ho tum log submit?
4/8/22, 2:55 PM - YUDHISHTER RANA Pec Mech: Genuinely batana
4/8/22, 2:55 PM - Gursharan Kaur✨: Nhi
4/8/22, 3:12 PM - Kshitiz Sharma Mech: Maine krdi
4/8/22, 3:58 PM - Yashwin: ++
4/8/22, 3:58 PM - Gursharan Kaur✨: Dhokhebaaj ! 🥺🥺
4/8/22, 3:59 PM - Rohit Pec Mech: Bhai
4/8/22, 3:59 PM - Rohit Pec Mech: Bhejio zara
4/8/22, 3:59 PM - Rohit Pec Mech: <Media omitted>
4/8/22, 3:59 PM - Gursharan Kaur✨: Haan yaar ab itta sa toh krde @919876326716
4/8/22, 4:01 PM - Yashwin: Yaar jo ghoom rahi wohi hai
4/8/22, 4:01 PM - Yashwin: Kuch extra nahi kiya
4/8/22, 4:01 PM - Yashwin: 15 tak kiye hai
4/8/22, 4:01 PM - Gursharan Kaur✨: Wahi 4 question ??
4/8/22, 4:01 PM - Yashwin: Bhejta hup
4/8/22, 4:01 PM - Gursharan Kaur✨: Haan yaar plzzz 🥺
4/8/22, 4:03 PM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 4:03 PM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 4:03 PM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 4:03 PM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 4:03 PM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 4:03 PM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 4:03 PM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 4:03 PM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 4:03 PM - Kshitiz Sharma Mech: <Media omitted>
4/8/22, 4:12 PM - Gursharan Kaur✨: Thanks a lot yaar ..❤️‍🔥❤️‍🔥
4/10/22, 8:50 PM - Yashwin: Kal hai kya non teaching day
4/10/22, 8:50 PM - Yashwin: ?
4/10/22, 8:51 PM - Gursharan Kaur✨: Yaar most prolly nhi h ...
4/10/22, 8:51 PM - Gursharan Kaur✨: Jitta abhi tk pta chla h ...
4/10/22, 9:25 PM - YUDHISHTER RANA Pec Mech: Kal manufacturing ki practical file ki submission hai??
4/11/22, 10:29 AM - Yashwin: Karni hai bunk koi class
4/11/22, 10:29 AM - Yashwin: Abhi btado
4/11/22, 10:30 AM - Gursharan Kaur✨: Saari hi krlo yaar 😭😭😭😭😭
4/11/22, 10:30 AM - Ishroop: After rac koi nahi lagaani
4/11/22, 10:30 AM - Yashwin: Rac kyu lagani
4/11/22, 10:30 AM - Yashwin: Syllabus hojayega cover
4/11/22, 10:30 AM - Ishroop: Meri attendance ka scene hai
4/11/22, 10:30 AM - Gursharan Kaur✨: I m fucking tired ...yaar toh m toh ni attend krri ab ek bhi class
4/11/22, 10:30 AM - Gursharan Kaur✨: Prerna bhi ni aari
4/11/22, 10:30 AM - Ishroop: Moreover mujhe rac still interesting lagti
4/11/22, 10:31 AM - Ishroop: Agar class canceled krwa sakte fir koi scene nahi
4/11/22, 10:31 AM - Gursharan Kaur✨: Krwale yaar
4/11/22, 10:31 AM - Kshitiz Sharma Mech: Manu
4/11/22, 10:31 AM - Gursharan Kaur✨: Chli jaa pj k paas
4/11/22, 10:31 AM - Ishroop: Mein keise krwaau yaar
4/11/22, 10:31 AM - Yashwin: Yaar bullet train ki speed se chalti class
4/11/22, 10:31 AM - Ishroop: Kya bolungi sir ko 😂
4/11/22, 10:31 AM - Gursharan Kaur✨: ++
4/11/22, 10:31 AM - Gursharan Kaur✨: Athletics meet wala excuse
4/11/22, 10:31 AM - Gursharan Kaur✨: K sir sabhi thke huye hain
4/11/22, 10:32 AM - Gursharan Kaur✨: Bache bhut kam aaye hain
4/11/22, 10:32 AM - Yashwin: Rac ki nahi but manu ki karni na phir
4/11/22, 10:32 AM - Gursharan Kaur✨: Kya ??
4/11/22, 10:32 AM - Yashwin: Yaar saari bunk karlo
4/11/22, 10:33 AM - Yashwin: Bhot confusion hai 🥲
4/11/22, 10:33 AM - Gursharan Kaur✨: Yeasssss !!!
4/11/22, 10:33 AM - Gursharan Kaur✨: I agree
4/11/22, 10:33 AM - Gursharan Kaur✨: Kro saari bunk ...
4/11/22, 10:33 AM - Gursharan Kaur✨: Who all are up for mass bunk og f all the clasess ?
4/11/22, 10:34 AM - Ishroop: Sir wohi bolenge agar 1p se zyaada bache hue to wo class le lenge
4/11/22, 10:34 AM - Ishroop: 10*
4/11/22, 10:35 AM - Gursharan Kaur✨: Haan toh bs mechanchies pe we will text k koi mt aana
4/11/22, 10:41 AM - Shalin: Mech vibr ki class bunk ho rhi hai ??
4/11/22, 10:41 AM - Shalin: Ya wo lga rhe hai sbhi ??
4/11/22, 10:42 AM - Ishroop: Mass bunk hi krlo then
4/11/22, 10:45 AM - YUDHISHTER RANA Pec Mech: <Media omitted>
4/11/22, 10:45 AM - Shalin: Ok
4/11/22, 10:58 AM - Ishroop: <Media omitted>
4/11/22, 10:59 AM - Gursharan Kaur✨: Sbko maaro yaar belt se ..
4/11/22, 10:59 AM - Gursharan Kaur✨: Hadd hogayi h yaar ... 😭😭😭🥲🥲🥲
4/11/22, 10:59 AM - Ishroop: Me also attending ab
Miss krne ka point nahi
4/11/22, 11:01 AM - Ishroop: And abhi aur aa rahe hain itne
4/11/22, 11:01 AM - Gursharan Kaur✨: Aate raho yaar !!
4/11/22, 11:01 AM - Gursharan Kaur✨: Jo mrzi kro 😂
4/11/22, 3:09 PM - Sparsh Pec: Som lab aajao
4/11/22, 3:09 PM - Gursharan Kaur✨: Prac hoga ??
4/11/22, 3:09 PM - Gursharan Kaur✨: Ya attendance sake ...
4/11/22, 3:09 PM - Sparsh Pec: Prac shyad
4/11/22, 9:00 PM - Sagar: https://meet.google.com/qsr-ksih-mre
4/11/22, 9:00 PM - Sagar: @919814484499
4/11/22, 9:00 PM - Sagar: @917710715181
4/11/22, 9:00 PM - Sagar: @916239412997
4/11/22, 9:00 PM - Sagar: @919876326716
4/11/22, 9:00 PM - Sagar: @918146907246
4/11/22, 9:14 PM - Sparsh Pec: 🤔
4/11/22, 9:35 PM - Sagar: <Media omitted>
4/12/22, 9:48 AM - Sagar: @919814484499
4/12/22, 9:48 AM - Sagar: @917710715181
4/12/22, 9:48 AM - Sagar: @916239412997
4/12/22, 9:48 AM - Sagar: @919876326716
4/12/22, 9:48 AM - Sagar: @918146907246
4/12/22, 9:48 AM - Sagar: I m in L6
4/12/22, 10:50 AM - Shalin: Kha hai practical ??
4/12/22, 10:53 AM - Shalin: Mv ki ??
4/12/22, 10:54 AM - Ishroop: <Media omitted>
4/12/22, 10:54 AM - Ishroop: Class cancel
4/12/22, 10:59 AM - Sparsh Pec: Aaj to flash mob bhi h
4/12/22, 11:01 AM - Sagar: Hum sab toh neeche Wale room mein hain
4/12/22, 11:03 AM - Ishroop: Chodho
4/12/22, 11:03 AM - Ishroop: Kyo lagaana prac
4/12/22, 11:03 AM - Yashwin: Aaj tut hai
4/12/22, 11:49 AM - Sparsh Pec: <Media omitted>
4/12/22, 12:09 PM - Ishroop: Today’s lab will be conducted online as due to cab’s strikes in tricity I am not available in college.
4/12/22, 12:09 PM - Ishroop: Pls inform everyone
4/12/22, 12:09 PM - Ishroop: Will share the gmeet link with you at 3.
4/12/22, 12:09 PM - Ishroop: - ai/ml
4/12/22, 12:10 PM - Shalin: 🥳🥳
4/12/22, 1:26 PM - YUDHISHTER RANA Pec Mech: Kya scene hai ab fir is viva ka??
4/12/22, 1:27 PM - Yashwin: Pata nahi
4/12/22, 1:28 PM - Ishroop: Hola Peepss ,
We hope u enjoyed being clicked today at Meta Parking , be it a solo pic or with ur friends , it was indeed a fun.

But that's not all , the Branch photograph of all the years will be taking place tomorrow , the schedule for the same is shared along.

Hope to see u all !

For more queries please contact -
Abi: 7973653358
Kavya: 9915620695
Rhythm: 8728974200
4/12/22, 1:28 PM - Ishroop: *All Years:-*

Aerospace: 2 pm
Civil: 2:20 pm
Computer Science: 2:45 pm
Electrical: 3:10 pm
Electronics: 3:35 pm
Mechanical: 4 pm
Metallurgy: 4:25 pm
Production: 4:45 pm
4/12/22, 1:28 PM - Ishroop: Ai ml ke practical mein 3:30-3:45 pe bol dena ki maam class photo hai
4/12/22, 1:28 PM - Ishroop: Have to leave
4/12/22, 1:29 PM - Ishroop: Simple
4/12/22, 1:30 PM - YUDHISHTER RANA Pec Mech: Badhiya👍
4/12/22, 3:02 PM - Ishroop: To join the video meeting, click this link: https://meet.google.com/ues-rfxy-owf
Otherwise, to join by phone, dial +1 413-369-1287 and enter this PIN: 978 423 647#
4/12/22, 3:03 PM - Ishroop: Ai ml
4/12/22, 5:43 PM - Yashwin: <Media omitted>
4/12/22, 5:43 PM - Yashwin: <Media omitted>
4/12/22, 5:43 PM - Yashwin: <Media omitted>
4/12/22, 5:43 PM - Yashwin: <Media omitted>
4/12/22, 5:43 PM - Yashwin: <Media omitted>
4/13/22, 2:15 PM - Yashwin: <Media omitted>
4/13/22, 2:16 PM - Yashwin: The diagrams of these questions along with the ph plot need to be drawn before the next tut
4/13/22, 2:19 PM - Yashwin: <Media omitted>
4/13/22, 2:19 PM - Yashwin: <Media omitted>
4/13/22, 2:19 PM - Yashwin: <Media omitted>
4/13/22, 2:20 PM - Yashwin: <Media omitted>
4/13/22, 2:20 PM - Yashwin: <Media omitted>
4/13/22, 2:20 PM - Yashwin: <Media omitted>
4/13/22, 2:21 PM - Kshitiz Sharma Mech: <Media omitted>
4/13/22, 2:21 PM - Kshitiz Sharma Mech: <Media omitted>
4/13/22, 2:21 PM - Kshitiz Sharma Mech: <Media omitted>
4/13/22, 2:22 PM - Kshitiz Sharma Mech: <Media omitted>
4/13/22, 2:22 PM - Kshitiz Sharma Mech: <Media omitted>
4/19/22, 8:22 AM - YUDHISHTER RANA Pec Mech: Aaj koi scene to nahi hai na college ka?
4/19/22, 8:23 AM - Yashwin: Hona toh nahi chahiye
4/19/22, 9:43 AM - Rohit Pec Mech: Oe aaj aiml ki bt hai 3 baje wale me
4/19/22, 9:44 AM - Rohit Pec Mech: Ma'am ne pichli baar bhi yehi bolke gye theee ki jaisi attendance chalri hai us according agar tumne agla Tuesday nhi lagaya to issues honge
4/19/22, 9:45 AM - Yashwin: Kya karna phir
4/19/22, 9:45 AM - Rohit Pec Mech: Bhai chalte hai lab me
4/19/22, 9:46 AM - Rohit Pec Mech: Abhi mech vib rehnedo
4/19/22, 9:46 AM - Yashwin: Yaar ek class ki liye special aana padega
4/19/22, 9:46 AM - Rohit Pec Mech: MV wali bhi lagalio 2 baje
4/19/22, 9:47 AM - Yashwin: Meri attendance mv mei theek hai
4/19/22, 9:47 AM - Rohit Pec Mech: Okok
4/19/22, 9:50 AM - YUDHISHTER RANA Pec Mech: ++
4/19/22, 9:51 AM - Sagar: Agar 3  pm wali class lagani hai toh batado
Nahi toh mera off hai
4/19/22, 9:56 AM - Yashwin: ++
4/19/22, 9:57 AM - Yashwin: Ek baar baat karlo ma’am se
4/19/22, 9:57 AM - Yashwin: Ki kal raat ko bhot late khtm hua hai aaj majority nahi aayegi
4/19/22, 9:58 AM - Rohit Pec Mech: Hn ye kr skte ho to krlo
4/19/22, 9:59 AM - Yashwin: But karega kaun ??
4/19/22, 9:59 AM - Yashwin: <Media omitted>
4/19/22, 10:00 AM - YUDHISHTER RANA Pec Mech: Mam ka no. Hai kisipe?
4/19/22, 10:05 AM - YUDHISHTER RANA Pec Mech: Sankalp Singla
4/19/22, 10:05 AM - Yashwin: Dekho koi jaa rha toh abhi btadena
4/19/22, 10:06 AM - YUDHISHTER RANA Pec Mech: ++
4/19/22, 10:06 AM - Yashwin: No hard feelings
4/19/22, 10:07 AM - Rohit Pec Mech: Hn please
4/19/22, 10:08 AM - Sankalp Singla: <Media omitted>
4/19/22, 10:09 AM - YUDHISHTER RANA Pec Mech: Bhai Tera hi plan lagra mujhe😂😅
4/19/22, 10:13 AM - Rohit Pec Mech: Bhai mann bilkul nhi
4/19/22, 10:13 AM - Rohit Pec Mech: But jis way me ma'am boli thii to lagra hai jaana chahiye 😔
4/19/22, 10:13 AM - Rohit Pec Mech: Karlo koi baat fir nhi jayenge
4/19/22, 10:14 AM - Yashwin: Pichli baar tune hi kari thi
4/19/22, 10:14 AM - Yashwin: Karle phirse
4/19/22, 10:15 AM - Rohit Pec Mech: No. Nhi hai
4/19/22, 10:15 AM - Rohit Pec Mech: Wo to meet pe kri thi
4/19/22, 10:15 AM - Yashwin: Number kiske pass hai ?
4/19/22, 10:15 AM - Rohit Pec Mech: Apna aiml ka gr jo hai wo krlena
4/19/22, 10:15 AM - Rohit Pec Mech: Uske paas no. Hoga
4/19/22, 10:17 AM - Yashwin: @916239579405 ma’am se karlio baat
4/19/22, 10:33 AM - Yashwin: <Media omitted>
4/19/22, 10:33 AM - Yashwin: Yeh finance mei haal hai
4/19/22, 10:43 AM - Shalin: Practical lgegi mvbr ki ??
4/19/22, 10:43 AM - Shalin: 11 am ??
4/19/22, 10:43 AM - YUDHISHTER RANA Pec Mech: Koini jaara
4/19/22, 10:43 AM - Rohit Pec Mech: No
4/19/22, 10:43 AM - Rohit Pec Mech: Yes
4/19/22, 10:44 AM - Shalin: Fir rac lgegi ??
4/19/22, 10:44 AM - Shalin: 2 pm??
4/19/22, 10:44 AM - Rohit Pec Mech: No nhi jana
4/19/22, 10:44 AM - YUDHISHTER RANA Pec Mech: ++
4/19/22, 10:44 AM - Shalin: Fir mai college kyo aaya
😢😢
4/19/22, 10:45 AM - YUDHISHTER RANA Pec Mech: Koini waapis chala jaa
4/19/22, 10:45 AM - Shalin: Buss pe paise fuukk diye
🤣🤣
4/19/22, 10:46 AM - Shalin: Aaj ki class  cancel
Ok 😄
4/19/22, 10:48 AM - Priyanshu Mech: I might attend the classes because my attendance is short
4/19/22, 10:51 AM - Shalin: Ai/ml ki class ki timming ??
4/19/22, 10:53 AM - Gursharan Kaur✨: Bro !!!
Dont go ... 🥲
4/19/22, 10:58 AM - Yashwin: Maam se baat karlo
4/19/22, 10:58 AM - Yashwin: Pata chale same aisa haal ho
4/19/22, 10:59 AM - Ishroop: Listen
Aaj rehne dete hain jaana
4/19/22, 10:59 AM - Ishroop: Kisi bhi class mein
4/19/22, 10:59 AM - Ishroop: Mv prac mein ussne files check krni hongi.
4/19/22, 10:59 AM - Ishroop: So koi point nahi jaane ka
4/19/22, 11:00 AM - Ishroop: Mv ki class mein kum syllabus nhi ho rakha jo jaane ke plan bana rahe ho
4/19/22, 11:00 AM - Ishroop: And ai ml mass bunk kr lenge ye bol ke ki maam majority log ghar gaye hue thei
4/19/22, 11:01 AM - Yashwin: Done
4/19/22, 11:01 AM - Gursharan Kaur✨: And guys kal shayad atd ka bhi viva h .. 🥲toh accordingly prepare yourself ...
4/19/22, 11:01 AM - Yashwin: Aur yeh boldena bhot late info mila
4/19/22, 11:01 AM - YUDHISHTER RANA Pec Mech: Parson
4/19/22, 11:01 AM - Yashwin: Parso
4/19/22, 11:01 AM - YUDHISHTER RANA Pec Mech: ++
4/19/22, 11:02 AM - YUDHISHTER RANA Pec Mech: Koi ni laga raha class aaj
4/19/22, 11:02 AM - Sagar: Confuse mat kro yaar
4/19/22, 11:02 AM - Sagar: 9 bje se Lage pde ho jaana hai nahi jaana
4/19/22, 11:02 AM - YUDHISHTER RANA Pec Mech: Nahi jaana,final hai ab
4/19/22, 11:03 AM - Gursharan Kaur✨: ++
4/19/22, 11:04 AM - Gursharan Kaur✨: Nhi jaana meri jaan 😂
4/19/22, 11:04 AM - Gursharan Kaur✨: Tnsn na le
4/19/22, 11:04 AM - Sagar: Sabhi ka yeh final hai
Agar nahi hai toh bata do
And please might go jawab mat dena
4/19/22, 11:05 AM - Yashwin: Jinka confirm hai thumbs up kardo
Jisko jaana hai jaa sakta no hard feelings
4/19/22, 11:05 AM - YUDHISHTER RANA Pec Mech: Not going👍👍
4/19/22, 11:05 AM - Yashwin: 👍👍
4/19/22, 11:05 AM - Gursharan Kaur✨: 👍
4/19/22, 11:06 AM - Sagar: 👍 agar baki sab ka bhi thumbs up hai
4/19/22, 11:06 AM - Gautam Pec: 👍🏼
4/19/22, 11:06 AM - Ishroop: 👍🏻
4/19/22, 11:06 AM - Arihan Mech: 👍🏻
4/19/22, 11:08 AM - Shalin: 👍
4/19/22, 11:23 AM - Ishroop: Baaki???
4/19/22, 11:24 AM - Rohit Pec Mech: 👌
4/19/22, 11:26 AM - Kshitiz Sharma Mech: 👍
4/19/22, 11:30 AM - Sankalp Singla: 👍
4/20/22, 4:39 PM - Shalin: @ Group G1 STUDENTS: As already told to you, I am on leave from today to Friday. Therefore, lectures of Wednesday and Friday (this week) are postponed. HOWEVER, PRACTICAL CLASSES WILL BE HELD AS PER SCHEDULE.

With best wishes,
Mahesh Yadav
4/20/22, 4:39 PM - Shalin: Kl quiz to nhi hai ??
4/20/22, 4:40 PM - Shalin: Cancel honi chahiye ??
4/20/22, 5:42 PM - Yashwin: Ha kal nahi hoga viva phir shyd
4/20/22, 5:42 PM - Yashwin: but ek practical pada hai abhi
4/20/22, 5:42 PM - Yashwin: toh lga lena sab
4/20/22, 5:47 PM - Gursharan Kaur✨: Haan haan
4/20/22, 5:47 PM - Yashwin: Late jayenge
4/20/22, 5:47 PM - Yashwin: Sir toh hai nahi
4/20/22, 5:48 PM - Yashwin: toh 9;30 - 45 chal lenge
4/20/22, 5:48 PM - YUDHISHTER RANA Pec Mech: <Media omitted>
4/20/22, 5:48 PM - YUDHISHTER RANA Pec Mech: Iske baare bhi bata do kya kia jaaye
4/20/22, 5:49 PM - Yashwin: Padhlo phir quiz hai kal 🥲🥲🥲🥲🥲🥲
4/20/22, 5:49 PM - Yashwin: Mcq hogi
4/20/22, 5:50 PM - Yashwin: Ek baar CRs ko boldo sir se baat karle
4/20/22, 5:51 PM - Yashwin: Dono topics abhi tak khtm nahi hue hai
4/20/22, 5:51 PM - Yashwin: aur quiz ka format kaisa goga\
4/20/22, 5:51 PM - Yashwin: hoga
4/20/22, 5:52 PM - Gautam Pec: Objective nhi hoga, most probably one word/one line questions
4/20/22, 5:53 PM - Yashwin: Yaar woh theek hai programming mei dikkat hai 😞
4/20/22, 5:54 PM - Yashwin: uski bhi objective hogi ?
4/20/22, 5:54 PM - Gautam Pec: Uska idea nhi hai
4/20/22, 6:02 PM - Gursharan Kaur✨: Jaisa sa mid sems mein tha vaise ...
4/20/22, 6:03 PM - Gautam Pec: Yes
4/20/22, 8:36 PM - Ishroop: Cool
4/20/22, 8:37 PM - Ishroop: Kisi ne atd ke last experiment ka blank side waala part kr liya complete to please bhejdo
4/21/22, 9:03 AM - YUDHISHTER RANA Pec Mech: Kisi ke pass meri ATD ki file to nahi hai😬?
4/21/22, 9:11 AM - Gursharan Kaur✨: Yaar thora time se hi aajaan
4/21/22, 9:11 AM - Gursharan Kaur✨: Cz prac pe time lg jaata rac lab mein
4/21/22, 9:11 AM - Gursharan Kaur✨: 9:20 max chle jayenge lab mein
4/21/22, 9:28 AM - Gautam Pec: This message was deleted
4/21/22, 10:03 AM - Rohit Pec Mech: Konsi lab me ho ?
4/21/22, 10:03 AM - Gautam Pec: RAC
4/23/22, 9:15 AM - Shalin: This message was deleted
4/24/22, 7:13 PM - YUDHISHTER RANA Pec Mech: kisi ne agar last practical kar liya ho Manu ka to bhejdo
4/24/22, 7:14 PM - YUDHISHTER RANA Pec Mech: rapid prototyping wala
4/24/22, 7:48 PM - Ishroop: MV assignment kri hai kya kisi ne?????
4/24/22, 7:50 PM - Ishroop: @919876326716 ???
4/24/22, 7:50 PM - Yashwin: Na
4/24/22, 8:34 PM - Ishroop: And manu ka last practical???
4/24/22, 8:59 PM - Yashwin: Ppt se copy karli
4/24/22, 8:59 PM - Yashwin: Karlo
4/24/22, 8:59 PM - Yashwin: Meine nahi kia
4/24/22, 9:11 PM - Ishroop: And atd??
4/24/22, 9:12 PM - Yashwin: Meine kuch nahi kia mera finance ka project ka kaam chal rha
4/24/22, 9:12 PM - Ishroop: 🥲
4/24/22, 9:15 PM - YUDHISHTER RANA Pec Mech: Postpone nhi karwa sakte kya yaar dono assignment ko
4/24/22, 9:15 PM - Yashwin: Dekh meine group par bola tha
4/24/22, 9:15 PM - Yashwin: Tum log karo baat
4/25/22, 1:26 AM - Shalin: Ppt share  kr do exp 5 ki ??
4/25/22, 1:26 AM - Shalin: Manufac ??
4/25/22, 9:01 AM - Gursharan Kaur✨: Aaj ai ml mein kaun prhayega?
4/25/22, 9:01 AM - Gursharan Kaur✨: Sudesh ya mayank ??
4/25/22, 9:24 AM - Ishroop: 9:45 enter krne nahi dega na wo 🥲
4/25/22, 9:24 AM - Yashwin: Abhi tak toh karne dia baaki uska pata naho
4/25/22, 9:33 AM - Gursharan Kaur✨: Nhi krne dega
4/25/22, 9:33 AM - YUDHISHTER RANA Pec Mech: 10-11 bhi hai ai/ML ki?
4/25/22, 9:39 AM - Yashwin: Na
4/25/22, 9:39 AM - Yashwin: Honi toh nahi chahiye
4/25/22, 9:39 AM - Ishroop: Bhai assignment jugaadoo
4/25/22, 9:40 AM - Ishroop: N yaha bhejdo pleasee
4/25/22, 9:40 AM - Sparsh Pec: Viva h aaj ?🌝
4/25/22, 9:40 AM - Ishroop: Manu ka yes hai
4/25/22, 9:40 AM - Ishroop: But koi bolega nahi.
4/25/22, 9:40 AM - Ishroop: 😤😤😤😤
4/25/22, 9:40 AM - Ishroop: Ki sir viva lelo ya file collect krlo
4/25/22, 9:41 AM - Rohit Pec Mech: NO
4/25/22, 9:41 AM - Rohit Pec Mech: Kuch nhi hoga aaj
4/25/22, 9:41 AM - Rohit Pec Mech: Agar sir asked we all say ki PPT me busy thee sir
4/25/22, 9:41 AM - Rohit Pec Mech: To next week lelena
4/25/22, 9:50 AM - Gursharan Kaur✨: I dont think so ..
4/25/22, 9:50 AM - Gursharan Kaur✨: ++++
4/25/22, 9:52 AM - Gursharan Kaur✨: <Media omitted>
4/25/22, 10:11 AM - Gursharan Kaur✨: <Media omitted>
4/25/22, 10:30 AM - YUDHISHTER RANA Pec Mech: Yaar mujhe 1 baar personal baat karni pade shayad sir se
4/25/22, 10:31 AM - YUDHISHTER RANA Pec Mech: Ki agar ho viva ya kuch bhi to main baad mein de dun kyunki mujhse shayad zyada der shayad raha ni jaayega college mein
4/25/22, 1:36 PM - Yashwin: Manu ka prac aaj leave karna
4/25/22, 1:36 PM - Yashwin: ??
4/25/22, 1:36 PM - Yashwin: Sabki attendance almost complete hai
4/25/22, 1:36 PM - Sparsh Pec: Yess
4/25/22, 1:36 PM - Sparsh Pec: Mass bunk krte h
4/25/22, 1:36 PM - Yashwin: Ok
4/25/22, 1:36 PM - Ishroop: Meri confirm kr pehle
4/25/22, 1:37 PM - Sparsh Pec: Hnn thik h teri bhi
4/25/22, 1:37 PM - Yashwin: Teri 2 miss thi 5 mei se
4/25/22, 1:37 PM - Yashwin: Shyd
4/25/22, 1:37 PM - Ishroop: 🥲
4/25/22, 1:37 PM - Sparsh Pec: Nhi nhi 7 me se 2
4/25/22, 1:37 PM - Yashwin: Ha
4/25/22, 1:37 PM - Ishroop: In this case also... 75% to cross nhi hui
4/25/22, 1:37 PM - Sparsh Pec: Kamal sir short nhi krenge
4/25/22, 1:38 PM - Sparsh Pec: Class ki bhi add hongi
4/25/22, 1:38 PM - Gursharan Kaur✨: ++
4/25/22, 1:38 PM - Gursharan Kaur✨: ++
4/25/22, 1:38 PM - Yashwin: Me mohak kshitiz thinking of not attending
4/25/22, 1:38 PM - Gursharan Kaur✨: Yaar attendance short ni krega kk
4/25/22, 1:38 PM - Sankalp Singla: Ready
4/25/22, 1:38 PM - Yashwin: Sankalp also
4/25/22, 1:38 PM - Sparsh Pec: <Media omitted>
4/25/22, 1:41 PM - Ishroop: Agar koi nahi jaayega to even I won't go. No worries 😇
4/25/22, 1:42 PM - Gursharan Kaur✨: ,++
4/25/22, 1:42 PM - Gursharan Kaur✨: Agar koi jaara h toh btado
4/25/22, 1:42 PM - Gautam Pec: +1
4/25/22, 1:44 PM - YUDHISHTER RANA Pec Mech: Pakka,is hisaab se to ai/ML mein bhi koi dikkat nhi hai,kyunki uski labs mein 3 bunk hai humari
4/25/22, 1:44 PM - YUDHISHTER RANA Pec Mech: ?
4/25/22, 1:44 PM - Sparsh Pec: Hn hn koi scene nhii
4/25/22, 1:45 PM - YUDHISHTER RANA Pec Mech: <Media omitted>
4/25/22, 1:46 PM - Ishroop: Neri ek attendance hai
4/25/22, 1:46 PM - Ishroop: Also practicals mein shaayad alag se pass hona hota hai
4/25/22, 1:47 PM - Gursharan Kaur✨: Abe nhi bhenchod
4/25/22, 1:47 PM - Gursharan Kaur✨: Mayank bhi attendance short ni krt
4/25/22, 1:47 PM - Gursharan Kaur✨: Krta*
4/25/22, 1:48 PM - YUDHISHTER RANA Pec Mech: Monica mam ka koi scene to nhi padta na?
4/25/22, 1:48 PM - YUDHISHTER RANA Pec Mech: Sabhi ki short hai labs mein to
4/25/22, 1:49 PM - Gursharan Kaur✨: Nhi bro !!
4/25/22, 1:49 PM - Gursharan Kaur✨: ++
4/25/22, 1:49 PM - YUDHISHTER RANA Pec Mech: Bas badhiya fir to
4/25/22, 1:49 PM - YUDHISHTER RANA Pec Mech: <Media omitted>
4/25/22, 1:59 PM - Rohit Pec Mech: +++++
4/25/22, 1:59 PM - Rohit Pec Mech: To then we not going to the lab today ?
4/25/22, 1:59 PM - Sagar: Yes
4/25/22, 2:00 PM - Rohit Pec Mech: Perfect 👌
4/25/22, 2:24 PM - Gursharan Kaur✨: Anyone going to lab today ??
4/25/22, 2:24 PM - Yashwin: Me no
4/25/22, 2:25 PM - Gursharan Kaur✨: I m asking who is not going ..
4/25/22, 2:25 PM - Rohit Pec Mech: Nobody is going
4/25/22, 2:27 PM - Shalin: Mai bhi nhi jaa rha
4/25/22, 2:49 PM - Gursharan Kaur✨: Koi hai jo abhi bhi jaara h ?
4/25/22, 3:39 PM - Ishroop: Koi gaya hai kya???
4/25/22, 3:39 PM - Yashwin: Ha ghar 🌝😂
4/25/22, 4:45 PM - Shalin: Manufac ki practical file submit krni hai aaj ??
4/25/22, 4:45 PM - Shalin: Mtlb kiya hai sabne submit ??
4/25/22, 4:45 PM - Yashwin: Koi nhi kar rha submit
4/25/22, 4:45 PM - Shalin: Ok thanks
4/25/22, 10:16 PM - Shalin: Mv ke practical file me white page agr complete hai to please send kr do ??
4/25/22, 10:16 PM - Shalin: Ex 5 , Ex 6 and ,Ex 7
4/25/22, 10:16 PM - Shalin: ??
4/25/22, 10:21 PM - YUDHISHTER RANA Pec Mech: kal practical file ki submission hai confirmed?
4/25/22, 10:21 PM - Shalin: Pta nhi
4/25/22, 10:21 PM - Shalin: Mai affwa sunn rha hu
4/25/22, 10:22 PM - Shalin: Hope ye affwa ho
4/25/22, 10:22 PM - YUDHISHTER RANA Pec Mech: viva ka scene to nahi hai kal?
4/25/22, 10:29 PM - Gursharan Kaur✨: Yaar agar viva hoyega toh plz meko ek baar inform krdena koi bhi ..
Since i will be bzy tmrw ..and nhi aa paungi shayad lab mein .. 🥲
4/26/22, 7:50 AM - Arihan Mech: Ai ml ka practical lagana hai?
4/26/22, 8:08 AM - Ishroop: 🌚🌚🌚
4/26/22, 10:53 AM - Shalin: Mech vibr ki practical
4/26/22, 10:53 AM - Shalin: Pg block me hai ??
4/26/22, 10:53 AM - YUDHISHTER RANA Pec Mech: Aaj tut hai ya practical
4/26/22, 10:53 AM - YUDHISHTER RANA Pec Mech: ?
4/26/22, 10:57 AM - Shalin: Tut hai ??
4/26/22, 11:32 AM - Ishroop changed this group's settings to allow all participants to edit this group's info
4/26/22, 10:58 AM - Gursharan Kaur✨: Yaar jo bhi hoyega try krna k meri and ishroop ki attendance Lgwa dena
4/26/22, 10:58 AM - Gursharan Kaur✨: Since we are bzy with bdc
4/26/22, 11:00 AM - Ishroop: Mein lagwa dungi dw
4/26/22, 11:01 AM - Ishroop: Mujhe mana kr diya donate krne se 🥲
4/26/22, 11:05 AM - Priyanshu Mech: Mine too
4/26/22, 11:05 AM - YUDHISHTER RANA Pec Mech: .
4/26/22, 11:06 AM - Sparsh Pec: Meri bhi 👀
4/26/22, 11:07 AM - Arihan Mech: Koi Gaya hai?
4/26/22, 11:07 AM - Ishroop: +++
4/26/22, 11:07 AM - Ishroop: Bhai sabki nahi lagegi
4/26/22, 11:07 AM - Ishroop: Ye zaroor hai ki prac cancel krwa sakte
4/26/22, 11:08 AM - Ishroop: Bolke majority has gone for bdc
4/26/22, 11:10 AM - Ishroop: Btao bhaii
4/26/22, 11:11 AM - Ishroop: @918146907246 @919877113830 @916239902903
4/26/22, 11:11 AM - Ishroop: @919876326716 @919779772164
4/26/22, 11:11 AM - Ishroop: Bcc btaaoo
4/26/22, 11:12 AM - Ishroop: Sabko tag krna padega kya
4/26/22, 11:12 AM - Gursharan Kaur✨: Haan yaar yahiin pe hain .. 😂
4/26/22, 11:12 AM - YUDHISHTER RANA Pec Mech: Main college pahuncha nhi abhi
4/26/22, 11:13 AM - Ishroop: Bs theek hai
4/26/22, 11:13 AM - Ishroop: Camcel krwa rhe
4/26/22, 11:13 AM - YUDHISHTER RANA Pec Mech: Baakiyon se to puchle😂😂
4/26/22, 11:19 AM - Sparsh Pec: Hora h prac ?
4/26/22, 11:20 AM - Ishroop: Hn
4/26/22, 11:20 AM - Yashwin: Yes
4/26/22, 11:20 AM - Ishroop: Apparantly log saare beithe hue thei lab
4/26/22, 11:20 AM - Sparsh Pec: Kya hora h usme ?
4/26/22, 11:20 AM - Gursharan Kaur✨: Bhai attendance lgwa dio bs  .
4/26/22, 11:21 AM - Gursharan Kaur✨: 🥲
4/26/22, 11:21 AM - Ishroop: Nhi laga rha
4/26/22, 11:21 AM - Ishroop: Chandrakant hai
4/26/22, 11:21 AM - Sparsh Pec: Viva lera ?
4/26/22, 11:21 AM - Ishroop: Humne bola sir bdc ke liye jaana hai
4/26/22, 11:21 AM - Ishroop: Nhi
4/26/22, 11:21 AM - Ishroop: Next week
4/26/22, 11:21 AM - Sparsh Pec: File check ?
4/26/22, 11:21 AM - Ishroop: Wo kr rha hai
4/26/22, 11:32 AM - Ishroop: <Media omitted>
4/26/22, 11:35 AM - Ishroop changed the group description
4/26/22, 12:26 PM - Kshitiz Sharma Mech: <Media omitted>
4/26/22, 12:26 PM - Kshitiz Sharma Mech: <Media omitted>
4/26/22, 12:29 PM - Kshitiz Sharma Mech: <Media omitted>
4/26/22, 12:29 PM - Kshitiz Sharma Mech: <Media omitted>
4/26/22, 12:29 PM - Kshitiz Sharma Mech: <Media omitted>
4/26/22, 12:29 PM - Kshitiz Sharma Mech: <Media omitted>
4/26/22, 12:29 PM - Kshitiz Sharma Mech: <Media omitted>
4/26/22, 12:29 PM - Kshitiz Sharma Mech: <Media omitted>
4/26/22, 12:41 PM - Rohit Pec Mech: <Media omitted>
4/26/22, 12:41 PM - Rohit Pec Mech: <Media omitted>
4/26/22, 12:41 PM - Rohit Pec Mech: <Media omitted>
4/26/22, 1:20 PM - Yashwin: Viva mei bhot questions pooche the
4/26/22, 1:20 PM - Gursharan Kaur✨: Kaunsa viva ? 🥲
4/26/22, 1:20 PM - Yashwin: Tavish ne bataya ai/ml ke mei
4/26/22, 1:20 PM - Yashwin: Jab unka hua tha
4/26/22, 1:21 PM - Gursharan Kaur✨: Achha 🥲
4/26/22, 1:21 PM - Gursharan Kaur✨: Darao mat yaar kuchh ni aata mujhe ... 🥲🥲
4/26/22, 1:21 PM - Ishroop: Aaj nahi ja rhe thei hum yaar 🥲
4/26/22, 1:22 PM - Ishroop: Aise Mt kro ditch
4/26/22, 1:22 PM - Ishroop: Bahut kaam hai
4/26/22, 1:22 PM - Gursharan Kaur✨: Haan toh mt jaao 😂
4/26/22, 1:22 PM - Ishroop: Next week de denge viva
4/26/22, 1:22 PM - Ishroop: Tujhe nahi bol rhi
4/26/22, 1:22 PM - Ishroop: Tera pata hai mujhe
4/26/22, 1:22 PM - Yashwin: Ma’am se baat karlo
4/26/22, 1:22 PM - Yashwin: Jaana toh mujhe bhi nahi hai
4/26/22, 1:24 PM - YUDHISHTER RANA Pec Mech: ++
4/26/22, 1:38 PM - Yashwin: Mv ki lgani class ?
4/26/22, 1:49 PM - YUDHISHTER RANA Pec Mech: Viva ki taiyaari to ni krre na fir tum??
4/26/22, 1:55 PM - Gursharan Kaur✨: Bilkul nhi
4/26/22, 1:55 PM - YUDHISHTER RANA Pec Mech: Class ka kya karna fir?
4/26/22, 1:55 PM - Gursharan Kaur✨: Mass bunk 😂
4/26/22, 1:56 PM - YUDHISHTER RANA Pec Mech: Already bunk ho chuke hain kaafi
4/26/22, 1:56 PM - Gursharan Kaur✨: Yaar agar jaoge toh bol dena k gursharan toh bdc mein hai ..
4/26/22, 1:56 PM - YUDHISHTER RANA Pec Mech: Pehle hi khundak mein hai wo
4/26/22, 2:01 PM - Yashwin: Subah woh maana nahi tha iska toh bilkul idea nahi ki yeh maanegi ya nahi
4/26/22, 2:02 PM - YUDHISHTER RANA Pec Mech: Phir kya karna?
4/26/22, 2:03 PM - YUDHISHTER RANA Pec Mech: Tum free ho jaaoge 3 tak?
@918146907246 @917710715181 @919876326716 @916239412997
4/26/22, 2:04 PM - Kshitiz Sharma Mech: Hnn
4/26/22, 2:04 PM - Sparsh Pec: Yrr aaj skip krte h
4/26/22, 2:05 PM - Sparsh Pec: Next time prepare krke ayenge
4/26/22, 2:08 PM - Yashwin: Preparation toh tab bhi nahi honi 🥲
4/26/22, 2:11 PM - Gursharan Kaur✨: ++
4/26/22, 2:11 PM - Gursharan Kaur✨: ++ hopefully ..
4/26/22, 2:13 PM - YUDHISHTER RANA Pec Mech: Ek baar sab confirm kardo
4/26/22, 2:14 PM - Sparsh Pec: Confirm
4/26/22, 2:14 PM - Yashwin: I will go with majority
4/26/22, 2:14 PM - Sagar: Ai ml  bunk kr dete hai kisi aur class ka bhi ni hua viva
4/26/22, 2:15 PM - Arihan Mech: Let's not go...
4/26/22, 2:15 PM - Rohit Pec Mech: BT hogi mai keh raha hoon. Aaj ya to ma'am se baat karke next week karwado
4/26/22, 2:15 PM - Sparsh Pec: 🙌
4/26/22, 2:15 PM - Rohit Pec Mech: Agar wo chid gyi dikkat hogi
4/26/22, 2:15 PM - Rohit Pec Mech: Last wala bhi mass bunk thaa aiml lab
4/26/22, 2:15 PM - Sagar: Nahi baat kya krni yaar
Vo friendly ni hai
4/26/22, 2:15 PM - Yashwin: Ma'am se baat karlo
4/26/22, 2:16 PM - Sparsh Pec: ++
4/26/22, 2:16 PM - Sagar: Next week se dekh lenge
4/26/22, 2:17 PM - Sparsh Pec: ++
4/26/22, 2:17 PM - Yashwin: ma'am ko bolo ki  a lot of students have not come today and those who have come majority of them are in the bdc camp
4/26/22, 2:17 PM - Gautam Pec: ++
4/26/22, 2:17 PM - Yashwin: so if u could reschedule the class
4/26/22, 2:17 PM - Sparsh Pec: Maam se kuch baat nhi krni
4/26/22, 2:17 PM - Yashwin: Chal hatt samne aakar bol
4/26/22, 2:18 PM - Sparsh Pec: <Media omitted>
4/26/22, 2:18 PM - Sparsh Pec: Hn ab bol
4/26/22, 2:18 PM - Yashwin: <Media omitted>
4/26/22, 2:19 PM - Rohit Pec Mech: निर्लज्ज व्यक्ति
4/26/22, 2:19 PM - Yashwin: @918054349284 na ??
4/26/22, 2:19 PM - Rohit Pec Mech: Yes
4/26/22, 2:20 PM - Sparsh Pec: Bas hogae khush 😑🤦‍♂️
4/26/22, 2:20 PM - Yashwin: Very Very happy
4/26/22, 2:21 PM - Gursharan Kaur✨: Yaar final decision btao kya krna h ??
4/26/22, 2:21 PM - Gursharan Kaur✨: 🥲🥲
4/26/22, 2:21 PM - Yashwin: Apni class ke gr ko bolo pls baat karle phele
4/26/22, 2:21 PM - Yashwin: ki class reschedule kardo
4/26/22, 2:22 PM - Yashwin: As some of us are not present and some are busy in the bdc
4/26/22, 2:22 PM - Yashwin: pls yeh boldp
4/26/22, 2:22 PM - Yashwin: Aur abhi karlo
4/26/22, 2:24 PM - Sparsh Pec: To whomsoever it may concern..
Yrr mene just abhi blood donate Kiya h
Bhot weakness h body me
Mene bhot prepare kra h viva ke liye
But I don't have the strength to appear for it...
4/26/22, 2:24 PM - Yashwin: @916239579405 pls talk to ma'am
4/26/22, 2:24 PM - YUDHISHTER RANA Pec Mech: My answer is also the same,no difference
4/26/22, 2:25 PM - Rohit Pec Mech: <Media omitted>
4/26/22, 2:27 PM - Gursharan Kaur✨: Haatttt !!!
4/26/22, 2:27 PM - Yashwin: Yaar baat karle tu hi ma’am se
4/26/22, 2:28 PM - Gursharan Kaur✨: Meko ye hi ni pta k mam hai kaun 😂
4/26/22, 2:28 PM - Ishroop: Yaar mujhese mat bulwaao
4/26/22, 2:28 PM - Gursharan Kaur✨: Na mepe no. H mam ka ...
4/26/22, 2:28 PM - Ishroop: Koi aur teacher hota mein bol deti
4/26/22, 2:28 PM - Yashwin: GR tu hai yaar
4/26/22, 2:28 PM - Gursharan Kaur✨: Toh aur kaun bolega ??
4/26/22, 2:28 PM - Ishroop: Monika Maam Phd Aiml.vcf (file attached)
4/26/22, 2:28 PM - Gursharan Kaur✨: @916239579405 is gr
4/26/22, 2:29 PM - Ishroop: Bhai meine ek class lagaayi hai
4/26/22, 2:29 PM - Ishroop: Ussmein bhi ussne sunaaya hai mujhe
4/26/22, 2:29 PM - Ishroop: Ki application daalo ye wo etc etc
4/26/22, 2:29 PM - Gautam Pec: @919876326716 Tu hi baat karle 🙂
4/26/22, 2:29 PM - Ishroop: Jisne considerable classes lagaayi wo krlo baat
4/26/22, 2:31 PM - Yashwin: Same hi lagayi hai sabne classes
4/26/22, 2:31 PM - Ishroop: Meine 1 lagaayi hai bs
4/26/22, 2:31 PM - Ishroop: 😂😂😂😂
4/26/22, 2:40 PM - Gursharan Kaur✨: Mne 1 bhi ni 😂
4/26/22, 2:40 PM - Sagar: Baat rehne dete hai  krni
4/26/22, 2:41 PM - Sagar: Mass bunk hai
Agar sab ek sath hai toh koi problem ni hogi
4/26/22, 2:41 PM - Yashwin: Woh bhi theek hai but woh message daaldo maam ko aur gayab hojao
4/26/22, 2:42 PM - Sagar: Kya message
4/26/22, 2:42 PM - Gursharan Kaur✨: Yaar jo bhi krlo bs agar jaoge toh mera and priyanshu ka bol dena
4/26/22, 2:42 PM - Ishroop: And me
4/26/22, 2:42 PM - Ishroop: Wtf @918699133946
4/26/22, 2:42 PM - Ishroop: 😤😤😤😤
4/26/22, 2:42 PM - Gursharan Kaur✨: And ishroop
4/26/22, 2:43 PM - Ishroop: Thanku 😌❤️
4/26/22, 2:43 PM - Yashwin: Jo bola ma;am ko bolne ko
4/26/22, 2:48 PM - Gursharan Kaur✨: Tu hi krde na forward ...
4/26/22, 2:52 PM - Sagar: Karlo yaar bunk meine vaise bhi pehli baar bola hai
4/26/22, 2:53 PM - Gursharan Kaur✨: Haan yaar krlo 🔥🔥
4/26/22, 2:55 PM - Sagar: Agli baar se ni karenge koi
4/26/22, 2:55 PM - Sagar: Is baar krlo
4/26/22, 3:07 PM - Rohit Pec Mech: *this Thursday there will proper aiml lab 3-5. And viva of assignment 1 will also be conducted and after that no requests will be granted*
4/26/22, 3:07 PM - Rohit Pec Mech: Aaj wala cancel karwa diya
4/26/22, 3:08 PM - Rohit Pec Mech: No viva today
4/26/22, 3:11 PM - Yashwin: Pls also study clustering
4/26/22, 3:11 PM - Yashwin: Notebook file is on gcr
4/26/22, 3:15 PM - Ishroop: Bc
4/26/22, 3:15 PM - Ishroop: Thursday ko atd bhi hai 😭
4/26/22, 8:45 PM - Ishroop changed the group description
4/27/22, 2:09 PM - YUDHISHTER RANA Pec Mech: L7 mein aa jaao tut ke liye
4/28/22, 6:58 AM - Yashwin: Aaj lab late jaaye na ?
4/28/22, 7:14 AM - Shalin: Time decide kr ke bta dena
4/28/22, 7:41 AM - Gursharan Kaur✨: Yaar m toh L6 mein baith jaungi jaake jab bhi jaana hua lab mein bta dena ..
4/28/22, 7:47 AM - Yashwin: Ok
4/28/22, 7:49 AM - Gursharan Kaur✨: And we will try k mahesh k aane se pehle prac start hojaye
4/28/22, 7:49 AM - Gursharan Kaur✨: Taake uska viva yaad hi na aaye . 😂
4/28/22, 7:49 AM - Ishroop: 😂🥲
4/28/22, 7:50 AM - Ishroop: But yaar aaj wo kisi bhi haalat mein lega viva
4/28/22, 7:50 AM - Ishroop: Aaj poore g1 ka viva ho jaayega of sorts 🥲
4/28/22, 7:50 AM - Gursharan Kaur✨: Chup reh !
Gaali sunegi ab mese .gndi wali ..
4/28/22, 7:50 AM - Gursharan Kaur✨: <Media omitted>
4/28/22, 7:50 AM - Ishroop: Hamaara subha, m2 ka dopeher and m3 ka ig kal hi gaya
4/28/22, 7:50 AM - Ishroop: Ok me quiet 😂
4/28/22, 7:50 AM - Gursharan Kaur✨: Nhi hua M3 ka
4/28/22, 7:51 AM - Gursharan Kaur✨: And bc apna toh test bhi h hpcd ka 😭😭
4/28/22, 7:51 AM - Yashwin: Sir ko next week ka boldete 🌝
4/28/22, 7:51 AM - Gursharan Kaur✨: Lol!!
4/28/22, 7:51 AM - Ishroop: Bc kuch nhi aata usska mujhe
4/28/22, 7:51 AM - Gursharan Kaur✨: Baakio ka aata h ?? 😂
4/28/22, 7:51 AM - Ishroop: Kal hona unka
4/28/22, 7:51 AM - YUDHISHTER RANA Pec Mech: already 2 viva hai agle hafte🙂🙂
4/28/22, 7:51 AM - Yashwin: Same day toh nahi hai
4/28/22, 7:51 AM - Ishroop: I supposed tujhe isska answer pata hoga 🥲😂
4/28/22, 7:52 AM - YUDHISHTER RANA Pec Mech: Na
4/28/22, 7:52 AM - Ishroop: Hamaare aaj 3 hain
4/28/22, 7:52 AM - Gursharan Kaur✨: Ab 2 kaunse ?? 🥲
4/28/22, 7:52 AM - Yashwin: Aaj ai ml ka bhi hai
4/28/22, 7:52 AM - Ishroop: Ek din mein
4/28/22, 7:52 AM - Yashwin: Manu ka
Mv ka
4/28/22, 7:52 AM - YUDHISHTER RANA Pec Mech: Kal m2 ka Hua tha
4/28/22, 7:52 AM - Gursharan Kaur✨: Mv ka bhi hona ?
4/28/22, 7:52 AM - Yashwin: Mv ki quiz bhi honi
4/28/22, 7:52 AM - Gursharan Kaur✨: 3 kaunse ?? 😂
4/28/22, 7:52 AM - Ishroop: Bhai group description update kr diya kro
4/28/22, 7:53 AM - Yashwin: Aur ek tut sheet bhi hai
4/28/22, 7:53 AM - Yashwin: Mv ki
4/28/22, 7:53 AM - Ishroop: Atd, hpcd, aiml
4/28/22, 7:53 AM - Gursharan Kaur✨: Yaar bs kro
Bhut kuchh h .... 🥲🥲😭😭😭
4/28/22, 7:53 AM - Yashwin: Ab yeh hpcd kya hai
4/28/22, 7:53 AM - Ishroop: @919876326716 bro krde 🥲
4/28/22, 7:53 AM - Gursharan Kaur✨: Iske baad depression mein chli jaungi m ...
4/28/22, 7:53 AM - Ishroop: Oe hai hamaara
4/28/22, 7:53 AM - Ishroop: 😓😓😓
4/28/22, 7:53 AM - Yashwin: Ok
4/28/22, 7:53 AM - Gursharan Kaur✨: Bro hpcd ka written test h !!
4/28/22, 7:53 AM - Yashwin: Kal applied ki quiz hai 🙃
4/28/22, 7:53 AM - Gursharan Kaur✨: Agar uska viva hota toh kyya hi scene tha 😂
4/28/22, 7:53 AM - Ishroop: Diagrams hi nahi aate mujhe 🥲
4/28/22, 7:53 AM - Ishroop: Wtf
4/28/22, 7:54 AM - Ishroop: Wtf
4/28/22, 7:54 AM - Ishroop: Wtf
4/28/22, 7:54 AM - Ishroop: WTf
4/28/22, 7:54 AM - Ishroop: WTf
4/28/22, 7:54 AM - YUDHISHTER RANA Pec Mech: 🙂🙂
4/28/22, 7:54 AM - Ishroop: WTf
4/28/22, 7:54 AM - Gursharan Kaur✨: Haaye bhenchod !!
🤦‍♀️🤦‍♀️🤦‍♀️
4/28/22, 7:54 AM - Ishroop: Ye kab hua???
4/28/22, 7:54 AM - Ishroop: Tffff
4/28/22, 7:54 AM - Ishroop: Kal kyo hai quiz
4/28/22, 7:54 AM - YUDHISHTER RANA Pec Mech: Kal bataya tha🙂
4/28/22, 7:54 AM - Ishroop: Kab bola ussne
4/28/22, 7:54 AM - Gursharan Kaur✨: Kal hua tha ye 😂
4/28/22, 7:54 AM - Ishroop: Yaaarrrrrrrr
4/28/22, 7:54 AM - Ishroop: 😭😭😭
4/28/22, 7:54 AM - Gursharan Kaur✨: Mujhe theory bhi ni aati ..lol!
4/28/22, 7:54 AM - YUDHISHTER RANA Pec Mech: Kyunki college walon ki zindagi mein thrill ni hai,isliye humari lere
4/28/22, 7:54 AM - Gursharan Kaur✨: Koini bro vaise bhi kaunse hmne prepare krke hi jaana tha
4/28/22, 7:54 AM - Ishroop: Mujhe chapter ka naam bhi nahi para kya chal raha
4/28/22, 7:54 AM - Ishroop: 🥲🥲🥲🥲
4/28/22, 7:55 AM - Ishroop: Point
4/28/22, 7:55 AM - Ishroop: 😂😂😂
4/28/22, 7:55 AM - Gursharan Kaur✨: Shayad se ek pta h mujhe  .xd
4/28/22, 7:55 AM - Ishroop: Nhi mujhe nahi idea 🥲
4/28/22, 7:56 AM - Gursharan Kaur✨: Chl koini arpan toh h hi .. 😂🔥
4/28/22, 7:56 AM - Ishroop: 😂😂😂
4/28/22, 8:05 AM - Rohit Pec Mech: Pagal hai kya
4/28/22, 8:05 AM - Rohit Pec Mech: Sach bol ?????
4/28/22, 8:05 AM - Rohit Pec Mech: <Media omitted>
4/28/22, 8:07 AM - Shalin: Hpcd kya hai??
4/28/22, 8:08 AM - Rohit Pec Mech: Elective hai bhai
4/28/22, 8:09 AM - Shalin: Aacha hydaulic 🤔
4/28/22, 8:09 AM - Shalin: Ok ok
4/28/22, 8:13 AM - YUDHISHTER RANA Pec Mech: @919876326716 pattern kya hoga?
4/28/22, 8:13 AM - YUDHISHTER RANA Pec Mech: Bataya tha kuch?
4/28/22, 8:14 AM - Yashwin: Theoretical hoga
4/28/22, 8:14 AM - Yashwin: No mcq
4/28/22, 8:15 AM - YUDHISHTER RANA Pec Mech: 😳
4/28/22, 8:19 AM - Yashwin: Valve timing ka pdf bhejna ek baar pls
4/28/22, 9:00 AM - Sparsh Pec: Yrr me 10 bje aunga
4/28/22, 9:01 AM - Sparsh Pec: Sir ko bta dena
4/28/22, 9:04 AM - Shalin: 9:30 tk ruk skte hai
4/28/22, 9:04 AM - Shalin: ??
4/28/22, 9:05 AM - Shalin: Mtlb practical lgane 9:25- 9:30 pe ja skte hai ??
4/28/22, 9:16 AM - YUDHISHTER RANA Pec Mech: Abhi kahan ho tum log?
4/28/22, 9:18 AM - Gursharan Kaur✨: L6
4/28/22, 9:38 AM - Yashwin: <Media omitted>
4/28/22, 9:39 AM - Sparsh Pec: Viva lere ?
4/28/22, 9:46 AM - Gursharan Kaur✨: Haan 🥲
4/28/22, 9:46 AM - Yashwin: Haan
4/28/22, 9:46 AM - Ishroop: <Media omitted>
4/28/22, 9:46 AM - Yashwin: @916239412997 ka 5 min se chal rha
4/28/22, 9:50 AM - Gursharan Kaur✨: <Media omitted>
4/28/22, 10:33 AM - Kshitiz Sharma Mech: <Media omitted>
4/28/22, 10:33 AM - Kshitiz Sharma Mech: Atd exp 6
4/28/22, 10:55 AM - Ishroop: <Media omitted>
4/28/22, 11:53 AM - Yashwin: @916239579405 your file is with sir and he said that you have to give your viva today itself at any time in his office itself.
Aaj ke baad evaluation nhi karenge fir sir
4/28/22, 11:54 AM - Ishroop: Ok
4/28/22, 12:01 PM - Gursharan Kaur✨: Congo ! 😂🥲
4/28/22, 12:04 PM - Sparsh Pec: Kamal sir aagye ?
4/28/22, 12:04 PM - Rohit Pec Mech: Bunk karlo
4/28/22, 12:04 PM - Rohit Pec Mech: Bakwaas class hoti waise bhi
4/28/22, 12:04 PM - Rohit Pec Mech: Only neend aati
4/28/22, 12:04 PM - Gursharan Kaur✨: Haan yaar btado koi
4/28/22, 12:05 PM - Gursharan Kaur✨: Sb mein hi neend aati bs 🥲
4/28/22, 12:09 PM - Gautam Pec: L7 mein hain
4/28/22, 12:09 PM - Gursharan Kaur✨: Okie
4/28/22, 12:09 PM - Yashwin: Ok toh apni class nahi ho rahi ?0
4/28/22, 12:09 PM - Gautam Pec: Hamari hi hai
4/28/22, 12:10 PM - Yashwin: Combined hai ?
4/28/22, 12:11 PM - Ishroop: 3 to 5 mein bola sir ne
4/28/22, 12:11 PM - Ishroop: Ai ml jaldi dear nikal jaungi 😇
4/28/22, 12:12 PM - Yashwin: Same excuse mera bhi 😂
4/28/22, 12:14 PM - Gursharan Kaur✨: Main bhi yahi excuse maaroe niklungi 😂
4/28/22, 12:14 PM - Gursharan Kaur✨: Maarke*
4/28/22, 12:14 PM - Ishroop: Hatt bc 😂
4/28/22, 12:14 PM - Gursharan Kaur✨: Chupp reh !! 😂
4/28/22, 12:14 PM - Gursharan Kaur✨: You cant oppose me bb 😇😗
4/28/22, 12:18 PM - Ishroop: Bhai kya chal raha manu mein???
4/28/22, 12:18 PM - Gursharan Kaur✨: Assignment milri h
4/28/22, 12:33 PM - Yashwin: *IMPORTANT*
On wed 50 marks quiz will be there for Manufacturing in which MCQ type+ short ans+ fill in the blanks will be there.

On Thurs 20 marks quiz will be there for lab and file submission will be there. Quiz pattern will be same as above.

Submission for group project research is on Wed itself. Both hard copy and soft copy need to be prepared and submitted.
4/28/22, 12:33 PM - Yashwin: Baaki sab toh theek hai group project kya hai
4/28/22, 12:34 PM - Gautam Pec: Minimum 3000 words + diagrams, MS Word
1-6 Injection Moulding
10-15 Blow moulding
16-22 Helmet manufacturing
4/28/22, 12:35 PM - Yashwin: Yeh abhi btane ki baat thodi hoti
4/28/22, 12:35 PM - Yashwin: <Media omitted>
4/28/22, 12:41 PM - Yashwin: Yaar thoda elaborate kardo
4/28/22, 1:01 PM - Shalin: Group teacher  bnaege ya aapas me bnana hai ??
4/28/22, 1:05 PM - Yashwin: Yeh bangaye groups
4/28/22, 1:05 PM - Yashwin: Roll no wise
4/28/22, 1:06 PM - Ishroop: Ok
4/28/22, 5:52 PM - Rohit Pec Mech: kal ATD quiz ka syllabus kitna hai ?
4/28/22, 7:52 PM - Ishroop: Kal 2 baje ke baad to kuch nahi hai na hamaara???
4/28/22, 7:55 PM - Yashwin: Cdgc wala hai
4/28/22, 7:55 PM - Ishroop: Bund Mata gaya bc cdgc
4/28/22, 7:56 PM - Ishroop: Krna hi nahi jab cat MBA
4/28/22, 7:56 PM - Ishroop: 😑😑😑
4/28/22, 7:57 PM - Gursharan Kaur✨: Match bhi h 😂
4/29/22, 3:01 PM - Yashwin: Kaun kaun lga rha test aaj ka ?
4/29/22, 3:02 PM - Yashwin: Mba wala
4/29/22, 3:02 PM - Yashwin: Btado
4/29/22, 3:09 PM - Ishroop: Me to nhi laga rhi
4/29/22, 3:09 PM - Sparsh Pec: Kyuu 🌝
4/29/22, 3:09 PM - Yashwin: Mei bhi nahi
4/29/22, 3:12 PM - Sparsh Pec: Bhyii tumhe special bta rha hu ki mazak me mat lena
4/29/22, 3:12 PM - Ishroop: Bhai kya hai ye
4/29/22, 3:12 PM - Ishroop: 🥺🥺🥺
4/29/22, 3:12 PM - Ishroop: Nahi krna mba
4/29/22, 3:13 PM - Ishroop: Nahi dena cat
4/29/22, 3:13 PM - Ishroop: Baat khatam
4/29/22, 3:14 PM - Sparsh Pec: Yrr option nhi h
4/29/22, 3:14 PM - Sparsh Pec: Baki everything at your own risk
4/29/22, 3:14 PM - Ishroop: Theek hai
4/29/22, 3:14 PM - Ishroop: Mein nahi de rhi
4/29/22, 11:32 PM - Ishroop changed the group description
4/30/22, 10:52 AM - Ishroop changed the group description
4/30/22, 10:51 AM - Ishroop: Ai ml ka kaunsa viva hai Tuesday ko
4/30/22, 10:57 AM - YUDHISHTER RANA Pec Mech changed the group description
4/30/22, 10:52 AM - Ishroop: Iss Tuesday ho to gaya viva...
4/30/22, 10:58 AM - YUDHISHTER RANA Pec Mech changed the group description
4/30/22, 10:52 AM - Sankalp Singla: Tues ko chuti hai
4/30/22, 10:52 AM - Ishroop: Cool cool
4/30/22, 1:13 PM - Rohit Pec Mech: Manu file bhejna koi
4/30/22, 1:13 PM - Rohit Pec Mech: @919876326716
4/30/22, 10:34 PM - YUDHISHTER RANA Pec Mech: *IMPORTANT*
On wed 50 marks quiz will be there for Manufacturing in which MCQ type+ short ans+ fill in the blanks will be there.

On Thurs 20 marks quiz will be there for lab and file submission will be there. Quiz pattern will be same as above.

Submission for group project research is on Wed itself. Both hard copy and soft copy need to be prepared and submitted.
4/30/22, 10:35 PM - YUDHISHTER RANA Pec Mech: monday ko hai kya kuch manu ka?
4/30/22, 10:35 PM - Gursharan Kaur✨: I dont think so ..
4/30/22, 10:36 PM - YUDHISHTER RANA Pec Mech: koi confirmed bata do 1 baar
4/30/22, 10:36 PM - Gursharan Kaur✨: Kisi aur group ka hua h kya viva ?
4/30/22, 10:36 PM - Gursharan Kaur✨: Manu ka
4/30/22, 10:37 PM - Gursharan Kaur✨: Kamal sir ne toh class mein bhi yahi bola tha ..
But someone was saying k viva k liye gaurav sir ne kaha h ...
4/30/22, 10:37 PM - YUDHISHTER RANA Pec Mech: jab quiz hai to viva ki kya zaroorat
4/30/22, 10:38 PM - Gursharan Kaur✨: Main bhi wahi sochri thi ..
4/30/22, 10:38 PM - Gursharan Kaur✨: But @916239579405 teko gaurav sir ne bola h kya viva k liye ??
4/30/22, 10:38 PM - Yashwin: Viva hona hoga but kamal sir ke pass mujhe lag rha ab time nahi  viva lene ka
4/30/22, 10:39 PM - YUDHISHTER RANA Pec Mech: yaar ye quiz exam ke baad bhi kar sakte hain
4/30/22, 10:39 PM - YUDHISHTER RANA Pec Mech: jaise pichle end sem ke time kia tha
4/30/22, 10:41 PM - Ishroop: naa
4/30/22, 10:41 PM - Ishroop: main group pe puchlo ek baar
4/30/22, 10:41 PM - Ishroop: m2 ya m3 mein se bhi kisi ka tuesday hota ig
4/30/22, 10:41 PM - Gursharan Kaur✨: Bs fir monday ko kuchh ni h yaar manu ka ..
4/30/22, 11:52 PM - Shalin: File submission bhi nhi ??
4/30/22, 11:52 PM - Shalin: Yha to thrusday likha hai ??
4/30/22, 11:56 PM - Shalin: Monday ko manufac  ka kya kya hoega ??
4/30/22, 11:57 PM - Shalin: Ek baar final btado ??
5/1/22, 12:02 AM - Yashwin: Ismei do practicals hai dono likhne ?
5/1/22, 12:03 AM - Ishroop: na
5/1/22, 12:03 AM - Yashwin: Kaunsa likhna ?
5/1/22, 12:03 AM - Ishroop: sirf wo jo last time krwaaya tha rac lab mein
5/1/22, 12:04 AM - Shalin: ++
5/1/22, 12:04 AM - Shalin: ++
5/1/22, 12:05 AM - Yashwin: Pata nahi
5/1/22, 12:06 AM - Shalin: <Media omitted>
5/1/22, 12:06 AM - Shalin: To yeh confirm nhi hai ??
5/1/22, 12:09 AM - Shalin: Yrr (haan/na) type krne me 2 sec bhi nhi lgte
😅😅
5/1/22, 12:10 AM - Yashwin: Yaar kisi ko nahi pata
5/1/22, 12:10 AM - Yashwin: Pata hoga btadenge
5/1/22, 12:10 AM - Shalin: Ok thanks
5/1/22, 12:10 AM - Yashwin: Prepare karle hogaya toh dedio
5/1/22, 11:06 AM - You changed the group description
5/1/22, 11:30 AM - Shalin: Manufac ki 5th exp me jo photo lgani hai
5/1/22, 11:30 AM - Shalin: Machine ki
5/1/22, 11:30 AM - Shalin: Wo share kr do
5/1/22, 11:54 AM - Gursharan Kaur✨: Guys suno...
Abhi abhi kamal sir se bata huyi h
Sir ne bola h k manufacturing ka viva nhi hoga  ..
And bs quiz hoyegi vo bhi Thursday ko hi ...
5/1/22, 11:54 AM - Gursharan Kaur✨: Jis din file submission h ussi din ...
5/1/22, 11:54 AM - Rohit Pec Mech: okayy
5/1/22, 11:54 AM - Rohit Pec Mech: to file submission to kal hai ?
5/1/22, 11:54 AM - Gursharan Kaur✨: Abey nhi  .. 🤦‍♀️
5/1/22, 11:55 AM - Rohit Pec Mech: thik. got it :3
5/1/22, 11:55 AM - YUDHISHTER RANA Pec Mech: any info ki MV ki file submission kab hai?
5/1/22, 11:56 AM - Gursharan Kaur✨: Ideally tuesday hi honi chahiye but uss din holiday h .. 😂✌️
5/1/22, 11:56 AM - YUDHISHTER RANA Pec Mech: matlab ispe suspense hai abhi🙂
5/1/22, 11:56 AM - Gursharan Kaur✨: Obvio
5/1/22, 11:56 AM - Ishroop: Btw atd ka ek aur prac hua tha... file check ho chuki already.... so wo likhna to nahi na ab?
5/1/22, 11:58 AM - Gursharan Kaur✨: Likhna h yaar shayad se
5/1/22, 11:59 AM - Rohit Pec Mech: MV ke kitne lecture hogye hai abtak ?
5/1/22, 11:59 AM - Rohit Pec Mech: BC 15 lecture se kamm pe short hai MV me :(((
5/2/22, 11:22 AM - Ishroop changed the group description
5/2/22, 11:01 AM - Gursharan Kaur✨: Class h abhi rac ki ?
5/2/22, 11:01 AM - Yashwin: Pata nahi sir nahi aaye
5/2/22, 11:02 AM - Gursharan Kaur✨: Achha
5/2/22, 11:02 AM - Gursharan Kaur✨: Yaar agar sir aagaye toh bta dena
5/2/22, 11:03 AM - Yashwin: Aagaye
5/2/22, 11:21 AM - Ishroop: Manu ki file aaj check nahi honi na?
5/2/22, 12:57 PM - Sparsh Pec: Yrr if someone is near SOM lab...to vha pr Jake puchlo ki Manuf. Ka prac hoga ke nhii
5/2/22, 12:57 PM - Yashwin: @916239579405 puchle ek baar
5/2/22, 12:57 PM - Rohit Pec Mech: +1
5/2/22, 1:25 PM - Ishroop: M in sac
5/2/22, 1:25 PM - Ishroop: Khaana khaa rhi
5/2/22, 1:26 PM - Ishroop: Koi aur hai to puchlo warna 2 baje puch lenge
5/2/22, 1:59 PM - Yashwin: Manu file submission today
5/2/22, 2:00 PM - Sparsh Pec: Warm regards
Kamal sir
5/2/22, 2:01 PM - Shalin: Aaj file deni hai ??
5/2/22, 2:04 PM - Rohit Pec Mech: Wtfff
5/2/22, 2:04 PM - Rohit Pec Mech: Bhai ye ab kyu bata rahe
5/2/22, 2:04 PM - Rohit Pec Mech: BC Ghar aagya mai
5/2/22, 2:04 PM - Yashwin: Ruk hum baat kar rahe
5/2/22, 2:05 PM - Rohit Pec Mech: Karo bhai
5/2/22, 2:05 PM - Shalin: Manufac ki practical lgani hai ??
5/2/22, 2:05 PM - Yashwin: Tum karo direct baat
5/2/22, 2:06 PM - Shalin: Ya mass bunk hai ??
5/2/22, 2:06 PM - Rohit Pec Mech: Sir ka number dena
5/2/22, 2:06 PM - Yashwin: Ek baar call karlo sir ko
5/2/22, 2:06 PM - Rohit Pec Mech: .
5/2/22, 2:07 PM - Shalin: ++
5/2/22, 2:07 PM - Yashwin: +91 89011 05666
5/2/22, 2:09 PM - Rohit Pec Mech: Sir keh rahe hai ki file submission apne lab timings ke according hi hai. And Thursday ko tumhara lab quiz hai wo seperate hai
5/2/22, 2:09 PM - Rohit Pec Mech: Ek baar gaurav sir ka number dena koi
5/2/22, 2:09 PM - Rohit Pec Mech: Fast
5/2/22, 2:09 PM - Yashwin: But message mei kuch aur likha hai yeh toh bol
5/2/22, 2:09 PM - Rohit Pec Mech: Bola maineee
5/2/22, 2:09 PM - Yashwin: Woh toh kya matlab
5/2/22, 2:10 PM - Rohit Pec Mech: Sir kehte ki aaj check karwake khtm karo
5/2/22, 2:10 PM - Rohit Pec Mech: Thursday ko quiz hai lab ka
5/2/22, 2:10 PM - Yashwin: Bol sir file hi nahi laayr
5/2/22, 2:10 PM - Rohit Pec Mech: Maine bola ki sir message dekhke bachhe hi nhi aaye college
5/2/22, 2:10 PM - Rohit Pec Mech: Kehte ki dekhlo 5 baje tak karwalo check
5/2/22, 2:11 PM - Rohit Pec Mech: Mai to kehta koi 2 gaurav sir ko jaake ye sab smjhado aur boldo ki Wednesday ko check karwa denge sir
5/2/22, 2:11 PM - Yashwin: Kuch nahi hona
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: <Media omitted>
5/2/22, 2:13 PM - Yashwin: Photos ka print lelo
5/2/22, 2:14 PM - Yashwin: Double chali gayi hai
5/2/22, 2:18 PM - YUDHISHTER RANA Pec Mech: File mein chipkaane ka scene hai kya?
5/2/22, 2:23 PM - Sparsh Pec: Everybody in SOM lab at 2:30
5/2/22, 2:24 PM - Sankalp Singla: why???
5/2/22, 2:28 PM - Shalin: Sir ne bola hai
wed :Practical file submission and theory Quiz
5/2/22, 2:28 PM - Shalin: Thrus : Practical quiz
5/2/22, 2:28 PM - Rohit Pec Mech: Thanls
5/2/22, 2:28 PM - Rohit Pec Mech: Thanks
5/2/22, 2:29 PM - Shalin: Ok
5/2/22, 2:31 PM - Sparsh Pec: Jldi aajo
Attendance lgti h
5/2/22, 2:31 PM - Sparsh Pec: Lgti*
5/2/22, 2:31 PM - Rohit Pec Mech: Proxy lagade pls
5/2/22, 2:31 PM - Rohit Pec Mech: I'm at home
5/2/22, 2:35 PM - Sparsh Pec: Jldi aajo
Sir wait nhi krenge
5/2/22, 2:36 PM - Mohak Gandhi Pec: Aarha 1 min
5/2/22, 3:01 PM - Gursharan Kaur✨: Gaurav sir hain?
5/2/22, 3:04 PM - Sparsh Pec: Ab to nhi ptaa
5/2/22, 3:04 PM - Gursharan Kaur✨: 3 bje lab hoti h yaar 🤦‍♀️
5/2/22, 3:05 PM - Gursharan Kaur✨: 2 bje hi chle gaye the kya tum log ?
5/2/22, 3:05 PM - Ishroop: Bhai kya scene hai??
5/2/22, 3:05 PM - Ishroop: Lab hai ya nahi????
5/2/22, 3:06 PM - Ishroop: Also pichle 70 msgs mein kya tha???
5/2/22, 3:22 PM - Ishroop: Anyone
5/2/22, 3:22 PM - Ishroop: ...
5/2/22, 3:22 PM - Ishroop: Bta do b
5/2/22, 3:22 PM - Sparsh Pec: ..
5/2/22, 3:23 PM - Ishroop: Ab to ho gaye 3:30
5/2/22, 3:23 PM - Ishroop: Kya kru?
5/2/22, 3:23 PM - Sparsh Pec: Chill
5/2/22, 5:12 PM - Shalin: 2 cheez thi kaam ki
5/2/22, 5:12 PM - Shalin: Ek yeh
5/2/22, 5:12 PM - Shalin: Aur wo photos
5/2/22, 5:12 PM - Shalin: Jo @919876326716 ne send ki hain
5/2/22, 5:33 PM - Shalin: Aur bhi kuch ho skta hai
mughe nhi pta
5/2/22, 8:10 PM - Ishroop: Cool. Thanks
5/3/22, 9:02 AM - Gursharan Kaur✨: Yaar kisi ki mv ki file complete h ??
5/3/22, 10:11 AM - Ishroop: ++
5/3/22, 10:19 AM - Rohit Pec Mech: manu ka 5th practical hai kisipe ?
5/3/22, 10:48 AM - Yashwin: Mv ke viva kab hoga iski kuch khabar hai
5/3/22, 10:49 AM - Yashwin: Aur file submission
5/3/22, 12:27 PM - Ishroop changed the group description
5/3/22, 11:24 AM - Ishroop: Tuesday
5/3/22, 11:24 AM - Ishroop: Tuesday
5/3/22, 11:24 AM - Ishroop: ++
@919876326716 bro ye bhejde please
5/3/22, 11:30 AM - Yashwin: Tuesday aaj hai 🌝
5/3/22, 11:31 AM - Rohit Pec Mech: Happy Eid
5/3/22, 11:31 AM - Yashwin: Thodi der mei bhejta
5/3/22, 11:43 AM - Ishroop: Oh hn fuck 😂🥲
5/3/22, 3:04 PM - Yashwin: Atd ki quiz hogayi
5/3/22, 3:04 PM - Yashwin: Aur kitni quiz chahiye
5/3/22, 3:04 PM - Yashwin: Decription change
5/3/22, 3:42 PM - Ishroop: This message was deleted
5/3/22, 5:39 PM - Yashwin: Listen everyone
5/3/22, 5:40 PM - Yashwin: Kal by chance mv ka viva hota
5/3/22, 5:40 PM - Yashwin: Toh humei koi info nahi hai
5/3/22, 5:40 PM - Yashwin: Na sir ka message aaya hai
5/3/22, 5:41 PM - Yashwin: Kal already do quiz hai and file submission hai
5/3/22, 5:41 PM - Yashwin: No free time to take viva
5/3/22, 5:41 PM - Yashwin: Sir ko bolo friday ko lenge
5/3/22, 5:43 PM - Sagar: Ok
5/3/22, 5:44 PM - Yashwin: But still would recommend file lekar ana
5/3/22, 9:54 PM - Ishroop: Lab me bola tha
5/3/22, 9:54 PM - Ishroop: Class me bola tha
5/3/22, 9:54 PM - Ishroop: Ye hua hai kya???????
5/3/22, 9:56 PM - Rohit Pec Mech: A news for us too
5/3/22, 9:56 PM - Rohit Pec Mech: 😔
5/3/22, 9:56 PM - Yashwin: Hua kya hai
5/3/22, 9:56 PM - Ishroop: 6 practical hai manu ke apparantly
5/3/22, 9:56 PM - Ishroop: P.s. @919876326716
5/3/22, 9:57 PM - Yashwin: Yaar Gaurav ne uss din file dekh kar bola theek hai
5/3/22, 9:57 PM - Yashwin: Kya hai yeh 🥲
5/3/22, 9:57 PM - Rohit Pec Mech: Bs fir theek hai
5/3/22, 9:58 PM - Yashwin: Oye karle
5/3/22, 9:58 PM - Rohit Pec Mech: We don't need to follow others
5/3/22, 9:58 PM - Yashwin: Abhi time hai
5/3/22, 9:58 PM - Rohit Pec Mech: Apne gaurav sir badhiya hai
5/3/22, 9:58 PM - Rohit Pec Mech: He'll understand
5/3/22, 9:58 PM - Yashwin: Toh usne check nahi karni
5/3/22, 9:58 PM - Ishroop: Kal file kk ko deni
5/3/22, 9:58 PM - Ishroop: Gaurav sir ko nahi
5/3/22, 9:58 PM - Rohit Pec Mech: Kasam se theory ka kuch nhi padha. Ab wohi padhunga poori raat
5/3/22, 9:58 PM - Rohit Pec Mech: TF
5/3/22, 9:59 PM - Ishroop: Mujhe bhi padha do koi kuch
5/3/22, 9:59 PM - Rohit Pec Mech: 😩
5/3/22, 9:59 PM - Ishroop: 😓
5/3/22, 9:59 PM - Rohit Pec Mech: Ek 5 , 5 min ka video link hai
5/3/22, 9:59 PM - Rohit Pec Mech: Usme saare machining processes explained hai
5/3/22, 9:59 PM - Rohit Pec Mech: 😔
5/3/22, 9:59 PM - Ishroop: Bhejde please
5/3/22, 9:59 PM - Rohit Pec Mech: Full 1 unit
5/3/22, 9:59 PM - Rohit Pec Mech: Yeps bhejta
5/3/22, 10:00 PM - Ishroop: Kaunsa cutting waala na???
5/3/22, 10:00 PM - Rohit Pec Mech: https://youtube.com/playlist?list=PLWv6RLxuaVQwMg6kFEoeeMEGTWNnr7Jmr
5/3/22, 10:00 PM - Ishroop: Jismein merchant circle hai...
5/3/22, 10:00 PM - Rohit Pec Mech: Ye full ek unit hai
5/3/22, 10:00 PM - Rohit Pec Mech: All non conventional processes
5/3/22, 10:00 PM - Ishroop: Oh okay cool
5/3/22, 10:01 PM - Rohit Pec Mech: Baaki powder waali ki grp pe PDFs hai
5/3/22, 10:01 PM - Rohit Pec Mech: 😔😔
5/3/22, 10:01 PM - Rohit Pec Mech: And baaki dhoondh dhoondh ke padna net se
5/3/22, 10:01 PM - Ishroop: Yaar wo research paper kyo krne hai
5/3/22, 10:01 PM - Ishroop: Chutiye hain hum kya
5/3/22, 10:01 PM - Ishroop: 😑😑😑😑
5/3/22, 10:01 PM - Rohit Pec Mech: Not us. PEC 😭
5/3/22, 10:01 PM - Ishroop: Mech PhD waale krte hain research paper
5/3/22, 10:02 PM - Ishroop: Thanks a ton btw
5/3/22, 10:02 PM - Rohit Pec Mech: ✌️sabka vikaas
5/3/22, 10:24 PM - Ishroop: 6 hi hain na ???
5/3/22, 10:25 PM - Yashwin: Dekhlo saari machines ek baar
5/3/22, 10:26 PM - YUDHISHTER RANA Pec Mech: <Media omitted>
5/3/22, 10:27 PM - Ishroop: This message was deleted
5/3/22, 10:27 PM - Ishroop: Bas???
5/3/22, 10:27 PM - Ishroop: Aur to kuch nahi hai na kal?
5/3/22, 10:27 PM - Ishroop: This message was deleted
5/3/22, 10:27 PM - Ishroop: 12- manu quiz and viva and file
1:20 - ai ml quiz
+ project manu
+ sports proff
5/3/22, 10:27 PM - Sankalp Singla: Viva nhi hai
5/3/22, 10:28 PM - Ishroop: Viva in general hoga hi nahi???
5/3/22, 10:28 PM - Ishroop: Ya kal nahi hai???
5/3/22, 10:28 PM - Yashwin: Bhai kyu faaltu panic kar rahe
5/3/22, 10:28 PM - Yashwin: Kaunsa viva
5/3/22, 10:29 PM - Ishroop: Ok cool
5/3/22, 10:29 PM - Sankalp Singla: 4 bje hai
5/3/22, 10:30 PM - Ishroop: manu?
5/3/22, 10:30 PM - Sankalp Singla: Hn
5/3/22, 10:30 PM - Yashwin: Yes
5/3/22, 10:30 PM - Ishroop: cool
5/3/22, 10:30 PM - Ishroop: thanks
5/3/22, 10:47 PM - Ishroop: nahi kra na 6th prac perform humne????
5/3/22, 10:47 PM - Sankalp Singla: Na
5/3/22, 10:47 PM - Ishroop: bs
5/3/22, 10:47 PM - Ishroop: m1 se koi mt likho fir
5/3/22, 10:48 PM - Ishroop: jab krwaaya hi nahi to
5/4/22, 12:28 AM - Rohit Pec Mech: This message was deleted
5/4/22, 12:28 AM - Rohit Pec Mech: This message was deleted
5/4/22, 12:30 AM - Rohit Pec Mech: AiML k codes bhejde ek baar @919779772164
5/4/22, 5:01 AM - Sagar: Yaar sab codes classroom pe uploded hai
5/4/22, 12:28 PM - Gursharan Kaur✨: Yaar manu k prac ki dates pta hain kisi ko ??
5/4/22, 12:28 PM - Ishroop: +++
5/4/22, 12:29 PM - Rohit Pec Mech: Practical bhi hona hai . Tf ?
5/4/22, 12:29 PM - Ishroop: Dates as in practical kaunsa kis din hua tha
5/4/22, 12:29 PM - Ishroop: File mein likhni
5/4/22, 12:29 PM - Rohit Pec Mech: Ooo acha
5/4/22, 12:29 PM - Gursharan Kaur✨: Yuss !!
5/4/22, 12:29 PM - Gursharan Kaur✨: Konse nashe mein h tu ?? 😂
5/4/22, 12:30 PM - Rohit Pec Mech: Aajkal kaafi submissions ho rahi. Kuch unexpected bhi. Islie 😭
5/4/22, 12:30 PM - Ishroop: Zyaada padh liya issne
5/4/22, 12:30 PM - Gursharan Kaur✨: Yus ik 😂
5/4/22, 12:30 PM - Rohit Pec Mech: <Media omitted>
5/4/22, 1:34 PM - Gursharan Kaur✨: Guys suno
Hmaari mv ki file submission honi h and viva hona h either kal lunch break se pehle ya prso jab bhi
5/4/22, 1:34 PM - Gursharan Kaur✨: Sir ne kaha h k 2 hrs ka time chahiye sir ko
5/4/22, 1:34 PM - Yashwin: Parso
5/4/22, 1:34 PM - Yashwin: After mv quiz
5/4/22, 1:35 PM - Gursharan Kaur✨: Viva+ quiz+ file submission teeno kaam hone h
5/4/22, 1:40 PM - Yashwin: Parso hi karlo
5/4/22, 1:40 PM - Yashwin: Kal rac ki assignment bhi karni submit
5/4/22, 1:41 PM - Gursharan Kaur✨: 3-5 ??
5/4/22, 1:41 PM - Yashwin: 2-4??
5/4/22, 1:42 PM - Gursharan Kaur✨: 2-3 atd ki make up quiz h
5/4/22, 1:42 PM - Gursharan Kaur✨: But ek hi bnda h m1 mein se
5/4/22, 1:43 PM - Gursharan Kaur✨: Toh final krlo jaise bhi krna ..i will convey the msg to sir
5/4/22, 1:43 PM - Yashwin: Woh sir se baat karlega
Right @918054349284
5/4/22, 1:43 PM - Priyanshu Mech: I have viva
5/4/22, 1:44 PM - Gursharan Kaur✨: Yaar the thing is quiz bhi honi h
Toh sbko rukna hi pdega ...till the end ...
5/4/22, 1:44 PM - Gursharan Kaur✨: Kis subject ka ??
5/4/22, 1:44 PM - Priyanshu Mech: Ada
5/4/22, 1:45 PM - Gursharan Kaur✨: Decide kro yaar jaldi 😂
5/4/22, 1:45 PM - Gursharan Kaur✨: Sir k text aare hain 😂
5/4/22, 1:53 PM - Gursharan Kaur✨: Yaar suno ...
Final hogaya h...
2-4 sbka sort hojega accordingly
5/4/22, 1:53 PM - Gursharan Kaur✨: But saare 2 bje aajana vibrations ki lab mein
5/4/22, 1:53 PM - Gursharan Kaur✨: Except @918054349284
5/4/22, 1:53 PM - Gursharan Kaur✨: And ada walo ko 3 bje free krdenge
5/4/22, 8:02 PM - Rohit Pec Mech: RAC ki assignment hai to bhejdo pls
5/4/22, 8:18 PM - Ishroop: ++++
5/4/22, 8:56 PM - You changed the group description
5/4/22, 10:29 PM - Sankalp Singla: 9.30 aana na kl???
5/4/22, 10:31 PM - Yashwin: Jab marzi aao file hi check honi
5/4/22, 10:33 PM - Yashwin: Viva hoga phirse remaining ka
5/4/22, 10:33 PM - Yashwin: Yeh poocha hai
5/4/22, 10:33 PM - Yashwin: Abhi
5/4/22, 11:15 PM - Sparsh Pec: Ans kya aaya ?
5/4/22, 11:16 PM - Yashwin: Ans hai viva prepare karlo
5/4/22, 11:16 PM - Sparsh Pec: Yrr ye kya baat huii 🥲
5/4/22, 11:16 PM - Rohit Pec Mech: Konsa viva ?
5/4/22, 11:16 PM - Rohit Pec Mech: Kal kya kya hai
5/4/22, 11:16 PM - Rohit Pec Mech: RAC quiz + assignment
5/4/22, 11:16 PM - Gursharan Kaur✨: Mp lab quiz
5/4/22, 11:16 PM - Rohit Pec Mech: Manu ka practical quiz
5/4/22, 11:16 PM - Rohit Pec Mech: Aur
5/4/22, 11:16 PM - Sparsh Pec: That's not done @god
5/4/22, 11:17 PM - Rohit Pec Mech: Abey aur kya hai wo bata
5/4/22, 11:17 PM - Sparsh Pec: I'm done
5/4/22, 11:17 PM - Rohit Pec Mech: Ok
5/4/22, 11:17 PM - Sparsh Pec: Byee guys
5/4/22, 11:17 PM - Gursharan Kaur✨: Bye bye 😂
5/4/22, 11:18 PM - Rohit Pec Mech: MV ki file ke sath viva bhi hoga kya kal ?
5/4/22, 11:18 PM - Gursharan Kaur✨: Kal thori h prso h vo toh 🤦‍♀️
5/4/22, 11:19 PM - Rohit Pec Mech: F Mai faltu me baithke file complete Kari abhi 😩😩
5/4/22, 11:19 PM - Rohit Pec Mech: Ab dekha mai
5/5/22, 4:45 AM - Shalin: Rac ki quiz ??
5/5/22, 4:45 AM - Shalin: This message was deleted
5/5/22, 5:27 AM - Shalin: Ok pta chl gya
5/5/22, 5:29 AM - Shalin: Atd ka practical hoega ya sirf file check hogi ??
5/5/22, 5:33 AM - Yashwin: File check hogi aur baaki prac ka viva hoga
5/5/22, 5:51 AM - Shalin: Ok thanks mtlb atd ka prac nhi hoga ??
5/5/22, 7:13 AM - Ishroop: Last experiment ka lhs hai kisi pe any chance?
5/5/22, 7:16 AM - YUDHISHTER RANA Pec Mech: kitne time tak aana??
5/5/22, 7:18 AM - Ishroop: 9:30??
5/5/22, 7:26 AM - Sankalp Singla: Hn
5/5/22, 7:41 AM - Rohit Pec Mech: File to hamari checked hai na ?
5/5/22, 8:06 AM - Yashwin: Next two practicals
5/5/22, 8:19 AM - Ishroop: 2???
5/5/22, 8:19 AM - Ishroop: Ek hi to hai
5/5/22, 8:19 AM - Ishroop: Humidification dehumidification waala
5/5/22, 8:20 AM - Yashwin: 3 heat engine lab 3 rac
5/5/22, 8:20 AM - Ishroop: Total 6 practicals hai... jin mein se ek lab layout hai
5/5/22, 8:21 AM - Yashwin: Total 7 with lab layout
5/5/22, 8:21 AM - Ishroop: <Media omitted>
5/5/22, 8:21 AM - Ishroop: Kaunsa reh gaya?
5/5/22, 8:57 AM - Sparsh Pec: Yrr me late ho jaunga
5/5/22, 8:57 AM - Sparsh Pec: Sir ko bta dena
5/5/22, 8:58 AM - YUDHISHTER RANA Pec Mech: +++
5/5/22, 9:09 AM - Gautam Pec: ++
5/5/22, 9:10 AM - Ishroop: I will reach in 5 mins. Bol dungi sir ko ki tumlog bus ya cab se aa rahe and hence u guys r a little late
5/5/22, 9:10 AM - Ishroop: Cool??
5/5/22, 9:10 AM - Sparsh Pec: Hnn
5/5/22, 9:10 AM - Ishroop: Agar puchenge to ill give this explanation mtlb
5/5/22, 9:10 AM - Gursharan Kaur✨: Abhi lab jaari bc ?? 😂
5/5/22, 9:11 AM - Ishroop: Pec market thi
5/5/22, 9:11 AM - Ishroop: Mujhe practical likhna last waala abhi
5/5/22, 9:11 AM - Ishroop: Alag laude lage hain bc 🥲
5/5/22, 9:11 AM - Gursharan Kaur✨: Same !!
5/5/22, 9:11 AM - Ishroop: Yehi 3 hain na weise likhne waale
5/5/22, 9:12 AM - Gursharan Kaur✨: Rac wale 3 hain ??
5/5/22, 9:12 AM - Ishroop: <Media omitted>
5/5/22, 9:12 AM - Ishroop: @919876326716
5/5/22, 9:12 AM - Ishroop: .
5/5/22, 9:13 AM - Ishroop: @918699133946
5/5/22, 9:13 AM - YUDHISHTER RANA Pec Mech: Koi gaya hai lab abhi?
5/5/22, 9:13 AM - Ishroop: Jaane lagi thi... btaao na jaun?
5/5/22, 9:14 AM - Ishroop: Boldo bc warna ja rhi mein
5/5/22, 9:14 AM - Yashwin: Ha lab mei baithe hai
5/5/22, 9:14 AM - Yashwin: Sir nahi hai
5/5/22, 9:15 AM - Yashwin: L6 locked hai
5/5/22, 9:19 AM - Gursharan Kaur✨: Na ja 😂
5/5/22, 9:20 AM - Ishroop: <Media omitted>
5/5/22, 9:20 AM - Shalin: Hnn
5/5/22, 9:21 AM - Ishroop: Nahi krne 3 rac ke
5/5/22, 9:21 AM - Ishroop: 2 hi hain
5/5/22, 9:21 AM - Gursharan Kaur✨: Bc !!
5/5/22, 9:21 AM - Gursharan Kaur✨: 🥲
5/5/22, 9:21 AM - Gursharan Kaur✨: Thnk god !!
5/5/22, 9:27 AM - Shalin: Kaun se do
5/5/22, 9:27 AM - Shalin: Naam bta do
5/5/22, 9:28 AM - Shalin: Ya jo cancel hua hai uss  Exp ka naam bta do ??
5/5/22, 9:28 AM - Shalin: This message was deleted
5/5/22, 9:36 AM - Ishroop: *Attendance short (ATD):*
*(These guys to attend Friday class without fail)*
7006 (1 short)
7010 (1 short)
7016 (1 short)
7017 (3 short)
7019 (5 short)
5/5/22, 9:37 AM - Sparsh Pec: Or meri ?
5/5/22, 9:37 AM - Ishroop: Teri poori hai
5/5/22, 9:37 AM - Ishroop: Lab include krke
5/5/22, 9:47 AM - Ishroop: <Media omitted>
5/5/22, 9:47 AM - Ishroop: <Media omitted>
5/5/22, 9:53 AM - Rohit Pec Mech: On my way
5/5/22, 10:12 AM - Kshitiz Sharma Mech: <Media omitted>
5/5/22, 10:31 AM - Kshitiz Sharma Mech: <Media omitted>
5/5/22, 11:35 AM - Gursharan Kaur✨: This message was deleted
5/5/22, 11:36 AM - Rohit Pec Mech: Abey
5/5/22, 11:36 AM - Rohit Pec Mech: Ye lodu hai kya 😭
5/5/22, 11:36 AM - Rohit Pec Mech: Abhi to khtm hui lab bc
5/5/22, 11:36 AM - Gursharan Kaur✨: Are ruko 😂
5/5/22, 11:36 AM - Rohit Pec Mech: Oooo achaaaa waitt
5/5/22, 11:36 AM - Rohit Pec Mech: Wait
5/5/22, 11:36 AM - Rohit Pec Mech: Aaj 3-5 lab hai
5/5/22, 11:37 AM - Rohit Pec Mech: Jisme hamne nhi jaana hai
5/5/22, 11:37 AM - Rohit Pec Mech: Sir hamari attendance laga denge
5/5/22, 11:37 AM - Gursharan Kaur✨: Yups !
5/5/22, 1:10 PM - Ishroop: Please inform everyone that second lab viva is today at 3PM in CL5 as conveyed earlier in the previous lab.
5/5/22, 1:10 PM - Ishroop: Good afternoon maam
Maam we have a class from 3 to 5 today.
5/5/22, 1:10 PM - Ishroop: -Monika ai ml
5/5/22, 1:10 PM - Ishroop: Just keeping u guys posted
5/5/22, 1:10 PM - Ishroop: Also ye kab bola tha???
5/5/22, 1:12 PM - Gursharan Kaur✨: Wtf is wrong with her ?? 🤦‍♀️🤦‍♀️
5/5/22, 1:12 PM - Ishroop: Idk
5/5/22, 1:12 PM - Rohit Pec Mech: Not informed
5/5/22, 1:12 PM - Gursharan Kaur✨: Which class dude ??
5/5/22, 1:12 PM - Ishroop: Baaki kisi group ka hua bhi hai doosra viva???
5/5/22, 1:12 PM - Ishroop: Atd
5/5/22, 1:13 PM - Ishroop: .
5/5/22, 1:13 PM - Gursharan Kaur✨: Great great !!
5/5/22, 1:13 PM - Gursharan Kaur✨: Bs yahi bolo 😂
5/5/22, 1:13 PM - Gursharan Kaur✨: K viva h ussmein bhi 😂
5/5/22, 1:13 PM - Gursharan Kaur✨: And kal bhi ham free ni hain ...
5/5/22, 1:13 PM - Ishroop: Koi ek banda tho agar free hai to baat kr aao maam se
5/5/22, 1:13 PM - Yashwin: Ha ishroop baat karle
5/5/22, 1:13 PM - Gursharan Kaur✨: ++
5/5/22, 1:14 PM - Ishroop: <Media omitted>
5/5/22, 1:15 PM - Yashwin: Phir kal hi bol
5/5/22, 1:15 PM - Ishroop: Bhai meine krli baat. Usse weise hi mujh se khudas hai
5/5/22, 1:15 PM - Yashwin: Aaj toh nahi possible
5/5/22, 1:16 PM - Gursharan Kaur✨: Yaar kal mv ka bhi h na shaam ko ...
5/5/22, 1:16 PM - Ishroop: Tabhi I am saying baat kelo
5/5/22, 1:16 PM - Ishroop: Krlo*
5/5/22, 1:17 PM - Gursharan Kaur✨: Yaar ek kaam kr
5/5/22, 1:17 PM - Gursharan Kaur✨: Usko bol k kal 11-12 hi free hain ham bss
5/5/22, 1:17 PM - Gursharan Kaur✨: Vo bhi agar finance wale free hain toh ...
5/5/22, 1:18 PM - Gursharan Kaur✨: @919876326716 free ho na tum log ??
5/5/22, 1:20 PM - Yashwin: Ha
5/5/22, 1:20 PM - Yashwin: Koi problem nahi
5/5/22, 1:20 PM - Yashwin: Bas aaj nahi
5/5/22, 1:23 PM - Gursharan Kaur✨: Yaar bs fir mam ko bolo k one hour slot hi free h
5/5/22, 1:23 PM - Gursharan Kaur✨: 11-12
5/5/22, 1:23 PM - Gursharan Kaur✨: Kal
5/5/22, 1:24 PM - Yashwin: Aaj nahi hai
5/5/22, 1:24 PM - Gursharan Kaur✨: Toh kal dekhle vo apna ab...
5/5/22, 2:51 PM - Shalin: Aaj hai Ai/ml ka kuch
5/5/22, 2:51 PM - Shalin: 3 bje se ??
5/5/22, 3:33 PM - Ishroop: Nhi
5/5/22, 3:35 PM - Gursharan Kaur✨: @919467734085 yaar sir se poochh le ek baar k attendance leni h kya sir ne abhi ??
5/5/22, 5:56 PM - You changed the group description
5/5/22, 6:22 PM - Rohit Pec Mech: Kal ATD ki theory quiz hai ?
5/5/22, 6:22 PM - Rohit Pec Mech: Ye kab hua
5/5/22, 6:23 PM - Yashwin: Nahi sirf jinki miss hui thi
5/5/22, 6:23 PM - Rohit Pec Mech: To description se hatao 😩
5/5/22, 6:23 PM - Yashwin: Meine nahi daali 🌝
5/5/22, 6:23 PM - Rohit Pec Mech: Means kal only MC quiz and practical submission hai na
5/5/22, 6:23 PM - Rohit Pec Mech: MV
5/5/22, 6:23 PM - Yashwin: Ha aur practical ka viva
5/5/22, 6:23 PM - Rohit Pec Mech: Yess
5/5/22, 6:24 PM - Rohit Pec Mech: Tomorrow only MC day
5/5/22, 6:24 PM - Rohit Pec Mech: MV
5/5/22, 10:08 PM - Kshitiz Sharma Mech: Timings?
5/5/22, 10:09 PM - Yashwin: Mujhe maaf karde mei so rha mujhe nahi pata
5/5/22, 10:09 PM - Yashwin: <Media omitted>
5/5/22, 10:09 PM - Rohit Pec Mech: <Media omitted>
5/5/22, 10:09 PM - Kshitiz Sharma Mech: Gn
5/5/22, 10:10 PM - Yashwin: <Media omitted>
5/5/22, 10:14 PM - Gursharan Kaur✨: Kal mv theory quiz ki timing is 10:15 am
Iske baad shayad lab quiz bhi h ... 🥲
Ai ml viva 11am to 12 pm
Uske baad
Mv ki file submission, viva and most prolly lab quiz 2 to 4
5/5/22, 10:16 PM - Yashwin: Ai ml ka viva nahi ho sakta apni lab quiz hai 🌝 yeh baat ma’am ko nahi pata
5/5/22, 10:17 PM - Ishroop: <Media omitted>
5/5/22, 10:17 PM - Gursharan Kaur✨: Yaar ig @916239579405 ne baat krli h mam se
K kal hoga viva .. 😂
5/5/22, 10:17 PM - Ishroop: Hn hn
5/5/22, 10:17 PM - Ishroop: Btaya to tha 5 baje
5/5/22, 10:17 PM - Ishroop: Dh mein
5/5/22, 10:18 PM - Gursharan Kaur✨: And aaj kyu nhi bola tune ye @919876326716 when we were discussing k kya krna h ai ml viva ka ..
5/5/22, 10:18 PM - Gursharan Kaur✨: 🥲
5/5/22, 10:18 PM - Yashwin: Kab kiya discuss bta toh dete 🥲
5/5/22, 10:18 PM - Ishroop: .
5/5/22, 10:18 PM - Ishroop: .
5/5/22, 10:18 PM - Ishroop: .
5/5/22, 10:18 PM - Gursharan Kaur✨: Group pe hi discussiok hoti h yaar saari 🥲
5/5/22, 10:19 PM - Yashwin: Tab nahi thi but agar mv ki quiz kal lambi chali gayi
5/5/22, 10:19 PM - Yashwin: Toh nahi dete viva
5/5/22, 10:19 PM - Yashwin: 😂
5/5/22, 10:19 PM - Gursharan Kaur✨: 😂😂😂
5/5/22, 10:19 PM - Gursharan Kaur✨: Can work !! 😂🔥🔥
5/5/22, 10:20 PM - Ishroop: 😂😂😂😂
5/6/22, 7:56 AM - Ishroop: @919876326716 @916239412997 yaar mv ke exp 5 6 7 ki blank sides bhejdo ek baar please 😭
5/6/22, 7:59 AM - Rohit Pec Mech: Kitne baje submit karni hai file
5/6/22, 8:00 AM - Yashwin: Mei nikal rha college ke liye abhi college mei dekhlio
5/6/22, 8:00 AM - Yashwin: 2 bje ?
5/6/22, 8:01 AM - Rohit Pec Mech: Perfect
5/6/22, 8:08 AM - Ishroop: Ok
5/6/22, 8:08 AM - Ishroop: File 3 se 5 practical ke time nahi honi submit?
5/6/22, 8:08 AM - Yashwin: 2-4 hai
5/6/22, 8:09 AM - Ishroop: Okk
5/6/22, 8:12 AM - Yashwin: Viva dena hai ai/ml ka
5/6/22, 8:12 AM - Yashwin: Sab decision le lena
5/6/22, 8:13 AM - Rohit Pec Mech: Nooo
5/6/22, 8:14 AM - Yashwin: Phir sabka no hona chahiye
5/6/22, 8:18 AM - Gursharan Kaur✨: 2 to 4*
5/6/22, 8:18 AM - Ishroop: Zero laga degi wo
5/6/22, 8:18 AM - Ishroop: Kya faayda
5/6/22, 8:18 AM - Ishroop: Oki
5/6/22, 8:19 AM - Gursharan Kaur✨: Meko koi scene ni h
Dekhlo agar koi ni jayega toh m bhi ni jaungi
Agat joage viva dene toh m bhi chli jaungi ...
5/6/22, 8:19 AM - Yashwin: Waise clustering aur classification kisko aati hai
5/6/22, 8:19 AM - Yashwin: 🥲
5/6/22, 8:19 AM - Yashwin: Theory nahi code
5/6/22, 8:22 AM - Yashwin: Baaki groups ka hua viva
5/6/22, 8:22 AM - Yashwin: ??
5/6/22, 8:25 AM - Ishroop: Hn m3 ka hua ig
5/6/22, 8:25 AM - Yashwin: M2 ka nahi hua phir hum kyu de 🌝
5/6/22, 8:26 AM - Ishroop: 🥲
5/6/22, 8:26 AM - Ishroop: Mere to weise bhi nahi lagne marks viva mein ai ml ke.
5/6/22, 8:26 AM - Ishroop: So for me to na jaao hi better 😂
5/6/22, 8:37 AM - Gursharan Kaur✨: Yes
5/6/22, 8:37 AM - Gursharan Kaur✨: ++
5/6/22, 8:37 AM - Yashwin: M5 ka bhi nahu hua
5/6/22, 8:37 AM - Gursharan Kaur✨: Haan yaar ik 😭
5/6/22, 9:14 AM - Rohit Pec Mech: @919876326716  kahan hai ?
5/6/22, 9:15 AM - Yashwin: Ghar pe
5/6/22, 9:16 AM - Rohit Pec Mech: Tu to kehra thaa nikal gaya college k lie
5/6/22, 9:17 AM - Yashwin: <Media omitted>
5/6/22, 9:17 AM - Yashwin: Nikla hua gu
5/6/22, 9:17 AM - Yashwin: Hu*
5/6/22, 9:17 AM - Rohit Pec Mech: Okok 😂
5/6/22, 10:50 AM - Ishroop: Venue for viva:
5/6/22, 10:50 AM - Ishroop: Phd scholar’s lab
5/6/22, 10:50 AM - Ishroop: New academic block, 1st floor
5/6/22, 10:50 AM - Ishroop: Kya scene hai????
5/6/22, 10:51 AM - Gursharan Kaur✨: Chlna saalo ??
5/6/22, 11:08 AM - Ishroop: Btaa do @919478379030
5/6/22, 11:08 AM - Ishroop: @918054349284
5/6/22, 11:08 AM - Ishroop: @919876326716
5/6/22, 11:08 AM - Ishroop: @916239412997
5/6/22, 11:08 AM - Ishroop: Kyaa scene
5/6/22, 11:18 AM - Gursharan Kaur✨: Guys abhi k liye Monika mam ne bola h k she will talk to mayank sir
5/6/22, 11:23 AM - Rohit Pec Mech: Yes
5/6/22, 11:23 AM - Gursharan Kaur✨: And will let us know
5/6/22, 11:23 AM - Rohit Pec Mech: Aaj no viva of AiML
5/6/22, 11:23 AM - Rohit Pec Mech: It will be rather on the same day of exam , ya if there is any other info she'll inform us after talking to Mayank sir
5/6/22, 11:24 AM - Ishroop: Cool
5/6/22, 1:48 PM - Shalin: 2-4 file submission hai
viva bhi hai
5/6/22, 1:48 PM - Shalin: Kha pe hai ??
5/6/22, 1:54 PM - Yashwin: Everyone TOM lab aao
5/6/22, 1:54 PM - Yashwin: Asap
5/6/22, 1:55 PM - Sparsh Pec: Mera quiz h atd ka
5/6/22, 1:55 PM - Sparsh Pec: Btadena sir ko
5/6/22, 1:55 PM - Ishroop: Mein aa rahi asap
5/6/22, 1:56 PM - Yashwin: Quiz hai abhi
5/6/22, 1:57 PM - Gursharan Kaur✨: Hn hh tnsn na le
5/6/22, 2:03 PM - Yashwin: 2 min mei aajao
5/6/22, 2:03 PM - Gursharan Kaur✨: Yuss !!
5/6/22, 2:03 PM - Gursharan Kaur✨: Jaldi aajao yaar ..
5/6/22, 2:03 PM - Yashwin: Quiz start ho rahi
5/7/22, 9:30 AM - Yashwin: Jo refrigerants waali assignment karri thi uska pdf bnaya kisi ne ?
5/8/22, 11:23 AM - Shalin: Mv ka syllabus kha milega ??
5/8/22, 11:23 AM - Shalin: Ya koi send kr do ??
5/8/22, 11:24 AM - Shalin: Handout ??
5/8/22, 11:27 AM - Gursharan Kaur✨: <Media omitted>
5/8/22, 11:32 AM - Shalin: Ok thanks
5/10/22, 12:31 PM - Ishroop: Apna viva nahi hona 😂🥲
5/10/22, 12:31 PM - Ishroop: ????
5/10/22, 12:34 PM - Yashwin: Dekh koi info toh aaya nahi
5/10/22, 12:34 PM - Gursharan Kaur✨: Obvio nhi
5/10/22, 12:34 PM - Gursharan Kaur✨: Jab btaya hi ni usne
5/10/22, 12:37 PM - Yashwin: Puchlo ek vaar
5/10/22, 12:37 PM - Yashwin: Varna boldenge
5/10/22, 12:37 PM - Yashwin: Nahi btaya
5/10/22, 12:41 PM - Yashwin: Dekho humei nahi inform kara
5/10/22, 12:41 PM - Yashwin: Mei ghar jaa rha
5/10/22, 12:42 PM - Shalin: Ghr chalo
5/10/22, 12:44 PM - Yashwin: Ma’am ko boldena paper khtm hote hi ghar chale gaye as no info was given
5/10/22, 2:30 PM - Ishroop: Hn
5/10/22, 2:30 PM - Ishroop: Weise pucha jhi ussne
5/10/22, 2:30 PM - Ishroop: So mein khudse kuch nhi bol rhi
5/11/22, 12:59 PM - Ishroop: Venue for viva:
5/11/22, 12:59 PM - Ishroop: Phd scholar’s lab
5/11/22, 12:59 PM - Ishroop: New academic block, 1st floor
5/11/22, 12:59 PM - Ishroop: AI/ML lab viva will be tomorrow at 12:40
5/11/22, 12:59 PM - Ishroop: Venue is same as above
5/11/22, 12:59 PM - Ishroop: 🥲🥲🥲
5/11/22, 12:59 PM - Ishroop: Kisine maam se jaakr baat kri hai kya?
5/11/22, 1:00 PM - Yashwin: Kal na ?
5/11/22, 1:00 PM - Yashwin: Not me
5/11/22, 1:24 PM - Rohit Pec Mech: Wtf
5/11/22, 1:25 PM - Rohit Pec Mech: Aaj hai kya ye ?
5/11/22, 1:25 PM - Rohit Pec Mech: Mai ghar aagya
5/12/22, 6:44 AM - Ishroop: Reminder
5/12/22, 8:47 AM - Gursharan Kaur✨: Bhenchod !! 🥲
5/12/22, 8:47 AM - Gursharan Kaur✨: Pehle kam lge huye hain kya ???
5/12/22, 8:53 AM - Ishroop: _Ab to aadat si hai mujhko aise jeene ki_
5/12/22, 7:52 PM - YUDHISHTER RANA Pec Mech: Bhai Mahesh Yadav Fail to ni karte kisi ko?
5/13/22, 9:14 AM - Yashwin: <Media omitted>
5/13/22, 9:14 AM - Yashwin: <Media omitted>
5/13/22, 9:14 AM - Yashwin: <Media omitted>
5/13/22, 9:14 AM - Yashwin: <Media omitted>
5/13/22, 9:14 AM - Yashwin: <Media omitted>
5/17/22, 9:20 AM - Sparsh Pec: Koi jara h kyaa paper dekhne
5/17/22, 9:26 AM - Rohit Pec Mech: Yes ig
5/17/22, 9:26 AM - Yashwin: Phir marks dekkar aayega
5/17/22, 9:26 AM - Yashwin: 🌝
5/17/22, 9:27 AM - Sparsh Pec: Yes.
5/17/22, 9:43 AM - Rohit Pec Mech: Dekh kar*
5/17/22, 9:51 AM - Yashwin: Yes sir exactly
5/17/22, 9:54 AM - Rohit Pec Mech: Tu aara ?
5/17/22, 10:11 AM - Yashwin: Mei Delhi mei hu
5/17/22, 10:15 AM - Rohit Pec Mech: Damnn. Enjoii
5/17/22, 10:16 AM - Yashwin: Pollution and garmi 🌝
7/25/22, 12:01 PM - YUDHISHTER RANA Pec Mech: Jo gcr pe experiments aaye hain unmein se kaunsa likhna hai?
7/25/22, 12:53 PM - Ishroop: G1 - temporary hardness
7/25/22, 6:29 PM - Yashwin: Kal class online hai offline ?
7/25/22, 7:31 PM - Ishroop: Koi info aayi nahi abhi
7/25/22, 7:32 PM - Ishroop changed this group's icon
7/28/22, 10:40 PM - Yashwin: <Media omitted>
8/1/22, 8:03 PM - YUDHISHTER RANA Pec Mech: Practical file ki submission Kab tak hai?
8/1/22, 8:05 PM - Shalin: This message was deleted
8/5/22, 12:48 AM - Shalin: <Media omitted>
8/5/22, 12:48 AM - Shalin: <Media omitted>
8/5/22, 12:48 AM - Shalin: inn dono me kaun si krni hai ??
8/5/22, 1:00 AM - Shalin: N1 (0.1 ya 0.12 ) hai ??
Ye to confirm kr do ??
8/5/22, 1:00 AM - Gursharan Kaur✨: Jo man kre vo likhlo
8/5/22, 1:01 AM - Shalin: This message was deleted
8/5/22, 1:02 AM - Shalin: Aise kaise ??
8/5/22, 1:02 AM - Shalin: This message was deleted
8/5/22, 1:09 AM - Shalin: Yhi krna chahiye
ok thanks
8/5/22, 7:47 AM - YUDHISHTER RANA Pec Mech: Waise confirmed hai aaj file ki submission?
8/5/22, 7:47 AM - Yashwin: No idea
8/5/22, 10:11 AM - Shalin: <Media omitted>
8/5/22, 10:11 AM - Shalin: <Media omitted>
8/5/22, 10:14 AM - Yashwin: <Media omitted>
8/9/22, 5:18 PM - Shalin: <Media omitted>
8/9/22, 5:19 PM - Shalin: Alkanity wale exp ki ??
8/21/22, 3:55 PM - Gautam Pec changed their phone number to a new number. Tap to message or add the new number.
8/23/22, 8:58 PM - Arihan Mech: Kal practical attend karna hai?
8/23/22, 8:58 PM - Gursharan Kaur✨: Hnji
8/23/22, 8:59 PM - Arihan Mech: And the airbus thing?
8/23/22, 8:59 PM - Rohit Pec Mech: Hn wohi
8/23/22, 8:59 PM - Rohit Pec Mech: Rehne dete practical
8/23/22, 8:59 PM - Rohit Pec Mech: 🫠
8/23/22, 8:59 PM - Gursharan Kaur✨: Prioritise krko
8/23/22, 8:59 PM - Gursharan Kaur✨: Krlo*
8/23/22, 8:59 PM - Gursharan Kaur✨: And agar majority nhi jaana chahte prac k liye
8/23/22, 8:59 PM - Gursharan Kaur✨: Toh nhi jayenge ..m
8/23/22, 9:00 PM - Rohit Pec Mech: Batado saare. Dekhlenge
8/23/22, 9:00 PM - Gursharan Kaur✨: As simple as that ...
8/23/22, 9:00 PM - Gursharan Kaur✨: Hn
8/23/22, 9:00 PM - Rohit Pec Mech: @all
8/23/22, 9:01 PM - Arihan Mech: Aur baaki ki classes?
8/23/22, 9:01 PM - Gursharan Kaur✨: @918427563125 @916239579405 @919467734085 @919478379030 @919779772164 @918146907246 @918054349284 @919876326716 @916239902903 @916239412997 @917710715181 @918146309152 @919872220548
8/23/22, 9:01 PM - Gursharan Kaur✨: .
8/23/22, 9:01 PM - Gursharan Kaur✨: Ye bhi btado sabhi ..
8/23/22, 9:02 PM - Yashwin: Airbus it is
8/23/22, 9:02 PM - Priyanshu Mech: +1
8/23/22, 9:03 PM - Arihan Mech: I'm fine with either
8/23/22, 9:04 PM - Sparsh Pec: Prac lgate h yrr 🙃
8/23/22, 9:10 PM - Shalin: Saalo mai bhi hun 😂😂
8/23/22, 9:19 PM - Sagar: +1
8/23/22, 9:19 PM - Ishroop: Airbus ke liye chalte yaar
8/23/22, 9:19 PM - Ishroop: Koi nahi jaayega class ke liye
8/23/22, 9:19 PM - Sagar: Prob mass bunk hoga
8/23/22, 9:20 PM - Ishroop: Wohi
8/23/22, 9:22 PM - Shalin: ++
8/23/22, 9:39 PM - YUDHISHTER RANA Pec Mech: Sir aapko kaise bhul sakte hain
8/23/22, 9:39 PM - YUDHISHTER RANA Pec Mech: No practical tomorrow
8/23/22, 9:40 PM - +91 98722 20548 left
8/23/22, 9:40 PM - Shalin: Absolute truth 🤣🤣
8/23/22, 9:43 PM - Gursharan Kaur✨: Confirmed h ab ye bas ....
8/23/22, 9:43 PM - YUDHISHTER RANA Pec Mech: Saanpon ki kami ni hai duniya mein
8/23/22, 9:43 PM - Gursharan Kaur✨: Kal koi Mt jaana
8/23/22, 9:44 PM - Gursharan Kaur✨: And agar koi jaara h toh btado abhi
8/23/22, 9:44 PM - Ishroop: +±
8/23/22, 9:44 PM - Ishroop: Sparsh i thought u were one of us now 🥲😂
8/23/22, 9:44 PM - Gursharan Kaur✨: ++
8/23/22, 9:44 PM - Gursharan Kaur✨: But for a while ...
8/23/22, 9:45 PM - Ishroop: Tu badal gaya yaar sparsh
8/23/22, 9:45 PM - Ishroop: Cdgc ne badal diya tujhe 😂
8/23/22, 9:45 PM - Gursharan Kaur✨: @918054349284 🥺🥺
8/23/22, 9:45 PM - Ishroop: 🥲😔
8/23/22, 9:45 PM - Gursharan Kaur✨: Yaar yaar na raha ...🥲
8/23/22, 9:59 PM - Arihan Mech: Prac nahi lagana??
8/23/22, 10:06 PM - Shalin: Aabhi tk to yhi pta chl rha hai
8/23/22, 10:07 PM - Gursharan Kaur✨: Abhi tk toh nhi lgana h
8/23/22, 10:14 PM - Arihan Mech: Subah koi jayega toh nahi?
8/23/22, 10:15 PM - Sparsh Pec: I don't think so 😈
8/23/22, 10:16 PM - Shalin: This message was deleted
8/23/22, 10:17 PM - Shalin: Pta nhi 🥲🥲
8/23/22, 10:39 PM - Shalin: Prr kl pta lg jayega
8/23/22, 10:42 PM - Gursharan Kaur✨: I don't think so ...
8/23/22, 10:43 PM - Gursharan Kaur✨: Agar koi jaara h toh btado yaar 🥲
8/23/22, 10:43 PM - Sparsh Pec: Yehi to bola mene 🙃
8/23/22, 10:43 PM - Gursharan Kaur✨: Ye toh ni bola tune 🤨
8/23/22, 10:50 PM - YUDHISHTER RANA Pec Mech: This message was deleted
8/24/22, 9:30 AM - YUDHISHTER RANA Pec Mech: Koi jaa to ni raha?
8/24/22, 9:30 AM - Yashwin: Sir ko message daaldo
8/24/22, 9:30 AM - Gursharan Kaur✨: I am not going ...
8/24/22, 9:31 AM - Yashwin: Most students are attending airbus session
8/24/22, 9:31 AM - Yashwin: Jisne apna name change kar rakha
8/24/22, 9:32 AM - Ishroop: Dw
8/24/22, 9:32 AM - Ishroop: Called sir
8/24/22, 9:32 AM - Ishroop: Class cancelled
8/24/22, 9:32 AM - Yashwin: Ok✌️
8/24/22, 9:32 AM - Ishroop: Reschedule krwa lenge baad mein
8/24/22, 7:06 PM - YUDHISHTER RANA Pec Mech: Aaj 12-1 DOMS ka lecture laga tha?
8/24/22, 7:09 PM - Ishroop: Bc
8/24/22, 7:09 PM - Ishroop: Kaun gaya lagaane???
8/24/22, 7:09 PM - YUDHISHTER RANA Pec Mech: Waise puchra hun😂
8/24/22, 7:09 PM - Yashwin: I guess koi nahi
8/24/22, 7:09 PM - Yashwin: G1 wale mostly session dekh rahe the
8/24/22, 7:09 PM - Gursharan Kaur✨: yehi lgra ab tk toh
8/24/22, 7:10 PM - Gursharan Kaur✨: G1 pe poochhlo koi
8/24/22, 7:10 PM - Gursharan Kaur✨: tb final hojega
8/24/22, 7:10 PM - YUDHISHTER RANA Pec Mech: Aur CAD laga tha aaj?
8/24/22, 7:13 PM - Ishroop: Agar kisi mkl ne lagaayi bhi hjgi to saamne se thoda bolega
8/24/22, 7:13 PM - Gursharan Kaur✨: koi na koi toh bolega hi
8/24/22, 9:26 PM - Rohit Pec Mech: Bhai aaj koi class kisine lagayi ho to bata do. We'll not say anything just pata ho ki kon gaya thaa
8/24/22, 9:26 PM - Rohit Pec Mech: Cause I didn't and I came to know ki koi gaya thaa shayad....
8/24/22, 9:27 PM - Rohit Pec Mech: Baaki batado chill scenes hai yaar 😶‍🌫️
8/24/22, 9:27 PM - Sparsh Pec: Mene lagai thi yrr
Sorry 🥺
8/24/22, 9:28 PM - Gursharan Kaur✨: Chup reh !!
8/24/22, 9:29 PM - Gursharan Kaur✨: Ask this on G1 .,.prolly you will get someone's reply ...
8/24/22, 9:29 PM - Yashwin: Red tshirt mei ha lgayi thi isne
8/24/22, 9:30 PM - Gursharan Kaur✨: Cz i got to know prolly someone went from M3 ...although i m not sure but this is what someone told me
8/24/22, 9:33 PM - Arihan Mech: Class lagi konsi thi?
8/24/22, 9:34 PM - Sparsh Pec: PPC ki
Mene vo hi lagai thi
8/24/22, 9:35 PM - Gursharan Kaur✨: 🤦‍♀️🤦‍♀️
8/24/22, 10:08 PM - Shalin: Aab pta krke kya hoga ??
8/24/22, 10:09 PM - Shalin: Aab kl ki class ka pta kro
8/25/22, 7:42 AM - Sagar: Probably Mohit kumar
8/25/22, 8:35 AM - Sparsh Pec: Attendance lga dena
8/25/22, 8:35 AM - Sparsh Pec: Process me baitha hu me
8/25/22, 8:35 AM - Ishroop: Will try but mushkil hai
8/25/22, 8:38 AM - Yashwin: Pls
8/25/22, 8:40 AM - Ishroop: Bhai itne logo ki kaha lagegi 🥲
8/25/22, 8:40 AM - Ishroop: 20 log bhi nahi hain class mein
8/25/22, 8:40 AM - Yashwin: Yaar try karle
8/25/22, 8:41 AM - Ishroop: Kya bolu? Tum hi bata do mein bol dungi.
8/25/22, 11:07 PM - Shalin: This message was deleted
8/25/22, 11:08 PM - Shalin: This message was deleted
8/26/22, 7:59 AM - Shalin: Follow this link to join my WhatsApp group: https://chat.whatsapp.com/CIE6TrKvqhgH10fU3asagi
8/26/22, 7:59 AM - Shalin: POM Group 2 (Sem 5)
8/26/22, 8:42 AM - Sagar: 9 o clock practical hai aaj?
8/26/22, 8:52 AM - Gursharan Kaur✨: Hn
8/26/22, 8:57 AM - Gursharan Kaur✨: Hai kahaan pe prac ??
8/26/22, 8:58 AM - Yashwin: Most probably fluid mechanics lab
8/26/22, 9:07 AM - Rohit Pec Mech: Yaar agar proxy pe attendance laga pao
8/26/22, 9:07 AM - Rohit Pec Mech: Laga lena pls
8/26/22, 9:07 AM - Yashwin: Chal hatt class lga aakar 😂
8/26/22, 9:07 AM - Rohit Pec Mech: Bhai beemar hoon 😔
8/26/22, 9:13 AM - Yashwin: Ok
8/26/22, 9:15 AM - Mohak Gandhi Pec: Lab kaha ha?
8/26/22, 9:15 AM - Gursharan Kaur✨: Audi se right turn then left turn ...
8/26/22, 9:16 AM - Mohak Gandhi Pec: ok
8/26/22, 9:31 AM - Ishroop: 20107006 Ishroop Kaur
8/26/22, 9:31 AM - Ishroop: 20107006 Ishroop Kaur
20107015 Gursharan
20107017 Priyanshu
8/26/22, 9:32 AM - Yashwin: Isko abhi mat bolna kuch
8/26/22, 9:32 AM - Kshitiz Sharma Mech: 20107006 Ishroop Kaur
20107015 Gursharan
20107017 Priyanshu
20107003 Kshitiz Sharma
20107005 Yashwin Mehtani
8/26/22, 9:32 AM - Yashwin: Confuse hojayenge
8/26/22, 9:33 AM - Ishroop: 🥲😂
8/26/22, 9:33 AM - Rohit Pec Mech: Ye kya chalra hai ?
8/26/22, 9:33 AM - Ishroop: Kuchni
8/26/22, 9:33 AM - Rohit Pec Mech: Hainji ?
8/26/22, 9:34 AM - Rohit Pec Mech: Then why you guys adding Sid's ?
8/26/22, 9:34 AM - Ishroop: Arrey dang hai
8/26/22, 9:34 AM - Rohit Pec Mech: Ou
8/26/22, 9:34 AM - Ishroop: Fm class
8/26/22, 9:34 AM - Rohit Pec Mech: Attendance laga dena fir 😔
8/26/22, 9:34 AM - Ishroop: List Bana raha M1 ki
8/26/22, 9:34 AM - Rohit Pec Mech: If possible
8/26/22, 9:34 AM - Ishroop: Bc dang hai.. what part of attendance do u think is required 😂
8/26/22, 9:34 AM - Yashwin: Lag jayegi shyd
8/26/22, 9:34 AM - Rohit Pec Mech: Acha hn
8/26/22, 9:34 AM - Rohit Pec Mech: Wo bhi hai
8/26/22, 9:34 AM - Ishroop: G2 ne poore sem nahi lagayi thi class
8/26/22, 9:34 AM - Rohit Pec Mech: Okok
8/26/22, 9:34 AM - Ishroop: 😂😂😂😂
8/26/22, 9:44 AM - Ishroop: <Media omitted>
8/28/22, 10:02 PM - Arihan Mech: Tomorrow's tutorial is scheduled at 2-3pm. Plz, inform in ur grp.
8/28/22, 10:02 PM - Arihan Mech: For Prod engg
8/28/22, 10:03 PM - Ishroop: Yaaaarrrr 🥲
8/28/22, 10:03 PM - Ishroop: Hai kaun pe ka tut incharge weise?
8/28/22, 10:03 PM - Yashwin: 9 bje tha tut
8/28/22, 10:03 PM - Gursharan Kaur✨: Mp kamal sir ...
8/28/22, 10:04 PM - Arihan Mech: Kamal sir ka text aaya
8/28/22, 10:04 PM - Ishroop: Okk cool
8/28/22, 10:04 PM - Ishroop: Hn
8/28/22, 10:05 PM - Ishroop: Ab 9 se 10 wehle hum 🥲
8/28/22, 10:05 PM - Yashwin: Yaar ek ghanta faaltu rukna padega
8/28/22, 10:05 PM - YUDHISHTER RANA Pec Mech: 8-9 hai kal?🥲
8/28/22, 10:05 PM - Yashwin: Ha
8/28/22, 10:05 PM - Sparsh Pec: Tujhe aaya ?
@916239412997 broo!!
8/28/22, 10:06 PM - Ishroop: Hn wohi to
8/28/22, 10:06 PM - Kshitiz Sharma Mech: Nopee
8/28/22, 10:27 PM - Sparsh Pec: Kal 8 bje h class ?
8/28/22, 10:28 PM - Sankalp Singla: Hn
8/28/22, 10:28 PM - Sparsh Pec: 🥺
8/29/22, 11:11 AM - Arihan Mech: Kamal sir said that he can take the tut today at 1 pm or 1.30 pm
8/29/22, 11:11 AM - Arihan Mech: He is busy tomorrow
8/29/22, 11:12 AM - Rohit Pec Mech: Lunch ?
8/29/22, 11:12 AM - Arihan Mech: 2 pm is also an option
8/29/22, 11:13 AM - Arihan Mech: Pls confirm the time that is okay with everyone and I can let sir know
8/29/22, 11:16 AM - Sparsh Pec: Yrrr
8/29/22, 11:17 AM - Sparsh Pec: 1 rakh lete h
8/29/22, 11:17 AM - Sparsh Pec: Vrna for 1-2 ka gap waste hojega
8/29/22, 11:19 AM - Yashwin: 1:30
8/29/22, 11:19 AM - Ishroop: Oyye aaj Rehne do
8/29/22, 11:19 AM - Ishroop: This message was deleted
8/29/22, 11:19 AM - Ishroop: Mass bunk kr lete
8/29/22, 11:19 AM - Ishroop: Tut hai weise bhi
8/29/22, 11:19 AM - Ishroop: Btao
8/29/22, 11:20 AM - Yashwin: Yeh sir ki class mei nahi kar sakte
8/29/22, 11:20 AM - Yashwin: Sir ke saath projecg karna hai
8/29/22, 11:20 AM - Ishroop: Oo yaar fir tum hi baat krlo sir se
8/29/22, 11:20 AM - Ishroop: Postpone krwa do
8/29/22, 11:20 AM - Ishroop: Kl krwa lo
8/29/22, 11:21 AM - Yashwin: Puch lenge
8/29/22, 11:21 AM - Ishroop: Hn please 🥺
8/29/22, 11:21 AM - Arihan Mech: Sir ne jana hai kahin, isliye kal mana kara
8/29/22, 11:21 AM - Ishroop: Parso krlein
8/29/22, 11:22 AM - Ishroop: Like any other time in the week
8/29/22, 11:27 AM - Sparsh Pec: Yrr 1 bje hogi vrna nhi hogi
8/29/22, 11:27 AM - Gursharan Kaur✨: ++
8/29/22, 11:27 AM - Sparsh Pec: Baat khtam
8/29/22, 11:27 AM - Gursharan Kaur✨: Nhi hogi yaar aaj toh ...
8/29/22, 11:28 AM - Ishroop: +++
8/29/22, 11:28 AM - Gursharan Kaur✨: Kabhi baad mein adjust krlenge
8/29/22, 11:28 AM - Yashwin: Sir se baat karlo phir
8/29/22, 11:28 AM - Ishroop: Yuss
8/29/22, 11:28 AM - Ishroop: Tum kro
8/29/22, 11:28 AM - Gursharan Kaur✨: Ajj pehle hi bhut jyada pak chuke hain
8/29/22, 11:28 AM - Ishroop: Tumhaare minor ke teacher hain
8/29/22, 11:28 AM - Gursharan Kaur✨: Subah se bc classes hi classes
8/29/22, 11:28 AM - Ishroop: ++++
8/29/22, 11:29 AM - Gursharan Kaur✨: ++
8/29/22, 11:29 AM - Yashwin: Mera idea nahi hai class na lgane ka aaj 🫡 mei nahi kar rha baat @918054349284 karlega
8/29/22, 11:31 AM - Sparsh Pec: Fir lgale 1 bje chup chap
8/29/22, 11:32 AM - Gursharan Kaur✨: Are yaar 🥲
8/29/22, 11:32 AM - Gursharan Kaur✨: @916239579405 tu krke aaja sir se baat
8/29/22, 11:32 AM - Yashwin: Lunch arrange karde phir
8/29/22, 11:33 AM - Yashwin: 🙃
8/29/22, 11:33 AM - Gursharan Kaur✨: Bhayi aaj ni please 😭
8/29/22, 11:33 AM - Yashwin: Karlo baat phir ki wed ya aage schedule karde
8/29/22, 11:35 AM - Gursharan Kaur✨: Thursday 9-10 ??
8/29/22, 11:35 AM - Sparsh Pec: Noooooo
8/29/22, 11:35 AM - Ishroop: Bhai @919876326716 Baat kri kab hai tumne teachers se
8/29/22, 11:36 AM - Ishroop: Bc har baar mein hi krti hu
8/29/22, 11:36 AM - Ishroop: Ek baar kisi valid reason se bol rhe hain to krle na
8/29/22, 11:36 AM - Gursharan Kaur✨: Kyu bc ab teko iss se kya problem h ??
8/29/22, 11:36 AM - Sparsh Pec: Thursday busy
8/29/22, 11:36 AM - Ishroop: Sparsh cancel nahi krwa rahe
8/29/22, 11:36 AM - Ishroop: Postpone krwa rahe
8/29/22, 11:36 AM - Gursharan Kaur✨: Bhayi yaar fir aaj 2-3 hi rakhlo
8/29/22, 11:37 AM - Gursharan Kaur✨: Jo sir ne bola tha as it is
8/29/22, 11:37 AM - Sparsh Pec: 1 bje me kya dikkat h ?
8/29/22, 11:37 AM - Ishroop: Arrey to dekh lenge na ki na rahein on the day tu nahi aa sakta
8/29/22, 11:37 AM - Gursharan Kaur✨: Cz na koi bata krne ko tyaar h na koi ek time decide kr ra
8/29/22, 11:37 AM - Yashwin: 👍
8/29/22, 11:37 AM - Ishroop: Hostellers ka lunch time hai 1 baje
8/29/22, 11:37 AM - Gursharan Kaur✨: Lunch bhi Krna hota h
8/29/22, 11:37 AM - Sparsh Pec: Yrr ek bje rakhte h or attendance lga kr chlte h
8/29/22, 11:37 AM - Sparsh Pec: Simple
8/29/22, 11:38 AM - Gursharan Kaur✨: Hellllll nooooooooo
8/29/22, 11:38 AM - Gursharan Kaur✨: Nooooo wayyyyyyyyy
8/29/22, 11:38 AM - Ishroop: Agar sirf attendance lagwaani hoti to dikkat na hoti
8/29/22, 11:38 AM - Ishroop: But sir padha ke hi chodhenge
8/29/22, 11:38 AM - Gursharan Kaur✨: Sir codes krwane wale hain
8/29/22, 11:38 AM - Ishroop: So no
8/29/22, 11:38 AM - Gursharan Kaur✨: Cnc k
8/29/22, 11:38 AM - Ishroop: Bs fir kisi aur din rakhwa lenge
8/29/22, 11:38 AM - Gursharan Kaur✨: So there is no chance k attendance lgake vaapis aajayein
8/29/22, 11:38 AM - Yashwin: Mei puchleta hu sir se but koi reason dedo
8/29/22, 11:39 AM - Gursharan Kaur✨: Just say it k sir aaj bacho ki McKinsey ki interviews hain ...
8/29/22, 11:39 AM - Ishroop: Hn best
8/29/22, 11:39 AM - Gursharan Kaur✨: And they are saying k kisi aur din rakhlo ...
8/29/22, 11:39 AM - Yashwin: Ok try karlete
8/29/22, 11:39 AM - Ishroop: Bolde majority G1 ke hain and unka miss ho jaayega saara
8/29/22, 11:40 AM - Gursharan Kaur✨: ++
8/29/22, 11:40 AM - Gursharan Kaur✨: Yes please !!
8/29/22, 12:15 PM - Yashwin: <Media omitted>
8/29/22, 12:17 PM - Sparsh Pec: Yrrrr
8/29/22, 12:17 PM - Sparsh Pec: Krdia naraz
8/29/22, 12:17 PM - Gursharan Kaur✨: Abe haat na !!
8/29/22, 12:17 PM - Gursharan Kaur✨: Tu toh rehne hi de
8/29/22, 12:18 PM - Sparsh Pec: 😂😂
8/29/22, 12:18 PM - Gursharan Kaur✨: Bs ab shaanti se 2-3 lagalo
8/29/22, 12:35 PM - Gursharan Kaur✨: Theek h na ??
8/29/22, 12:35 PM - Gursharan Kaur✨: Fir toh sir ko text krdete hain
8/29/22, 12:43 PM - Sparsh Pec: Kuch thik nhi h 😖
8/29/22, 12:53 PM - Gursharan Kaur✨: Tu toh rehne de
8/29/22, 1:14 PM - Shalin: Kha hoegi tut
8/29/22, 1:14 PM - Shalin: ??
8/29/22, 1:14 PM - Gursharan Kaur✨: Som lab or L6
8/29/22, 1:15 PM - Shalin: Ok
8/29/22, 1:57 PM - Arihan Mech: Tut in L6
8/29/22, 2:09 PM - YUDHISHTER RANA Pec Mech: Attendence dekh lena yaar agar ho sake
8/29/22, 2:12 PM - Ishroop: Yes yes
8/29/22, 2:12 PM - Ishroop: Me attending session 😌
8/29/22, 2:12 PM - YUDHISHTER RANA Pec Mech: Kitne log hain?
8/29/22, 2:12 PM - Ishroop: Idk
8/29/22, 2:12 PM - Ishroop: Sir ko bol dena mein session laga rhi bs
8/29/22, 2:12 PM - Ishroop: @918699133946
8/29/22, 2:12 PM - Ishroop: @919876326716
8/29/22, 2:12 PM - Ishroop: @918427563125
8/29/22, 2:12 PM - YUDHISHTER RANA Pec Mech: Same here🤓
8/29/22, 2:13 PM - YUDHISHTER RANA Pec Mech: Mera bhi yahi bol dena
8/29/22, 2:13 PM - Ishroop: Saale mera reason na utha
8/29/22, 2:13 PM - Ishroop: Tu bol dena ki tera mckinsey shortlist ho gaya tha
8/29/22, 2:13 PM - Ishroop: 🤨😌😌😌
8/29/22, 2:13 PM - YUDHISHTER RANA Pec Mech: Kyun zakhmon pe namak chidakri hai🥲
8/29/22, 2:14 PM - Ishroop: Arrey tu jee le khwaab
8/29/22, 2:14 PM - Ishroop: 🔥🔥🔥
8/29/22, 2:14 PM - YUDHISHTER RANA Pec Mech: 🥲👍
8/29/22, 3:51 PM - Ishroop: @916239412997 oyye mckinsey ka kya chal raha
8/29/22, 3:52 PM - Kshitiz Sharma Mech: Result ana h abhi
8/29/22, 3:54 PM - Ishroop: Abhi ek hi interview hua????
8/29/22, 3:54 PM - Kshitiz Sharma Mech: 2
8/29/22, 4:09 PM - Ishroop: First mein kya hua???
8/29/22, 4:09 PM - Ishroop: Like shortlist hue log ya sabhi ne diye 2 interviews
8/29/22, 4:11 PM - Kshitiz Sharma Mech: 3 hue the shortlist
8/29/22, 4:11 PM - Kshitiz Sharma Mech: But ye sirf GSC ka h
8/29/22, 4:11 PM - Kshitiz Sharma Mech: Baaki profiles ka ni ptaa
8/29/22, 4:28 PM - Ishroop: Kaun 3????
8/29/22, 4:28 PM - Ishroop: U and baaki dono???
8/29/22, 4:33 PM - Kshitiz Sharma Mech: Mera ni huaa 2nd round
8/29/22, 4:33 PM - Ishroop: F
8/29/22, 4:33 PM - Ishroop: Yaar bc hua kiska hai
8/29/22, 4:34 PM - Ishroop: Jo deserving log thei wo to nikal gaye
8/29/22, 4:34 PM - Kshitiz Sharma Mech: Abhinav Bharia ka huaa tha
8/30/22, 8:04 PM - Sankalp Singla: Kl prac lgare ho???
8/30/22, 8:04 PM - Yashwin: Ha
8/30/22, 8:04 PM - Yashwin: Ek toh lage
8/30/22, 8:07 PM - Sankalp Singla: Kl axxela ka process hai na
8/30/22, 8:08 PM - Yashwin: I have no idea
8/30/22, 8:08 PM - Sankalp Singla: Bata ra hu
8/30/22, 8:08 PM - Yashwin: Usko bolenge attendance toh lga dega
8/30/22, 8:08 PM - YUDHISHTER RANA Pec Mech: haan bhai lagwa dio
8/30/22, 10:43 PM - Shalin: Kl nhi lgani lab mtlab ??
8/30/22, 10:43 PM - Shalin: Ya lgani hai ??
8/31/22, 1:35 AM - Shalin: Mera bhi lagwa dio
8/31/22, 6:45 AM - Ishroop: Aaj lab laga lena sab. Cancel hone ka chance nahi hai
8/31/22, 6:46 AM - Ishroop: Last time bhi Airbus day krke cancel krwa di thi meine
8/31/22, 6:46 AM - Ishroop: Debashish sir hi hain as far as I know
8/31/22, 6:46 AM - Ishroop: So tumlog attendance ki itni bt mt lo but please jitne aa sakte aaj class laga lena
8/31/22, 7:00 AM - Yashwin: Ha attend karlo if possible
8/31/22, 8:34 AM - Shalin: HMT kha hai ??
8/31/22, 8:49 AM - Ishroop: Guys i just talked to sir
Practical roto block mein hai
8/31/22, 8:49 AM - Ishroop: Wahi aa jaao saare
8/31/22, 8:50 AM - Gursharan Kaur✨: Bhyi seriously ?
8/31/22, 8:50 AM - Gursharan Kaur✨: Ig first prac sbka eac lab mein hua tha
8/31/22, 8:50 AM - Ishroop: Hn I asked sir. Meine bata diya ki sir aaj first practical hai and debasish sir kehte roto block aa jaao
8/31/22, 8:50 AM - Gursharan Kaur✨: 2nd praf roto block mein hu h
8/31/22, 8:50 AM - Gursharan Kaur✨: Okok cool!!
8/31/22, 8:51 AM - Ishroop: Maybe humme 2md pehle krwa rahe idk
8/31/22, 8:51 AM - Ishroop: Tumlog wahi aa jaao
8/31/22, 8:54 AM - Shalin: Tom lab ke right Hmt lab
8/31/22, 8:55 AM - Shalin: 1st floor ??
8/31/22, 9:02 AM - Sparsh Pec: Me thoda late hojunga
8/31/22, 9:05 AM - Rohit Pec Mech: +1
8/31/22, 9:06 AM - Ishroop: Rehne do aane ko
8/31/22, 9:06 AM - Ishroop: Attendance bhi Rehne denge :)
8/31/22, 9:07 AM - Sparsh Pec: <Media omitted>
8/31/22, 9:33 AM - Yashwin: <Media omitted>
8/31/22, 9:34 AM - Sparsh Pec: Attendance?
8/31/22, 9:34 AM - Sparsh Pec: Aara hu me!!
8/31/22, 9:38 AM - Rohit Pec Mech: Mai bhi
8/31/22, 9:38 AM - Rohit Pec Mech: In 5 min
8/31/22, 9:38 AM - Yashwin: <Media omitted>
8/31/22, 9:38 AM - Yashwin: Practical hogaya khtm almost
8/31/22, 9:40 AM - Ishroop: Rehne do. Aaj itni bt hai nahi weise
8/31/22, 9:41 AM - Ishroop: Plus sir chill hain to idts attendance ka itna bolenge
8/31/22, 9:41 AM - Sparsh Pec: Debu sir h ?
8/31/22, 9:41 AM - Ishroop: Hnn
8/31/22, 9:41 AM - Ishroop: Tabhi bol rhi
8/31/22, 9:42 AM - Sparsh Pec: Me aagya bs
8/31/22, 9:42 AM - Sparsh Pec: Rok ke rak
8/31/22, 9:48 AM - Ishroop: Saale moot hai jo rok ke rakhein
8/31/22, 10:11 AM - Shalin: Jyada ho rha 🤣
9/1/22, 9:46 AM - Gursharan Kaur✨: Dear Students,

Please inform all the students of M1 Group of Heat and Mass Transfer lab to draw the sketch of the setup whose printout is already with you.

The thermocouple position, length of the copper rod etc. need to be mentioned clearly.

Thank you.
9/1/22, 9:47 AM - Gursharan Kaur✨: Regards- Debasish sir
9/1/22, 9:47 AM - Ishroop: Mtlb file likhni ya nahi
9/1/22, 9:48 AM - Gursharan Kaur✨: Obvio meri jaan likhni h ..
9/1/22, 9:48 AM - Ishroop: 🥲🥲🥲
9/1/22, 10:13 AM - Gursharan Kaur✨: Yes.

Some groups have started preparing and submitting the files.

So please prepare one and submit in your next lab class.
9/1/22, 10:16 AM - Ishroop: Layout to nahi likhna na ?
9/1/22, 10:16 AM - Yashwin: Layout FM wale mei likhna hai
9/1/22, 10:16 AM - Yashwin: iska idea nahi
9/1/22, 10:26 AM - Gursharan Kaur✨: Abhi tk toh ni bola sir ne
9/1/22, 10:27 AM - Gursharan Kaur✨: Baaki i will ask him
9/1/22, 10:27 AM - Ishroop: Hnn bata diyo puchke
9/1/22, 10:31 AM - Gursharan Kaur✨: Likhna h yaar ...
9/1/22, 10:34 AM - Ishroop: Ok
9/1/22, 7:55 PM - YUDHISHTER RANA Pec Mech: Kal kuch submission wagara hai FM ke practical ki?
9/1/22, 8:05 PM - Ishroop: Hn
9/1/22, 8:05 PM - Ishroop: Layout
9/1/22, 8:05 PM - Yashwin: Yeh kab hua 🌝
9/1/22, 8:06 PM - Ishroop: No idea but hua hai
9/1/22, 8:07 PM - Ishroop: Oh wait hn
9/1/22, 8:07 PM - Ishroop: @918054349284 ko hi aag lagi thi ki sir padha do practical krwa do etc
9/1/22, 8:07 PM - Ishroop: So sir ne jo poori lab dikhaayi thi
9/1/22, 8:07 PM - Ishroop: Usska layout banaana
9/1/22, 8:07 PM - Yashwin: Chal usko boldenge bhool gaye
9/1/22, 8:07 PM - Yashwin: 🫡
9/1/22, 8:14 PM - Sankalp Singla: Wo toh aaya hi ni tha shyd
9/1/22, 8:15 PM - Sankalp Singla: Dang kuch ni bola tha mere hisaab se
9/1/22, 8:17 PM - YUDHISHTER RANA Pec Mech: Aur bolenge bhi ni
9/1/22, 8:17 PM - YUDHISHTER RANA Pec Mech: Kya karke jaana
9/1/22, 8:17 PM - YUDHISHTER RANA Pec Mech: Bol denge nhi Pata tha
9/1/22, 8:17 PM - Shalin: Layout milega kha se ??
9/1/22, 8:17 PM - Shalin: Lab layout ??
9/1/22, 8:18 PM - YUDHISHTER RANA Pec Mech: Better
9/1/22, 8:37 PM - Sparsh Pec was added
9/1/22, 8:24 PM - Sparsh Pec: Areyyy ooooo
Faltu me naam lgari h 🤷‍♂️
Itni kya dushmani hogai
9/1/22, 8:24 PM - Sparsh Pec: Thanks broo 😘
9/1/22, 8:26 PM - Gursharan Kaur✨: Ye ni aaya tha yaar uss din ....
9/1/22, 8:26 PM - Sparsh Pec: Rehne de yrr, Shareef logo ko hi badnam kiya jata h
9/1/22, 8:27 PM - Yashwin: <Media omitted>
9/1/22, 8:27 PM - Gursharan Kaur✨: Vaise hai ni tu shareef .....but chlo uss din k liye i have to agree k nhi aaya tha tu. ...
9/1/22, 8:28 PM - Sparsh Pec: I'm really disheartened 💔
Bye.
9/1/22, 8:37 PM - Sparsh Pec left
9/1/22, 8:29 PM - Yashwin: Ok bye 😂✌️
9/1/22, 8:29 PM - Gursharan Kaur✨: After looking at this from notis i thought you are going to leave the group ... 😂
9/1/22, 8:30 PM - Gursharan Kaur✨: And how come you are still here .. 😂
9/1/22, 8:51 PM - Ishroop: Theek hai nahi aaya tha sparsh uss din
9/1/22, 8:51 PM - Ishroop: Maah bad
9/1/22, 8:51 PM - Ishroop: 😂🥲
9/1/22, 8:52 PM - Gursharan Kaur✨: Lol!!
9/2/22, 8:53 AM - Gursharan Kaur✨: Yaar fm lab hi aana h na ??
9/2/22, 8:54 AM - Ishroop: Hnn
9/2/22, 9:09 AM - Ishroop removed Divyam Jain
9/2/22, 8:58 AM - Yashwin: <Media omitted>
9/2/22, 9:09 AM - Ishroop added Gautam Pec
9/2/22, 8:58 AM - Yashwin: <Media omitted>
9/2/22, 9:10 AM - YUDHISHTER RANA Pec Mech: Hogya shuru?
9/2/22, 9:10 AM - Yashwin: Na
9/2/22, 9:10 AM - Yashwin: Kuch nahi ho rha
9/2/22, 9:11 AM - Gautam Pec: This message was deleted
9/2/22, 9:11 AM - Gautam Pec: This message was deleted
9/2/22, 9:29 AM - Gautam Pec: <Media omitted>
9/2/22, 9:29 AM - Gautam Pec: <Media omitted>
9/2/22, 9:29 AM - Gautam Pec: <Media omitted>
9/2/22, 9:29 AM - Gautam Pec: <Media omitted>
9/2/22, 9:31 AM - Gautam Pec: <Media omitted>
9/2/22, 9:32 AM - Gautam Pec: <Media omitted>
9/2/22, 9:32 AM - Gautam Pec: <Media omitted>
9/2/22, 9:32 AM - Gautam Pec: <Media omitted>
9/2/22, 9:54 AM - Ishroop: Nice work @919876326716 @919814484499 🔥🔥🔥🔥🔥
9/2/22, 9:54 AM - Gursharan Kaur✨: ++
9/2/22, 10:05 AM - Rohit Pec Mech: Agar kahin attendance mil sake to laga dena guys pls 😔😔
9/2/22, 10:09 AM - Gursharan Kaur✨: Ab toh gya time ..
9/3/22, 6:05 PM - Yashwin: Practical likhna na hmt ka ab
9/3/22, 6:07 PM - Gursharan Kaur✨: Hnm likhna h
9/3/22, 6:07 PM - Gursharan Kaur✨: Layout h kisi k paas ??
9/3/22, 6:08 PM - Yashwin: Layout toh nahi hai but jo wohi likhna hai na jo sir ne file bheji thi na
9/3/22, 6:08 PM - Yashwin: @916239579405 readings bhejdena ✌️
9/3/22, 6:08 PM - Gursharan Kaur✨: @919876326716 file bnake pdf bhej dena ...
9/3/22, 6:08 PM - Gursharan Kaur✨: 🥲
9/3/22, 6:09 PM - Yashwin: Ok 😂
9/3/22, 6:11 PM - Gursharan Kaur✨: <Media omitted>
9/3/22, 6:11 PM - Yashwin: ✌️
9/4/22, 5:34 PM - Arihan Mech: At what time, tomorrow's tute can be scheduled?
9/4/22, 5:34 PM - Arihan Mech: Except 9-10
9/4/22, 5:35 PM - Arihan Mech: For prod engg
9/4/22, 5:35 PM - Gursharan Kaur✨: What options do we have ??
9/4/22, 5:35 PM - Gursharan Kaur✨: 😂
9/4/22, 5:36 PM - Yashwin: Not after 1 shyd ek company ka test hai
9/4/22, 5:36 PM - Gursharan Kaur✨: Expedia ?
9/4/22, 5:36 PM - Yashwin: DMI
9/4/22, 5:36 PM - Gursharan Kaur✨: Oh
9/4/22, 5:37 PM - YUDHISHTER RANA Pec Mech: Kitne baje
9/4/22, 5:37 PM - Yashwin: time nahi aaya
9/4/22, 5:37 PM - YUDHISHTER RANA Pec Mech: Oh
9/4/22, 5:37 PM - Yashwin: toh isliye ghar time se jaana
9/4/22, 5:37 PM - Gursharan Kaur✨: Kis kis ne apply Kiya h for DMI ??
9/4/22, 6:41 PM - Kshitiz Sharma Mech: Maine bhi kiyaa h
9/4/22, 7:04 PM - Yashwin: Phir kal tut ka kya scene hai ?
9/4/22, 7:05 PM - Yashwin: Sir se puchlo if kal
9-10 10-11 ya 2-3 kuch bhi chalega
9/4/22, 7:22 PM - Gursharan Kaur✨: 10-11 class h
9/4/22, 7:23 PM - Gursharan Kaur✨: 2-3 chlega ??
9/4/22, 7:24 PM - Arihan Mech: 2-3 bata du?
9/4/22, 7:25 PM - Yashwin: Sorry parso bolna tha
9/4/22, 7:25 PM - Gursharan Kaur✨: Let @919876326716 and @916239412997 confirm first.....
9/4/22, 7:25 PM - Yashwin: 😅
9/4/22, 7:25 PM - Yashwin: Yaar test ka hi nahi pata kab hoga
9/4/22, 7:25 PM - Gursharan Kaur✨: Prso h kisi ka kuchh ??
9/4/22, 7:26 PM - Gursharan Kaur✨: Prso 2-3 kr sakte fir toh ...
9/4/22, 7:26 PM - Yashwin: Ha chalega
9/4/22, 7:26 PM - Sagar: <Media omitted>
9/4/22, 7:26 PM - Sagar: .
9/4/22, 7:27 PM - Yashwin: Ok yeh nahi dekha tha
9/4/22, 7:27 PM - Yashwin: But ghar bhi jaana hota time par
9/4/22, 7:27 PM - Sagar: Bata sakti hai
9/4/22, 7:27 PM - Gursharan Kaur✨: Fir toh 2-3 ??
9/4/22, 7:28 PM - Yashwin: Ok jab marzi rakho but sir ko given time par hi leni chahiye 😑
9/4/22, 7:32 PM - YUDHISHTER RANA Pec Mech: Exactly
9/4/22, 8:01 PM - Arihan Mech: The prod engg tut will be from 2-3 pm tomorrow
9/4/22, 8:05 PM - Ishroop: Arrey yaar 😔🥺😔
9/5/22, 2:04 PM - Shalin: Ho sake to meri attendence lgwa dena 😅😅
9/5/22, 2:07 PM - YUDHISHTER RANA Pec Mech: Same here
9/5/22, 2:08 PM - Sankalp Singla: ++
9/5/22, 2:09 PM - YUDHISHTER RANA Pec Mech: CR mam dekh lena
9/5/22, 2:10 PM - Yashwin: Woh khud class mei nahi hai
9/5/22, 2:10 PM - Yashwin: Kamal sir puch kar lenge
9/5/22, 2:10 PM - Yashwin: Toh attendance aise nahi milegi
9/5/22, 2:10 PM - Sankalp Singla: Batao
9/5/22, 2:10 PM - YUDHISHTER RANA Pec Mech: Waah
9/5/22, 3:15 PM - Ishroop: Bhai call kr diya kro
9/5/22, 3:15 PM - Ishroop: 🥲🥲🥲🥲
9/6/22, 8:28 AM - Ishroop: HMT practical 1
FM layout and tut sheet
9/6/22, 8:29 AM - Ishroop: Ye kaam hai
Kal hmt hai and friday ko fm so kr lena Yaad se sab
9/6/22, 10:14 AM - Shalin: Thank you @CR
9/6/22, 3:55 PM - Sankalp Singla: Practical bhejdo
9/6/22, 3:55 PM - Sankalp Singla: Hmt ka
9/6/22, 5:47 PM - Rohit Pec Mech: +1
9/6/22, 5:47 PM - Yashwin: <Media omitted>
9/6/22, 5:47 PM - Yashwin: <Media omitted>
9/6/22, 5:47 PM - Yashwin: <Media omitted>
9/6/22, 5:47 PM - Yashwin: <Media omitted>
9/6/22, 5:47 PM - Yashwin: <Media omitted>
9/6/22, 5:47 PM - Yashwin: <Media omitted>
9/6/22, 5:47 PM - Yashwin: M3 ka hai
9/6/22, 5:48 PM - Yashwin: Values change karlena
9/6/22, 5:49 PM - Rohit Pec Mech: Likhne wala part ?
9/6/22, 5:49 PM - Rohit Pec Mech: Line side wala hai ?
9/6/22, 5:49 PM - Yashwin: Observations
9/6/22, 5:49 PM - Yashwin: 🫡
9/6/22, 5:49 PM - Rohit Pec Mech: Ye bhi bhejdo koi
9/6/22, 5:49 PM - Yashwin: Kaisi baatein kar rha
9/6/22, 5:49 PM - Sankalp Singla: Hn
9/6/22, 5:50 PM - Rohit Pec Mech: Arey line side pe jo likhna hai wo mangra hoon
9/6/22, 5:50 PM - Yashwin: Tu bhi kya pooch rha
9/6/22, 5:50 PM - Gursharan Kaur✨: Yaar same hi likh dete
9/6/22, 5:50 PM - Yashwin: Woh toh sir ne send kar rakha group par
9/6/22, 5:50 PM - Gursharan Kaur✨: Kya farak pd raha h
9/6/22, 5:50 PM - Rohit Pec Mech: Wohi mangra
9/6/22, 5:50 PM - Yashwin: Phir sab same karna
9/6/22, 5:50 PM - Rohit Pec Mech: Idhar forward karna
9/6/22, 5:50 PM - Gursharan Kaur✨: Hn yaar.
9/6/22, 5:50 PM - Gursharan Kaur✨: Same hi kr dete hain
9/6/22, 5:51 PM - Rohit Pec Mech: <Media omitted>
9/6/22, 5:51 PM - Rohit Pec Mech: This message was deleted
9/6/22, 5:51 PM - Rohit Pec Mech: Ok got it
9/6/22, 5:51 PM - Yashwin: <Media omitted>
9/6/22, 5:51 PM - Yashwin: Nahi
9/6/22, 5:51 PM - Rohit Pec Mech: To
9/6/22, 5:51 PM - Gursharan Kaur✨: Vaise bhi apne Wale din pe sir ne setup galat kr rakha tha and why to waste time jab hamaare pdi hain calculations ...
9/6/22, 5:51 PM - Rohit Pec Mech: Bc
9/6/22, 5:51 PM - Rohit Pec Mech: 🗿🗿
9/6/22, 5:51 PM - Rohit Pec Mech: Aur konsa hai
9/6/22, 5:51 PM - Yashwin: First doc file
9/6/22, 5:51 PM - Yashwin: On
9/6/22, 5:52 PM - Yashwin: Hmt group
9/6/22, 5:52 PM - Sankalp Singla: Bhej hi de
9/6/22, 5:52 PM - Gursharan Kaur✨: <Media omitted>
9/6/22, 5:52 PM - Rohit Pec Mech: <Media omitted>
9/6/22, 5:52 PM - Sankalp Singla: Yrr
9/6/22, 5:52 PM - Rohit Pec Mech: Okkk
9/6/22, 5:52 PM - Yashwin: Na
9/6/22, 5:52 PM - Yashwin: <Media omitted>
9/6/22, 5:52 PM - YUDHISHTER RANA Pec Mech: Even better
9/6/22, 5:53 PM - Yashwin: Bhej toh dia
9/6/22, 5:53 PM - Rohit Pec Mech: Hn milgya
9/6/22, 5:53 PM - Rohit Pec Mech: Thank you
9/6/22, 5:53 PM - Gursharan Kaur✨: @919876326716 dude, kaise Krna fir ab ??
9/6/22, 5:59 PM - Yashwin: 아니네요
9/6/22, 6:00 PM - Yashwin: Same rakhlo jo photos mei hai sab
9/6/22, 6:00 PM - YUDHISHTER RANA Pec Mech: Sidha sidha ni likh sakta
9/6/22, 6:00 PM - Rohit Pec Mech: Arigato
9/6/22, 6:00 PM - Yashwin: Mannahitha
9/6/22, 6:01 PM - Yashwin: 감사히니다
9/6/22, 6:01 PM - Rohit Pec Mech: ファックオフ
9/6/22, 6:02 PM - Yashwin: Japanese nahi aati padhni 😎
9/6/22, 6:02 PM - Rohit Pec Mech: Korean kids
9/6/22, 6:02 PM - Rohit Pec Mech: 🗿
9/6/22, 6:05 PM - Shalin: India it is 😂😂
9/6/22, 6:05 PM - YUDHISHTER RANA Pec Mech: <Media omitted>
9/6/22, 6:07 PM - YUDHISHTER RANA Pec Mech: Bhai 7016 kyun?
9/6/22, 6:09 PM - Shalin: Kya mtlb
9/6/22, 6:10 PM - Shalin: Hmt wale sir ne username change krne ko bola tha shayad ??
9/6/22, 6:10 PM - Shalin: Nhi krna ??
9/6/22, 6:16 PM - YUDHISHTER RANA Pec Mech: Na na, kisine ni kia
9/6/22, 6:16 PM - YUDHISHTER RANA Pec Mech: Ab yahi reh gaya karne ko
9/6/22, 6:17 PM - Shalin: Hnn 🤔
9/6/22, 7:02 PM - Shalin: How's the josh ??
High sir 😂😂
9/6/22, 11:26 PM - Shalin: This message was deleted
9/6/22, 11:26 PM - Shalin: This message was deleted
9/7/22, 9:12 AM - Shalin: Hmt ki prac kidhr hai ??
9/7/22, 9:12 AM - Shalin: Roto block ??
9/7/22, 9:13 AM - Kshitiz Sharma Mech: Hn
9/7/22, 9:15 AM - Ishroop: Bhai aa jaao.
9/7/22, 9:18 AM - Rohit Pec Mech: Reaching in 10 min
9/7/22, 9:19 AM - Ishroop: <Media omitted>
9/7/22, 9:38 AM - Priyanshu Mech: <Media omitted>
9/7/22, 9:57 AM - Ishroop: <Media omitted>
9/7/22, 9:57 AM - Ishroop: Add the dimensions given in this in experiment 1
9/7/22, 4:03 PM - Ishroop: <Media omitted>
9/7/22, 4:03 PM - Sankalp Singla: Fm ka layout aur tut sheet bhi bhejdo
9/7/22, 4:04 PM - Gursharan Kaur✨: Bhej dete hain thore time tk ...
9/7/22, 4:04 PM - Gursharan Kaur✨: Layout toh ...
9/7/22, 4:05 PM - Gursharan Kaur✨: Tut sheet dekhlo kaun bhejega
9/7/22, 4:08 PM - Ishroop: Upar pada hai chat mein Saara samaan
9/7/22, 4:09 PM - Gursharan Kaur✨: Ig layout ni bheja tha hamne ...
9/7/22, 4:11 PM - Ishroop: Bheja tha
9/7/22, 4:11 PM - Ishroop: Check krlo ek baar
9/8/22, 5:01 PM - Yashwin: Kal 10:15 -11
9/8/22, 5:01 PM - Yashwin: Manu class
9/8/22, 5:01 PM - Yashwin: Kamal sir ka message aaya hai
9/8/22, 5:08 PM - Ishroop: Dang se baat ho gyi
9/8/22, 5:08 PM - Ishroop: He said jo jaaoge free
9/8/22, 5:08 PM - Gursharan Kaur✨: PE??
9/8/22, 5:08 PM - Ishroop: Yep
9/8/22, 5:12 PM - Sankalp Singla: Kl kyu rkhni hai class
9/8/22, 5:12 PM - Ishroop: Topic krwaana sir ne ek
9/8/22, 11:05 PM - YUDHISHTER RANA Pec Mech: kal layout ke alava hai kuch practical ka?
9/8/22, 11:08 PM - Yashwin: Na layout bhejde
9/8/22, 11:23 PM - Ishroop: Guys kal fm ka practical nahi hoga, tutorial class hogi coz permission nahi mili hai.

So kal file mein bas blank page pe layout Bana kr and tutorial sheet lekar aa jaana yaad se
9/8/22, 11:23 PM - Ishroop: *important*
9/8/22, 11:23 PM - Yashwin: Ok ✌️✌️✌️
9/8/22, 11:24 PM - Priyanshu Mech: Layout ki pic?
9/9/22, 7:56 AM - Ishroop: @918699133946
9/9/22, 7:57 AM - Gursharan Kaur✨: <Media omitted>
9/9/22, 9:00 AM - Shalin: Lab nhi lgani ??
9/9/22, 9:01 AM - Shalin: Tut  kha hoegi ??
9/9/22, 9:41 AM - Yashwin: @919478379030 teri 3 class mei zero attendance hai ✌️✌️
9/9/22, 9:42 AM - Yashwin: And Lab ki double attendance hai shyd 🫡
9/9/22, 9:49 AM - Rohit Pec Mech: Sir ko bol Dena ki covid symptoms hai
9/9/22, 9:49 AM - Rohit Pec Mech: Hospital me hi hoon abhi ;(
9/9/22, 10:12 AM - Gursharan Kaur✨: <Media omitted>
9/11/22, 8:55 PM - Yashwin: yeh m1 specific time table bnadiya
9/11/22, 8:55 PM - Yashwin: <Media omitted>
9/11/22, 8:56 PM - Yashwin: group dp mei daaldo
9/11/22, 8:56 PM - Ishroop changed this group's icon
9/11/22, 8:56 PM - Yashwin: ismei friday ka PPC aur NCR ka tut reh gya
9/11/22, 9:06 PM - Rohit Pec Mech: Yaar yashwin.
9/11/22, 9:06 PM - Rohit Pec Mech: Perfection 😭🤝
9/11/22, 9:06 PM - Rohit Pec Mech: Thank you
9/11/22, 9:07 PM - Yashwin: No problem ✌️
9/11/22, 9:12 PM - YUDHISHTER RANA Pec Mech: The god
9/13/22, 6:56 PM - Yashwin: HMT ka second prac kaunsa hai
9/13/22, 6:57 PM - Ishroop: <Media omitted>
9/13/22, 6:57 PM - Ishroop: Ye
9/13/22, 9:35 PM - Gursharan Kaur✨: yaar kisi ne exp 2 complete krliya hmt ka ?
9/13/22, 9:37 PM - Yashwin: Likhne ka try jaari hai but merepass readings nahi hai
9/13/22, 9:39 PM - Gursharan Kaur✨: Kisne readings note ki thi last time ??
9/13/22, 9:41 PM - Gursharan Kaur✨: <Media omitted>
9/14/22, 8:28 AM - Gursharan Kaur✨: Kisi ne calculations ki 2nd exp ki?? 🤌
9/14/22, 8:28 AM - Yashwin: Mera first bhi complete nahi hai
9/14/22, 8:28 AM - Gursharan Kaur✨: Calculations??
9/14/22, 8:28 AM - Gursharan Kaur✨: Yaar Aaj file ni check karwate fir ...
9/14/22, 8:28 AM - Gursharan Kaur✨: 🥲
9/14/22, 8:35 AM - Yashwin: Sir ko request karlebge
9/14/22, 8:42 AM - Gursharan Kaur✨: Hn sir ko bol denge k sir ek do din mein submit krdenge
9/14/22, 9:24 AM - Ishroop: Dear Student,

Today you have a lab right? Are the students coming?
9/14/22, 9:24 AM - Ishroop: Btao kya bolu sir ko
9/14/22, 9:24 AM - Gursharan Kaur✨: Nhi jaate yaar
9/14/22, 9:24 AM - Gursharan Kaur✨: Assignments bna lenge pe ki bhi and hmt ki bhi 🥲
9/14/22, 9:25 AM - Kshitiz Sharma Mech: Chle jaate h prr file ni check krwaenge
9/14/22, 9:25 AM - Ishroop: Warna we can do one thing ki sir ko boldein ki challe jaate
9/14/22, 9:25 AM - Ishroop: And only first practical kra hai
9/14/22, 9:25 AM - Ishroop: Second mein kaha se likhna ki confusion thi
9/14/22, 9:25 AM - Ishroop: And graph etc ki bhi
9/14/22, 9:25 AM - Ishroop: Ye bol sakte
9/14/22, 9:25 AM - Gursharan Kaur✨: 2 hrs jayenge bhyi 🥲
9/14/22, 9:25 AM - Ishroop: And sab first practical krlo
9/14/22, 9:25 AM - Gursharan Kaur✨: Agar ek baar Chle gaye toh
9/14/22, 9:25 AM - Ishroop: Yaar sir krne hi dete jo krna
9/14/22, 9:26 AM - Gursharan Kaur✨: Vo toh done h !
9/14/22, 9:26 AM - Ishroop: Lab mein Beith ke kr lenge kaam
9/14/22, 9:26 AM - Ishroop: Baaki if everybody doesnt want to go to batao
9/14/22, 9:26 AM - Gursharan Kaur✨: Fir chle jate !!! Okay ...
9/14/22, 9:26 AM - Ishroop: Yus
9/14/22, 9:26 AM - Ishroop: Jaakr starting mein sun lenge then apna apna kaam kr lenge and in turns readings le aayenge
9/14/22, 9:26 AM - Ishroop: Works?????
9/14/22, 9:27 AM - Gursharan Kaur✨: Cool!!
9/14/22, 9:28 AM - YUDHISHTER RANA Pec Mech: koi assignment aaj to ni submit karni?
9/14/22, 9:28 AM - Gursharan Kaur✨: Nhi
9/14/22, 9:29 AM - YUDHISHTER RANA Pec Mech: ok
9/14/22, 9:37 AM - Ishroop: Sir we will be coming to the lab at 10 but a lot of students have not been able to complete second practical because there were certain confusion regarding the practical.
9/14/22, 9:37 AM - Ishroop: Sure. No problem.
9/14/22, 9:37 AM - Ishroop: :))
9/14/22, 10:18 AM - Ishroop added Sparsh Pec
9/14/22, 10:11 AM - Gursharan Kaur✨: Bhyi aajo jis jisne attendance lgwani h
9/14/22, 10:15 AM - Gursharan Kaur✨: Jis jis ki proxy lgayi h hamne
Vo saare pe ki assignment krke bhej dena
Wrna next time se koi proxy ni lgegi .....
9/14/22, 10:17 AM - Rohit Pec Mech: Attendance laga dena yaar
9/14/22, 10:17 AM - Rohit Pec Mech: Done done 👍🏻👍🏻
9/14/22, 10:37 AM - Kshitiz Sharma Mech: <Media omitted>
9/14/22, 10:38 AM - Yashwin: <Media omitted>
9/15/22, 8:22 AM - Yashwin: @916239579405 kamal sir se ek vaar puchlena aaj tut ki timings change ka bol rahe the
9/15/22, 8:23 AM - Ishroop: Bc
9/15/22, 8:23 AM - Ishroop: Yaar kamal sir ka har baar ka hai 😑
9/15/22, 8:23 AM - Ishroop: Ruk krti mein baat
9/15/22, 8:23 AM - Yashwin: Na woh sir bol rahe the 11-12 ka
9/15/22, 8:23 AM - Yashwin: Class mei convert kardenge tut ko
9/15/22, 8:23 AM - Ishroop: This message was deleted
9/15/22, 8:24 AM - Ishroop: Won't be possible
9/15/22, 8:24 AM - Yashwin: Karle baat
9/15/22, 8:24 AM - Ishroop: M2 m3 dono ka tut hai
9/15/22, 8:24 AM - Ishroop: Hn krti mein ruk
9/15/22, 8:24 AM - Yashwin: Ha woh sir ne bola tha he will talk to the teachers
9/15/22, 8:24 AM - Ishroop: Abhi i am in class
9/15/22, 8:24 AM - Ishroop: 9 baje hi krungi ab baat
9/15/22, 8:25 AM - Yashwin: Chal iske baad karlio
9/15/22, 8:25 AM - Ishroop: Hnn dw
9/15/22, 8:57 AM - Yashwin: Proxy lgadena pls
9/15/22, 8:57 AM - Ishroop: Kismein????
9/15/22, 8:57 AM - Yashwin: FM mei
9/15/22, 8:58 AM - Gursharan Kaur✨: Is that even possible ??
9/15/22, 8:58 AM - Yashwin: Koi yes sir boldena peeche se🫡
9/15/22, 8:58 AM - Ishroop: Keise lagti hai fm mein proxy
9/15/22, 8:58 AM - Ishroop: Mujhe bhi batao
9/15/22, 8:58 AM - Ishroop: Laundo ko bolo fir
9/15/22, 8:58 AM - Gursharan Kaur✨: ++
9/15/22, 8:58 AM - Ishroop: Wohi mein soch rhi saala roz 8 baje kyo aate jab na sunna na kuch aur
9/15/22, 8:58 AM - Ishroop: 😂😂😂😂😂
9/15/22, 8:58 AM - Yashwin: Mei bhar khada hu khidki se boldeta 🌝
9/15/22, 8:59 AM - Gursharan Kaur✨: Wahi toh 🥲🤦‍♀️
9/15/22, 8:45 PM - Gursharan Kaur✨: Yaar kisi ne pe ki assignment krli ???
9/15/22, 9:23 PM - Sagar: G2 can submit their assignment on monday
9/15/22, 9:23 PM - Sagar: @916239579405
9/15/22, 9:23 PM - Sagar: You know what to do😌
9/15/22, 9:24 PM - Ishroop: I'll suggest don't do anything
9/15/22, 9:24 PM - Ishroop: As much as I wanna too
9/15/22, 9:24 PM - Ishroop: Coz see this is only going to fuel g2 against g1
9/15/22, 9:24 PM - Ishroop: And they are already pissed about the teachers
9/15/22, 9:25 PM - Ishroop: But if u guys still all want to theek hai I'll say
9/15/22, 9:25 PM - Sagar: Nice
9/15/22, 9:32 PM - Gursharan Kaur✨: Rehne de bro !
9/15/22, 9:32 PM - Gursharan Kaur✨: Kyu risk lena
9/15/22, 9:33 PM - Gursharan Kaur✨: Ek assignment submit krna on time is way more easier than being taught by Soni ..,🥲
9/15/22, 9:33 PM - Sagar: Okay
9/15/22, 9:40 PM - Ishroop: Wohi 🥲
9/15/22, 9:42 PM - YUDHISHTER RANA Pec Mech: Fluid mechanics ki practical file se related kya kaam hai kal ?
9/15/22, 9:43 PM - Yashwin: Ha koi layout poora bana hua bhejdo
9/15/22, 9:44 PM - Ishroop: Bas layout likh ke le aana
9/15/22, 9:44 PM - Ishroop: Tut sheet I'll suggest mt mention krna koi bhi. At max hua to bol denge ki sir mili thi but ghar pe hai wo.
9/15/22, 9:44 PM - Ishroop: Baaki jeise sabko sahi lage
9/15/22, 9:52 PM - Shalin: This message was deleted
9/15/22, 10:00 PM - Shalin: Assignment ho Jaye to please  share kr dena 🙏🙏
9/16/22, 8:59 AM - YUDHISHTER RANA Pec Mech: RAC lab mein aa jao saare
9/16/22, 9:06 AM - Yashwin: <Media omitted>
9/16/22, 9:06 AM - Yashwin: <Media omitted>
9/16/22, 9:07 AM - Yashwin: Ismei tut 1 mei 7-10
9/16/22, 9:07 AM - Yashwin: And tut 2 complete
9/16/22, 9:07 AM - Yashwin: Need to complete this in lab
9/16/22, 9:12 AM - Ishroop: Answers mil rahe hain?
9/16/22, 9:12 AM - YUDHISHTER RANA Pec Mech: https://holooly.com/solutions/capillary-rise-in-a-tube-to-what-height-above-the-reservoir-level-will-water-at-20c-rise-in-a-glass-tube-such-as-that-shown-in-fig-2-7-if-the-inside-diameter-of-the-tube-is-1-6-mm-problem/
9/16/22, 9:12 AM - Ishroop: Suno
9/16/22, 9:12 AM - Ishroop: Tut hai
9/16/22, 9:13 AM - YUDHISHTER RANA Pec Mech: Tut 1 Q-9
9/16/22, 9:13 AM - Ishroop: To chup krke 10 baje nikal jaana
9/16/22, 9:13 AM - Ishroop: Tut ek ghante ka hi hota
9/16/22, 9:13 AM - Yashwin: Jab tak tut sheet khtm nahi hogi yeh jaane nahi dega
9/16/22, 9:14 AM - Kshitiz Sharma Mech: <Media omitted>
9/16/22, 9:14 AM - Ishroop: Bccc
9/16/22, 9:17 AM - Rohit Pec Mech: Attendance laga dena pls 😔
9/16/22, 9:18 AM - Ishroop: +++
9/16/22, 9:18 AM - Yashwin: @916239579405 m1 ka toh tut hi nahi hai poore g1 and g2 ka nahi hota
9/16/22, 9:18 AM - Yashwin: Jo aaj tut le rha yeh nahi lagta lagyega
9/16/22, 9:18 AM - Rohit Pec Mech: Dekhlena
9/16/22, 9:18 AM - Rohit Pec Mech: Agar lag paaye to
9/16/22, 9:18 AM - Yashwin: Ok
9/16/22, 9:19 AM - Ishroop: Mtlb????
9/16/22, 9:24 AM - Yashwin: Yeh jo kamal sir ne message bheja
9/16/22, 9:25 AM - Ishroop: Kl laga to tha
9/16/22, 9:26 AM - Yashwin: Ha sir ko bolna padega ki class hai 2-3
9/16/22, 9:26 AM - YUDHISHTER RANA Pec Mech: https://holooly.com/solutions/pressure-in-tank-with-two-fluids-oil-with-a-specific-gravity-of-0-80-forms-a-layer-0-90-m-deep-in-an-open-tank-that-is-otherwise-filled-with-water-the-total-depth-of-water-and-oil-is-3-m-what-is-the/
9/16/22, 9:26 AM - YUDHISHTER RANA Pec Mech: This message was deleted
9/16/22, 9:26 AM - Ishroop: Kamal sir ki hi class hai aaj 2 se 3
9/16/22, 9:27 AM - YUDHISHTER RANA Pec Mech: Tut sheet 2 Q-2
9/16/22, 9:27 AM - Yashwin: Ncer ka tut nahi hai
9/16/22, 9:29 AM - Ishroop: Gursharan ne bola tha nahi hai aaj
9/16/22, 9:29 AM - Yashwin: Yeh zaroori tha bolna 😩
9/16/22, 9:31 AM - Yashwin: Ab class lagani padegi
9/16/22, 9:32 AM - Kshitiz Sharma Mech: <Media omitted>
9/16/22, 9:33 AM - Gursharan Kaur✨: Yaar khtm hojega aaj hi brrhiya
9/16/22, 9:33 AM - Gursharan Kaur✨: Wrna kuchh pta ni uska kab reschedule krde
9/16/22, 9:36 AM - Shalin: <Media omitted>
9/16/22, 9:54 AM - Shalin: <Media omitted>
9/16/22, 10:06 AM - Kshitiz Sharma Mech: https://holooly.com/solutions/load-lifted-by-a-hydraulic-jack-a-hydraulic-jack-has-the-dimensions-shown-if-one-exerts-a-force-f-of-100-n-on-the-handle-of-the-jack-what-load-f2-can-the-jack-support-neglect-lifter-weight-probl/
9/16/22, 10:06 AM - Kshitiz Sharma Mech: T2 1
9/16/22, 10:23 AM - Shalin: This message was deleted
9/16/22, 1:05 PM - Yashwin: Yaar aaj assignment submit nahi kar rahe PE ki sir se baat karlenege
9/16/22, 1:11 PM - Shalin: Jldi confirm kr lo ??
9/16/22, 1:11 PM - Gursharan Kaur✨: Confirm krke btado ek baar
9/16/22, 1:12 PM - Yashwin: Mei gbm mei hu club ki
9/16/22, 1:12 PM - Yashwin: Ek baar sir se baat hi karlo
9/16/22, 1:13 PM - Yashwin: Varna yaad toh hoga nahi koi submit mat karna
9/16/22, 1:59 PM - Kshitiz Sharma Mech: We have to submit the assignment today
9/16/22, 2:04 PM - Ishroop: Bhai wtf
9/16/22, 2:04 PM - Ishroop: 😑
9/16/22, 2:06 PM - Yashwin: Usne kha aaj hi krdena
9/16/22, 2:07 PM - Ishroop: Arrey to convince kro yaarrr
9/16/22, 2:07 PM - Ishroop: 🥲🥲🥲
9/16/22, 2:07 PM - Yashwin: Baad mei karoge toh mujhe nahi lagta kuch bolega
9/17/22, 6:58 PM - Shalin: This message was deleted
9/17/22, 6:59 PM - Shalin: This message was deleted
9/17/22, 7:08 PM - Sparsh Pec: Kya Krna h?
9/17/22, 7:11 PM - Shalin: Khud soch
College Mai aa gya
9/17/22, 7:11 PM - Shalin: Kuch to socha kr ??
9/17/22, 7:12 PM - Sparsh Pec: <Media omitted>
9/17/22, 7:13 PM - Shalin: Chll chorr
Kuch nhi krna hai 🤣🤣
9/17/22, 7:13 PM - Sparsh Pec: Pls btade
9/17/22, 7:13 PM - Shalin: Time nhi hai
9/17/22, 7:14 PM - Shalin: Match dekhna hai
9/17/22, 7:14 PM - Shalin: 🤣🤣
9/17/22, 7:14 PM - Shalin: Bye bye 🤣🤣
9/18/22, 11:24 AM - YUDHISHTER RANA Pec Mech: Kal kisi assignment ki submission hai?
9/18/22, 11:24 AM - Gursharan Kaur✨: Hmt
9/18/22, 11:27 AM - YUDHISHTER RANA Pec Mech: ohk
9/18/22, 9:04 PM - Shalin: Kl Hmt ki assignment submit krni hai ??
9/18/22, 9:04 PM - Shalin: ??
9/18/22, 9:04 PM - Sparsh Pec: Nope
9/18/22, 9:05 PM - Sparsh Pec: Uski date extend hogai 20 h ab
9/18/22, 9:05 PM - Shalin: OK 👍
9/18/22, 9:06 PM - Gursharan Kaur✨: Ye kisne bola ??
9/18/22, 9:06 PM - Gursharan Kaur✨: And kab hua ye ??
9/18/22, 9:06 PM - Shalin: Bta bro ??
9/18/22, 9:07 PM - Sparsh Pec: Bhai bar bar thodi bolunga
9/18/22, 9:07 PM - Gursharan Kaur✨: @918054349284
9/18/22, 9:07 PM - Shalin: Janta proof maang rhi hai
9/18/22, 9:07 PM - Gursharan Kaur✨: @918054349284
9/18/22, 9:08 PM - Ishroop: Bhai sirf class postpone hui hai, assignment ki deadline nahi
9/18/22, 9:08 PM - Shalin: Teri Sarkar nhi bnegi
9/18/22, 9:09 PM - Sparsh Pec: Arreyy yrr 🤦‍♂️
9/18/22, 9:09 PM - YUDHISHTER RANA Pec Mech: Koi scene hai ki hoje?
9/18/22, 9:09 PM - Ishroop: Idk
9/18/22, 9:10 PM - Shalin: This message was deleted
9/18/22, 9:10 PM - Shalin: This message was deleted
9/18/22, 9:26 PM - Shalin: @CR kl POM ki class hai ??
9/18/22, 9:26 PM - Shalin: ++
9/18/22, 9:26 PM - Gursharan Kaur✨: Hn hai
9/18/22, 11:57 PM - Rohit Pec Mech: Kal kon kon si assignment submissions hai ?
9/19/22, 8:50 AM - Yashwin: @916239579405 Debashish sir ko puchle ki kal de sakte assignment kyuki transient state nahi karwaya abhi tak
9/19/22, 8:50 AM - Yashwin: Aur 7th ke baad uske hi question hai
9/19/22, 8:50 AM - Kshitiz Sharma Mech: This message was deleted
9/19/22, 8:50 AM - Yashwin: And phir aaj aana nahi padega college
9/19/22, 8:53 AM - Sparsh Pec: ++
9/19/22, 8:57 AM - Kshitiz Sharma Mech: Shyd krvaya h transient state🙄
9/19/22, 8:58 AM - Gursharan Kaur✨: ++
9/19/22, 9:03 AM - Yashwin: Yaar
9/19/22, 9:03 AM - Yashwin: Aisa na bol
9/19/22, 9:50 AM - Shalin: Agr extend ho skta to krwa do ??
9/19/22, 9:50 AM - Shalin: Hmt ki Assignment ??
9/19/22, 9:55 AM - YUDHISHTER RANA Pec Mech: kisi ko book mili DOMS ki,same edition jo sir ne bataya tha?
9/19/22, 10:22 AM - Gursharan Kaur✨: Hn
9/19/22, 1:15 PM - YUDHISHTER RANA Pec Mech: Kahan submit karni hai hmt ki assignment?
9/20/22, 11:42 AM - Gursharan Kaur✨: <Media omitted>
9/20/22, 11:43 AM - Gursharan Kaur✨: <Media omitted>
9/20/22, 11:19 PM - Gursharan Kaur✨: yaar issmein kisi ko pta h k inhone ek hi row kyu likhi h readings wali?
9/20/22, 11:19 PM - Ishroop: No idea 🥲
9/20/22, 11:19 PM - Gursharan Kaur✨: and exp 3 ka kiya kisi ne kuchh ??
9/20/22, 11:19 PM - Gursharan Kaur✨: left side ??
9/20/22, 11:20 PM - Gursharan Kaur✨: @everyone
9/20/22, 11:20 PM - Ishroop: Nope
9/20/22, 11:20 PM - Gursharan Kaur✨: kal file check ni krwani ?
9/20/22, 11:20 PM - Ishroop: Bc 🥲
9/20/22, 11:20 PM - Kshitiz Sharma Mech: Shyd ye last wali row ho
9/20/22, 11:20 PM - Ishroop: Pending assignments kr rhi 🥲🥲🥲
9/20/22, 11:20 PM - Gursharan Kaur✨: baaki ki ???
9/20/22, 11:20 PM - Gursharan Kaur✨: 🥹🥹
9/20/22, 11:21 PM - Kshitiz Sharma Mech: Pta ni yrr mai to khud yhii krra huu
9/20/22, 11:21 PM - Gursharan Kaur✨: @919876326716 tune kiya kuchh ?
9/21/22, 12:06 AM - Shalin: <Media omitted>
9/21/22, 12:06 AM - Shalin: Ye 2nd exp ka hai ??
9/21/22, 1:09 AM - Ishroop: Yaar exp 2 and 3 ke lhs koi krle to please bhej dena :")
9/21/22, 1:09 AM - Gursharan Kaur✨: ++
9/21/22, 9:38 AM - Yashwin: Aaj ki lab lagani hai na ?
9/21/22, 9:39 AM - Sparsh Pec: Yes broo
No attendance 🥲
9/21/22, 9:39 AM - Gursharan Kaur✨: Abe saale Teri proxiyan bhr bhr k lagi huyi hain
9/21/22, 9:39 AM - Yashwin: Ha
9/21/22, 9:39 AM - Sparsh Pec: Then no problem
Short nhi to sb bdiya
9/21/22, 9:40 AM - Rohit Pec Mech: Laga hi lete hain
9/21/22, 9:40 AM - Rohit Pec Mech: Aaye hain to
9/21/22, 9:40 AM - Gursharan Kaur✨: File check krwaani ??
9/21/22, 9:41 AM - Yashwin: Teri file complete hai
9/21/22, 9:42 AM - Rohit Pec Mech: Na
9/21/22, 9:42 AM - Gursharan Kaur✨: Almost bs kr rakhi h pta ni theek h ya nhi ...🥲
9/21/22, 9:42 AM - Rohit Pec Mech: No
9/21/22, 9:59 AM - Shalin: This message was deleted
9/21/22, 9:59 AM - Shalin: Nhi
9/21/22, 10:46 AM - Sagar: <Media omitted>
9/21/22, 10:38 AM - Yashwin: <Media omitted>
9/21/22, 10:38 AM - Yashwin: <Media omitted>
9/21/22, 10:45 AM - Sankalp Singla: This message was deleted
9/21/22, 10:49 AM - Shalin: <Media omitted>
9/21/22, 10:52 AM - Gursharan Kaur✨: Exp3
9/21/22, 11:37 AM - Ishroop: <Media omitted>
9/21/22, 11:38 AM - Gursharan Kaur✨: Ye kaunse ki hain ??
9/21/22, 11:50 AM - Ishroop: 2nd only
9/21/22, 11:51 AM - Ishroop: Sir priyanshu ki file check kr rahe thei
9/21/22, 11:51 AM - Ishroop: To humme aakr kehte ki graph nahi banaaya and wo jo 3 number thei, grashoff etc waale wo use krke h nikaalna theoretical waala
9/21/22, 11:52 AM - Gursharan Kaur✨: Bhyi ye jyada ni hora 🥲🤦‍♀️
9/21/22, 1:32 PM - Shalin: This message was deleted
9/21/22, 6:55 PM - Shalin: This message was deleted
9/21/22, 6:56 PM - Shalin: This message was deleted
9/21/22, 9:59 PM - Shalin: Hmt ki file kl to nhi submit kr rha koi ??
9/21/22, 9:59 PM - Shalin: kl to nhi submit krni hai ??
9/21/22, 10:25 PM - Shalin: This message was deleted
9/21/22, 10:25 PM - Shalin: This message was deleted
9/21/22, 10:34 PM - YUDHISHTER RANA Pec Mech: kal hi kar diyo
9/21/22, 10:35 PM - Shalin: Nhi krna kl
9/21/22, 10:35 PM - Shalin: Thbi to confirm krna hai
9/21/22, 10:35 PM - YUDHISHTER RANA Pec Mech: to puch kyun raha
9/21/22, 10:36 PM - Shalin: Mereko nhi pta baki log kb kr rhe hai submit
9/21/22, 10:37 PM - Shalin: Chll chorr
9/21/22, 10:37 PM - Shalin: OK 👍
9/22/22, 7:26 AM - Yashwin: Yaar aaj agar kamal sir bole ki do ghante classes saath  mei toh pls mana kardena
9/22/22, 7:26 AM - Yashwin: Ek ghante ki class toh lagayi nahi jaati
9/22/22, 7:33 AM - Gursharan Kaur✨: 😂😂😂😂
9/22/22, 9:56 AM - Ishroop: Mass bunk fir tut???
9/22/22, 9:56 AM - Ishroop: Btao @919876326716 @916239412997
9/22/22, 10:24 AM - Sparsh Pec: Yesss 🥳
9/22/22, 10:29 AM - Ishroop: 😂😂😂
9/22/22, 11:45 AM - Yashwin: Tomorrow PE class 10-11
9/22/22, 11:45 AM - Yashwin: @916239579405 on G1
9/22/22, 11:46 AM - Ishroop: Bkl
9/22/22, 11:46 AM - Ishroop: 😑😤
9/22/22, 10:39 PM - Ishroop: Kal PE ki class hai?
9/22/22, 10:39 PM - Ishroop: Bataana bhai
9/22/22, 10:39 PM - Sparsh Pec: Yes
9/22/22, 10:39 PM - Sparsh Pec: No
9/22/22, 10:39 PM - Sparsh Pec: Chose one
9/22/22, 10:39 PM - Yashwin: Sir ne toh bola tha
9/22/22, 10:40 PM - Yashwin: Nahi lagani toh btado
9/22/22, 10:40 PM - Ishroop: Yaad nahi krwaayenge
9/22/22, 10:40 PM - Yashwin: 😏
9/22/22, 10:40 PM - Ishroop: Ho gyi class to Ho gayi
9/22/22, 10:51 PM - Shalin: Kl tut hai ya practical ??
9/22/22, 10:57 PM - Yashwin: Kal hi pata lagega
9/22/22, 10:58 PM - YUDHISHTER RANA Pec Mech: sir kahan maanne wale,official mass bunk hoje ya fir
9/22/22, 10:58 PM - YUDHISHTER RANA Pec Mech: even better
9/22/22, 11:00 PM - Shalin: Mass bunk best hai
9/22/22, 11:00 PM - Shalin: Kl pta chl jayega
OK 👍
9/23/22, 9:00 AM - Rohit Pec Mech: Proxy laga sakte ho
9/23/22, 9:04 AM - Yashwin: Kabhi class bhi lgale
9/23/22, 9:04 AM - Shalin: Kha ho rhi hai class
9/23/22, 9:04 AM - Yashwin: Rac lab
9/23/22, 9:04 AM - Kshitiz Sharma Mech: <Media omitted>
9/23/22, 9:04 AM - YUDHISHTER RANA Pec Mech: Abhi attendence to ni hori?
9/23/22, 9:05 AM - Sparsh Pec: I'll be reaching in 20
Raining 🌧️⛈️🌩️
9/23/22, 9:06 AM - YUDHISHTER RANA Pec Mech: Same here
9/23/22, 9:06 AM - Ishroop: Bc fir se tur
9/23/22, 9:06 AM - Ishroop: Tut*
9/23/22, 9:06 AM - Ishroop: Sir se puchho yaar practical kab hona
9/23/22, 9:17 AM - Rohit Pec Mech: Ye kaha hai
9/23/22, 9:17 AM - Rohit Pec Mech: Same
9/23/22, 9:59 AM - Shalin: Iski specification send kro
9/23/22, 10:00 AM - Shalin: Exp 3 ki specification ??
9/23/22, 2:33 PM - Sagar: Debasish sir said ki jitni late file check karwayenge utne kam marks lagenge
9/23/22, 2:34 PM - Sagar: Next week se 6 out of 10 milenge experiment ke marks
9/23/22, 2:34 PM - Sagar: Agar same day check krvayenge toh 9
9/23/22, 2:54 PM - Ishroop: Meine nahi di hai abhi
9/23/22, 2:54 PM - Ishroop: Bta kya kru
9/23/22, 2:54 PM - Ishroop: Agar calculation complete hai to bhejdo
9/23/22, 2:54 PM - Ishroop: I'll submit aaj hi
9/23/22, 2:54 PM - Yashwin: Mere pass file hi nahi hai
9/23/22, 2:54 PM - Ishroop: Bc
9/23/22, 2:54 PM - Yashwin: Varna bhejdeta
9/23/22, 2:54 PM - Ishroop: Sir ko bolo Monday sab de denge
9/23/22, 2:54 PM - Ishroop: Tu suit kr aaya hai kya?
9/23/22, 2:55 PM - Ishroop: Submit*
9/23/22, 3:00 PM - Yashwin: Na
9/23/22, 4:24 PM - Shalin: File jldi submit krne ko bola hai
9/23/22, 4:24 PM - Shalin: Attendance km hone pe marks kat rhe hain
9/23/22, 4:24 PM - Shalin: Aur kuch nhi hai
9/23/22, 4:25 PM - Shalin: This message was deleted
9/25/22, 11:04 PM - YUDHISHTER RANA Pec Mech: Koi legend jisne fm ki assignment karli ho🙂?
9/25/22, 11:05 PM - Ishroop: Kl chutti hai
9/25/22, 11:05 PM - YUDHISHTER RANA Pec Mech: Even better
9/25/22, 11:05 PM - Ishroop: :)
9/25/22, 11:06 PM - YUDHISHTER RANA Pec Mech: But waise puchra tha
9/25/22, 11:06 PM - Ishroop: Ohhhh
9/25/22, 11:06 PM - Ishroop: In that case.....
9/25/22, 11:06 PM - Ishroop: +++
9/25/22, 11:12 PM - Shalin: Online submit krni hai
9/25/22, 11:12 PM - Shalin: Offline bhi krni hai ??
9/26/22, 9:46 PM - Yashwin: <Media omitted>
9/26/22, 9:48 PM - Gursharan Kaur✨: Yaar pehle toh ye clear kro k given, assumptions etc etc likhna h
9/26/22, 9:48 PM - Shalin: Kisne kha likhna hai ??
9/26/22, 9:52 PM - Gursharan Kaur✨: @919876326716 kaisa krna h ??
9/26/22, 9:58 PM - Gursharan Kaur✨: Bhyi ab koi mt likhna ....
9/26/22, 9:58 PM - Gursharan Kaur✨: Ye sb
9/26/22, 9:59 PM - Yashwin: Jaisa pdf mei hai waisa likh do
9/26/22, 9:59 PM - Gursharan Kaur✨: +++
9/26/22, 10:00 PM - Gursharan Kaur✨: True true !!
9/26/22, 10:00 PM - Sparsh Pec: Abe oyee, copy nhi krta me 😒
9/26/22, 10:01 PM - Yashwin: Ha theek hai na khud kar better understanding hogi
9/26/22, 10:01 PM - Shalin: This message was deleted
9/26/22, 10:01 PM - Shalin: Strict rules
Copy paste
9/26/22, 10:01 PM - Shalin: 😤😤
9/26/22, 10:02 PM - Sparsh Pec: <Media omitted>
9/26/22, 10:02 PM - Rohit Pec Mech: <Media omitted>
9/26/22, 10:25 PM - YUDHISHTER RANA Pec Mech: Aadarshwaadi log🙏
9/27/22, 11:02 AM - Shalin: <Media omitted>
9/27/22, 11:42 AM - Gursharan Kaur✨: 3rd exp mein graph bnana hai ??
9/27/22, 11:43 AM - Ishroop: Sab M1 waale kl hi de dena file
9/27/22, 11:43 AM - Gursharan Kaur✨: Kuchh logo ki file check ho chuki h
9/27/22, 11:43 AM - Gursharan Kaur✨: And kuchh aaj jare hain ...
9/27/22, 11:44 AM - Ishroop: Hn unhi ke liye bol rahi practical file complete krke le aayenge kal
9/27/22, 11:45 AM - Gursharan Kaur✨: Dekhlo agar koi ni krwayega aaj toh ham bhi nhi jaate otherwise we will go around 12
9/27/22, 11:45 AM - Ishroop: Hn tabhi baat kr rahi
9/27/22, 11:45 AM - Ishroop: Bata do sab kal hi de denge
9/27/22, 11:45 AM - Yashwin: Sir se baat ki thi
9/27/22, 11:46 AM - Yashwin: Unhone class ke baad bol
9/27/22, 11:46 AM - Yashwin: Bola abhi check karke dedenge
9/27/22, 11:50 AM - Ishroop: 🥲
9/27/22, 11:50 AM - Ishroop: Ok chal
9/27/22, 11:50 AM - Ishroop: Krwa lo jinhe krwaani
9/27/22, 11:52 AM - YUDHISHTER RANA Pec Mech: Arey 😶
9/27/22, 11:53 AM - Ishroop: Mein kl hi krwaungi
9/27/22, 11:53 AM - YUDHISHTER RANA Pec Mech: Chalo koi to hai kal wala
9/27/22, 11:53 AM - Sparsh Pec: Yr 🫂
9/27/22, 12:59 PM - Rohit Pec Mech: Submit kahan karni hai assignment
9/27/22, 12:59 PM - Rohit Pec Mech: FM ki ?
9/27/22, 12:59 PM - Yashwin: Rac
9/27/22, 10:24 PM - Yashwin: <Media omitted>
9/27/22, 10:24 PM - Gursharan Kaur✨: iska graph dekhlena yaar
9/27/22, 10:24 PM - Gursharan Kaur✨: jo pic click ki thi na uss din vo galat thi
9/27/22, 10:24 PM - Yashwin: Ha bna rha
9/27/22, 10:25 PM - Gursharan Kaur✨: bheju??
9/27/22, 10:25 PM - Yashwin: Bhej
9/27/22, 10:25 PM - Yashwin: But values alag hongi
9/27/22, 10:26 PM - Gursharan Kaur✨: Kis se ??
9/27/22, 10:26 PM - Yashwin: Graph ki
9/27/22, 10:26 PM - Gursharan Kaur✨: Are M1 ki toh same hi hain na apni ...
9/27/22, 10:26 PM - Yashwin: Bhejde ek baar
9/27/22, 10:27 PM - Gursharan Kaur✨: rukja meri file ishroop k paas h vo bhejti
9/27/22, 11:20 PM - Gursharan Kaur✨: <Media omitted>
9/28/22, 10:29 AM - Yashwin: <Media omitted>
9/28/22, 10:47 AM - Gursharan Kaur✨: <Media omitted>
9/28/22, 11:28 AM - Yashwin: <Media omitted>
9/28/22, 2:09 PM - Gursharan Kaur✨: Yaar meri hmt ki prac file toh ni h kisi k paas ?
9/28/22, 2:45 PM - Shalin: This message was deleted
9/28/22, 3:55 PM - Gursharan Kaur✨: <Media omitted>
9/28/22, 3:55 PM - Gursharan Kaur✨: <Media omitted>
9/28/22, 3:57 PM - Gursharan Kaur✨: This message was deleted
9/28/22, 3:57 PM - Gursharan Kaur✨: This message was deleted
9/28/22, 5:30 PM - Shalin: This message was deleted
9/28/22, 5:40 PM - Shalin: This message was deleted
9/28/22, 5:40 PM - Shalin: This message was deleted
9/28/22, 5:41 PM - Shalin: This message was deleted
9/29/22, 11:03 AM - Mohak Gandhi Pec: <Media omitted>
9/29/22, 11:17 AM - Ishroop: <Media omitted>
9/29/22, 11:17 AM - Ishroop: <Media omitted>
9/29/22, 11:17 AM - Ishroop: Kl waale exp mein precautions add kr lena
9/29/22, 11:18 AM - Ishroop: <Media omitted>
9/29/22, 11:18 AM - Ishroop: - Debashish sir
9/29/22, 11:20 AM - Ishroop: Also correction hai:

Dia of orifice is 1.4 cm
Distance between consecutive thermocouples is 3 cm
9/29/22, 1:05 PM - Yashwin: @916239579405 cad ki class cancel karwade 🫡
9/29/22, 1:05 PM - Yashwin: Mann nahi lagane ka
9/29/22, 1:21 PM - Ishroop: Contact himank
9/29/22, 1:25 PM - Yashwin: Chal rehne de
9/29/22, 1:26 PM - Ishroop: Na na krwa le
9/29/22, 1:26 PM - Ishroop: Meri khud ki bhi tabiyat theek nahi to better if cancel ho jaaye
9/29/22, 1:26 PM - Yashwin: Na yaar lga hi lete 😂
9/29/22, 5:31 PM - Ishroop: In experiment 5 and 6, finalized orifice diameter to be considered = 2cm and NOT 1.4 cm.
9/29/22, 5:31 PM - Ishroop: - Debashish sir
9/29/22, 6:58 PM - Yashwin: Kal nahi karte PE ki assignment submit
9/29/22, 6:58 PM - Yashwin: Monday karenge
9/29/22, 6:58 PM - Yashwin: Batao ?
9/29/22, 7:23 PM - Sparsh Pec: Okayy
9/29/22, 7:29 PM - Shalin: Confirm krke batado ??
9/29/22, 7:47 PM - Yashwin: Kal sir ki class nahi hai
9/29/22, 7:48 PM - Yashwin: Na unko yaad rehta
9/29/22, 7:48 PM - Yashwin: Karne ko karlo
9/29/22, 7:48 PM - Ishroop: Cool
9/29/22, 8:01 PM - Sparsh Pec: Screenshot lelia h 🌝
9/29/22, 8:01 PM - Yashwin: <Media omitted>
9/29/22, 8:02 PM - Sparsh Pec: <Media omitted>
9/30/22, 9:01 AM - Priyanshu Mech: Come to CAD lab for the practical
9/30/22, 9:02 AM - Ishroop: Meri proxy lagge
9/30/22, 9:03 AM - Ishroop: Laga dena**
9/30/22, 9:03 AM - Ishroop: If possible
9/30/22, 9:07 AM - Sparsh Pec: On my way guys
9/30/22, 9:07 AM - Sparsh Pec: It's raining heavily 🌧️☔
9/30/22, 9:09 AM - Yashwin: See no clouds my friend
9/30/22, 9:09 AM - Gursharan Kaur✨: 😂🙄😤
9/30/22, 9:09 AM - Yashwin: Perhaps in ur dreams
9/30/22, 9:09 AM - Gursharan Kaur✨: ++
9/30/22, 9:09 AM - Ishroop: *Savage Yashwin*
9/30/22, 9:12 AM - Sparsh Pec: <Media omitted>
9/30/22, 9:25 AM - Sparsh Pec: Cad lab kidhar h ?
9/30/22, 9:25 AM - Yashwin: HMT ke opp
9/30/22, 9:48 AM - Rohit Pec Mech: Mech department?
9/30/22, 9:48 AM - Rohit Pec Mech: Nhi sorry
9/30/22, 9:48 AM - Rohit Pec Mech: FM ki lab kahan hori ?
9/30/22, 9:49 AM - YUDHISHTER RANA Pec Mech: Cad lab,roto block aaja
9/30/22, 10:01 AM - Ishroop: Koi pe ki assignment submit  kr rha???
9/30/22, 10:01 AM - Yashwin: Not me
9/30/22, 10:01 AM - Ishroop: Ya sabko boldu ki Monday kr lenge submit???
9/30/22, 10:01 AM - YUDHISHTER RANA Pec Mech: Haan
9/30/22, 10:01 AM - Yashwin: Ha informally bolde
9/30/22, 10:02 AM - Yashwin: Sir ko mat bolna
9/30/22, 10:02 AM - Ishroop: Hn wohi kuch bache postpone krwaane ke liye bol rhe thei
9/30/22, 10:02 AM - Ishroop: I said m1 to nahi de raha
9/30/22, 10:02 AM - Ishroop: To tum log bhi dekhlo monday ko kr lena submit
9/30/22, 10:36 AM - Gursharan Kaur✨: Same !!
10/2/22, 7:33 PM - Rohit Pec Mech: Kal kon kon si assignment Deni hai !!!!
10/2/22, 7:33 PM - Yashwin: FM and PE
10/3/22, 12:07 PM - Yashwin: Kal karenge pe ki submit assignment
10/3/22, 2:29 PM - Ishroop: Yaar koi kamal sir se mille to bol dena i am down with fever. Kal tak submit kr dungi
10/6/22, 8:57 AM - Shalin: Hmt ke practical ki reading group pe share kr dena
10/6/22, 9:55 AM - Gursharan Kaur✨: Guys jaana h practical k liye. ??
Who all are going acknowledge this msg asap
10/6/22, 9:56 AM - Sparsh Pec: Only if you guys are going...
10/6/22, 10:01 AM - Ishroop: Oyye chal pado yaar
10/6/22, 10:02 AM - Gursharan Kaur✨: Ham log sir se baat krke aate hain ...
10/6/22, 10:02 AM - Ishroop: Mein college kyo aayi hu fir 😂😂
10/6/22, 10:02 AM - Gursharan Kaur✨: Kyu bhyi ??
10/6/22, 10:02 AM - Gursharan Kaur✨: Tu h clg mein ?? 😂🤌
10/6/22, 10:02 AM - Ishroop: Yesss sirf ek hmt prac ke liye aayi
10/6/22, 10:03 AM - Gursharan Kaur✨: Practice bhi h shaam ko 🙂
10/6/22, 10:03 AM - YUDHISHTER RANA Pec Mech: Kitne ho tum total
10/6/22, 10:03 AM - Gursharan Kaur✨: Ham 3 toh h hi pkka
10/6/22, 10:03 AM - Gursharan Kaur✨: Aur btao kaun kaun jaara ??
10/6/22, 10:03 AM - YUDHISHTER RANA Pec Mech: Chodho yaar kya karoge jaake🙂
10/6/22, 10:03 AM - Gursharan Kaur✨: Prac lgaane ??
10/6/22, 10:03 AM - Ishroop: Mein nahi aa rhi
10/6/22, 10:03 AM - Ishroop: Midsem tak na boliyo ab
10/6/22, 10:04 AM - Gursharan Kaur✨: Ab mregi tu ...🙃
10/6/22, 10:04 AM - Ishroop: Gaand fatt rakhi yaha
10/6/22, 10:04 AM - Sankalp Singla: Sir ko bol dena xeam ka test hai
10/6/22, 10:04 AM - Ishroop: Aajaao
10/6/22, 10:04 AM - Gursharan Kaur✨: 😂😂😂😂
10/6/22, 10:04 AM - Ishroop: Oyye m serious mein nhi midsem tak
10/6/22, 10:04 AM - Gursharan Kaur✨: Hnm dekhte hain krte baat sir se
10/6/22, 10:04 AM - Ishroop: Baaki aa jaao lab
10/6/22, 10:04 AM - Sagar: <Media omitted>
10/6/22, 10:04 AM - Ishroop: Ye bol denge koi scene nahi
10/6/22, 10:04 AM - Gursharan Kaur✨: Suno aur koi Mt jaana abhi
10/6/22, 10:05 AM - Ishroop: Tu kaha hai?
10/6/22, 10:05 AM - Gursharan Kaur✨: Ham log jaake baat krte hain k sir bacho ka test hain
10/6/22, 10:05 AM - Gursharan Kaur✨: Hn hn cool
10/6/22, 10:05 AM - Rohit Pec Mech: +1
10/6/22, 10:05 AM - Ishroop: Saale intern lag gayi teri
10/6/22, 10:05 AM - Ishroop: 😂😂😂😂😂
10/6/22, 10:05 AM - YUDHISHTER RANA Pec Mech: 😬
10/6/22, 10:05 AM - Gursharan Kaur✨: Bsdk 😂
10/6/22, 10:05 AM - Gursharan Kaur✨: 🤦‍♀️
10/6/22, 10:06 AM - Rohit Pec Mech: Help karwa raha hu yaar 😭😭
10/6/22, 10:06 AM - Rohit Pec Mech: Friends ki
10/6/22, 10:06 AM - Ishroop: Jaldi pahunch hmt lab
10/6/22, 10:06 AM - Rohit Pec Mech: 😥
10/6/22, 10:06 AM - Yashwin: <Media omitted>
10/6/22, 10:08 AM - Gursharan Kaur✨: I am there 🤦‍♀️
10/6/22, 10:09 AM - Ishroop: I also
10/6/22, 10:09 AM - Ishroop: Tu lab ke andar hai...???
10/6/22, 10:12 AM - Gursharan Kaur✨: Yaaar lab hogi ab toh aajao jo jo aa sakte hain
10/6/22, 10:13 AM - Gursharan Kaur✨: Ya fir reschedule krni pdegi lab
10/6/22, 10:13 AM - Shalin: This message was deleted
10/6/22, 10:14 AM - Gursharan Kaur✨: Toh ya fir uske liye time slot 2 hrs ki decide krlo
10/6/22, 10:14 AM - Shalin: This message was deleted
10/6/22, 10:16 AM - Gursharan Kaur✨: Guys abhi cancel hogya h practical
Baad mein jo bhi hoga dekha jayega
10/6/22, 5:42 PM - Shalin: Assignment Hmt ki extend krwa do , kl submit krni hain
10/6/22, 5:44 PM - Yashwin: Sir be boldia tha araam se karna
10/6/22, 5:44 PM - Yashwin: Aadhe topic class mei nahi hue
10/6/22, 5:44 PM - Shalin: This message was deleted
10/6/22, 5:51 PM - Shalin: Ok 👍
10/6/22, 6:43 PM - Shalin: Kl Friday ya Thrusday
Kaun sa timetable
 follow chlega  ??
10/6/22, 7:12 PM - Ishroop: Friday
10/6/22, 7:20 PM - Shalin: Okk
10/6/22, 9:07 PM - YUDHISHTER RANA Pec Mech: Apne practical ka kya scene hai kal?
10/6/22, 9:55 PM - Ishroop: Oyye kal na doms ki class hai
10/6/22, 9:55 PM - Ishroop: Na cad ki keh rhe and na ncr i guess
10/6/22, 9:55 PM - Ishroop: To Kal subha fm lagaani????
10/6/22, 9:56 PM - YUDHISHTER RANA Pec Mech: Usi ke liye Maine msg likha tha
10/6/22, 9:58 PM - Ishroop: Oh ff Haan sorry
10/6/22, 9:58 PM - Ishroop: Mein just so ke uthi 🥲😂
10/6/22, 9:59 PM - YUDHISHTER RANA Pec Mech: 😂😂
10/6/22, 10:01 PM - Ishroop: Btao yaar kl nahi lagaate mein so jaungi wapis
10/6/22, 10:02 PM - Yashwin: Mei toh waise nahi aa rha
10/6/22, 10:02 PM - YUDHISHTER RANA Pec Mech: Soja
10/6/22, 10:02 PM - Ishroop: 😂😂
Pehle comfirm hone de
10/6/22, 10:03 PM - YUDHISHTER RANA Pec Mech: Tereko lagta hai koi aayega😂
10/6/22, 10:03 PM - Ishroop: @918054349284 @919478379030 btao bhai :")
10/6/22, 10:04 PM - Rohit Pec Mech: Wrong choice of people 😔
10/6/22, 10:08 PM - Ishroop: Ohh yaar Tumhaara man krta to tum pahunch jaate
10/6/22, 10:11 PM - Gursharan Kaur✨: I will go with the majority
10/6/22, 10:11 PM - Ishroop: Abhi tak to naa jaane waali hi hai
10/6/22, 10:11 PM - Ishroop: @918054349284 buddy aap reh gaye bataane ko
10/6/22, 10:56 PM - Sparsh Pec: Me NCC ke liye jara hu
So you guys are free from my side
10/6/22, 10:58 PM - Ishroop: Okiiii so kal koi nahi ja raha @918699133946
10/7/22, 8:15 AM - Gursharan Kaur✨: Pkka nhi jaara koi bhi ???
10/7/22, 8:53 AM - Sagar: Okay
10/7/22, 9:10 AM - YUDHISHTER RANA Pec Mech: No
10/7/22, 9:30 AM - Ishroop: Bhai koi nahi gaya na
10/7/22, 9:30 AM - Ishroop: 🥲🥲🥲
10/7/22, 9:36 AM - Sankalp Singla: Nope
10/10/22, 10:16 AM - Shalin: Hmt ki assignment Mid Sem ke baad deni hai
Ya sbne submit kr di ??
10/10/22, 10:17 AM - Shalin: DOMS ki class hogi Aaj ??
10/10/22, 10:18 AM - YUDHISHTER RANA Pec Mech: mid sem ka baad hmt ki
10/10/22, 3:55 PM - Yashwin: Kal kaun kaun college jaa rha
10/10/22, 3:56 PM - Yashwin: Agar chutti maar rahe bta dena
10/10/22, 3:56 PM - Yashwin: Uss hisab se aana plan karlenge
10/10/22, 10:18 PM - Sparsh Pec: Kal ka kya scene h bois
10/10/22, 10:18 PM - Sparsh Pec: And gals
10/10/22, 10:18 PM - Ishroop: Aa jaao kl
10/10/22, 10:18 PM - Ishroop: Fm and pe laga lete
10/10/22, 10:18 PM - Ishroop: At least
10/10/22, 10:19 PM - Ishroop: Cad ke liye I asked himank ki sir se baat kr sakta to, he said kal subha ek baar call kr lenge ki kl ki lab and parso ki class postpone ya cancel krwa lein
10/10/22, 10:19 PM - Sparsh Pec: Okayy
10/10/22, 10:23 PM - YUDHISHTER RANA Pec Mech: Fm mein bhi kuch fark padta ni waise sir ko
10/10/22, 10:40 PM - Ishroop: But fm ka syllabus kum krwaana
10/10/22, 10:41 PM - Ishroop: Dynamics ka bolna ki alag se le lenge test post midsems. Ki midsem mein dynamics na daalein
10/10/22, 10:41 PM - Gursharan Kaur✨: Haan please 🫠🫠🫠🫠🫠🫠
10/10/22, 10:41 PM - Gursharan Kaur✨: 😭😭😭😭
10/10/22, 10:41 PM - Gursharan Kaur✨: Itna ni ho payega bhyi ..
Aur bhi subjects hain yaar ... 🥺🥺🥺
10/10/22, 10:44 PM - Ishroop: 🥲🥲🥲
10/10/22, 10:44 PM - Ishroop: Aa jaana fir kl subha ha lekin
10/10/22, 10:44 PM - Ishroop: Mein to apni taraf se 2 3 baar bol chuki
10/10/22, 10:44 PM - Ishroop: Kal sab bolenge to shaayad sun le
10/10/22, 10:44 PM - Rohit Pec Mech: Yaar FM ka material kahan hai
10/10/22, 10:44 PM - Rohit Pec Mech: Padhai kidar se krni
10/10/22, 10:44 PM - Gursharan Kaur✨: I will try my best k uth jau tb tk :)
10/10/22, 10:45 PM - YUDHISHTER RANA Pec Mech: 1 chapter kam karne mein kya chala jaayega sir ka🥲
10/10/22, 10:45 PM - Ishroop: Idk yaar. Shaayad he is in that ki 5 ques 5 topics or smtg
10/10/22, 10:45 PM - Gursharan Kaur✨: +++
10/10/22, 10:45 PM - Ishroop: Meine bola to hai ki sir paper instead of saya gar wo 50 se le raha tha .. to 40 ka lelo
10/10/22, 10:46 PM - Gursharan Kaur✨: Bhyi ye kya h ...
Ek topic mein se 2 questions aajayenge toh kya jaara iska .... 😭😭🤦‍♀️
10/10/22, 10:46 PM - Ishroop: Amd 10 number dynamics ka class test le lena usske laga lena
10/10/22, 10:46 PM - Ishroop: No but like paper 40 marks ka bana le. 10 marks dunics waalo ki evaluation baad mein lele na like post midsem
10/10/22, 10:46 PM - Ishroop: Abhi to ussne chapter bhi nahi complete kiya
10/10/22, 10:46 PM - YUDHISHTER RANA Pec Mech: Ye test Kab Hai ab
10/10/22, 10:47 PM - Ishroop: Jo wo wednesday tak padhaayega wo sab aayega
10/10/22, 10:47 PM - YUDHISHTER RANA Pec Mech: Ye faltu ki heropanti mein faadre
10/10/22, 10:47 PM - YUDHISHTER RANA Pec Mech: Cad ne alag le rakhi hai🙂
10/10/22, 10:47 PM - Ishroop: <Media omitted>
10/10/22, 10:47 PM - Ishroop: 🥲🥲🥲🥲
10/10/22, 10:48 PM - Ishroop: @916239902903 ye sun
10/10/22, 10:48 PM - Gursharan Kaur✨: Cool!!
10/10/22, 10:49 PM - Gursharan Kaur✨: Brhiya h bhyi ..
Bs jo bhi boldo dynamics htwado bhyii midsems se ....
10/10/22, 10:49 PM - Ishroop: Mujhe to kinematics bhi nahi aati
10/10/22, 10:50 PM - YUDHISHTER RANA Pec Mech: teri baat sahi hai,bc pehle hi padhai ni hori
10/10/22, 10:50 PM - Ishroop: Weekend ke pehle tak kinetics bol rhi thi usse. Ab pata chala hai kinetics and kinematics alag alag chapters hain
10/10/22, 10:50 PM - Ishroop: 🥲🥲🥲🥲🥲
10/10/22, 10:50 PM - Gursharan Kaur✨: +++++++++++++++++++
10/10/22, 10:50 PM - YUDHISHTER RANA Pec Mech: yaar paper pass hain fir bhi padhai ni hori ye alag hi fuddupanti hai
10/10/22, 10:54 PM - Sankalp Singla: Sahi baat hai bilkul
10/11/22, 7:48 AM - Yashwin: Aaj class mei kya ho rha btadena mei nahi aa sakta
Baarish ho rahi aur bimar nahi padhna 🤧
10/11/22, 8:37 AM - Sparsh Pec: Hnn yrr mujhe bhi bta dena
It's raining heavily 🌧️🥲
10/11/22, 8:43 AM - YUDHISHTER RANA Pec Mech: Same,heavy rain here too⛈️
10/20/22, 9:22 AM - Yashwin: Tut lagani ?
10/20/22, 9:22 AM - Yashwin: PE ka
10/20/22, 9:22 AM - Ishroop: Dekhlo man to hai nahi
10/20/22, 9:23 AM - Yashwin: M1 ka hai rehne do 🌝
10/20/22, 9:23 AM - Yashwin: Class hi lgate
10/20/22, 9:23 AM - Ishroop: Works for me
10/20/22, 9:23 AM - Ishroop: Baakiyo ko mana lo :)
10/20/22, 9:50 AM - Shalin: Tut lgate hai
Class nhi lgate ??
10/20/22, 10:08 AM - Sparsh Pec: Lgri h Tut?
10/20/22, 10:09 AM - Yashwin: Ha aaja
10/20/22, 10:09 AM - Yashwin: Pe ki class bhi nahi hai shyd
10/20/22, 7:56 PM - Sparsh Pec: Guys yrr please kal class lga lete h
Vrna mera aane ka Mann nhi krega or
Tum sabko happy diwali wish bhi nhi kr paunga 🥲
10/20/22, 7:57 PM - Gursharan Kaur✨: Yahiin pe wish krde:)
10/20/22, 7:58 PM - Sparsh Pec: Yrr PPC ki or FM ki to vese bhi lgani hi h
Short h dono me or vo manenge bhi nhi end mein
10/20/22, 7:59 PM - Rohit Pec Mech: Hn
10/20/22, 7:59 PM - Rohit Pec Mech: I'll also come
10/20/22, 7:59 PM - Rohit Pec Mech: FM imp
10/20/22, 8:01 PM - YUDHISHTER RANA Pec Mech: <Media omitted>
10/20/22, 8:04 PM - Sparsh Pec: Bhai yudhishter WhatsApp tak hi tha kya humara rishta 😭
10/20/22, 8:06 PM - YUDHISHTER RANA Pec Mech: Na bhai Kal gale milke diwali wish karenge
10/20/22, 8:06 PM - YUDHISHTER RANA Pec Mech: 🫂
10/20/22, 8:09 PM - Ishroop: .
10/20/22, 8:10 PM - Ishroop: .
10/20/22, 8:10 PM - Ishroop: .
10/20/22, 8:10 PM - Ishroop: .
10/20/22, 8:10 PM - YUDHISHTER RANA Pec Mech: When u don't want to type😂
10/20/22, 8:10 PM - Ishroop: Hence Proved @919478379030 @918054349284
10/20/22, 8:10 PM - Ishroop: :)
10/20/22, 8:10 PM - Sparsh Pec: Areyy ooo
Pahunchna hota to yha btata nhi
10/20/22, 8:11 PM - Sparsh Pec: Honesty ko koi appreciate hi nhi krta
10/20/22, 8:11 PM - Ishroop: Confirmation maangi thi. Pichle convo ka context lele pehle.
10/20/22, 8:11 PM - Ishroop: Ussi confirmation ke context mein tha ki agar group pe nahi likha to chances hain ki tjm ja sakte
10/20/22, 8:12 PM - Ishroop: Agar likha hai to pata hai nahi jaaoge or at least we hope
10/20/22, 8:12 PM - Sparsh Pec: Ohhhhhhhh
10/20/22, 8:12 PM - Sparsh Pec: Aaj likha h jaane ke liye
Just to be clear 😬
10/20/22, 8:12 PM - Ishroop: Mt jaao yaar
10/20/22, 8:12 PM - Ishroop: Bc 😭
10/20/22, 8:12 PM - Ishroop: Pehle koi hmt assignment bhejdo
10/20/22, 8:12 PM - Ishroop: Fir aa jaana kal
10/20/22, 8:13 PM - Yashwin: Me not coming to college tomorrow attendance jha lag sakti pls lga dena
Thank you
10/20/22, 8:13 PM - Sparsh Pec: Doneee
10/20/22, 8:13 PM - Yashwin: Tavish waali karle
10/20/22, 8:13 PM - Ishroop: Doms mein @918054349284 me also
10/20/22, 8:13 PM - Ishroop: Galat hai wo
10/20/22, 8:13 PM - Yashwin: Sahi hai
10/20/22, 8:13 PM - Yashwin: Verified all answers myselh
10/20/22, 8:13 PM - Ishroop: Nhi mujhe sab toppers bol chuke galat hai
10/20/22, 8:14 PM - Sparsh Pec: Attendance lga dunga tumhari mein
10/20/22, 8:14 PM - Yashwin: Ok jaise marzi meine khud bhi check karke solve ki thi theek lage the
10/20/22, 8:15 PM - Sparsh Pec: She means you no topper 🥲
10/20/22, 8:15 PM - Ishroop: Aisa nahi hai.
10/20/22, 8:15 PM - Ishroop: Yaar agar doubt hota to dekh hi leti mein kahi se mil jaaye kisi aur ki
10/20/22, 8:15 PM - Sparsh Pec: No worry yashu
Enjoy diwali
10/20/22, 8:15 PM - Yashwin: Meine toh same copy kardi
10/20/22, 8:16 PM - Ishroop: Chodh. Nahi mili to mein bhi wohi krungi copy
10/20/22, 8:16 PM - Sparsh Pec: Krke khtam kr
Debu sir doesn't care
10/20/22, 8:17 PM - Yashwin: Exactly no of questions should be same
10/20/22, 8:17 PM - Sparsh Pec: Yesss
Isi baat pr 17 bhejde bhaii
10/20/22, 8:17 PM - Yashwin: Meine khud kiya hota toh to bhejta 🤧🤧
10/20/22, 8:18 PM - Yashwin: Itna dimaag nahi lagata jo aaya karke passe karo
10/21/22, 8:53 AM - Gursharan Kaur✨: Ajj prac hona h na fm ka !?
Ya fir ansys wala kaam hi fir se ??
Pta h kisi ko ??
10/21/22, 8:53 AM - Yashwin: Prac
10/21/22, 8:56 AM - Sparsh Pec: On my way guys
10/21/22, 8:56 AM - Sparsh Pec: It's raining heavily 🌧️🥲
10/21/22, 8:56 AM - Yashwin: Ha yaar mei toh boat se aa rha paani zyada bhat gaya 🤧🤧
10/21/22, 8:58 AM - Shalin: India me nhi ho tum ??
10/21/22, 8:58 AM - Sparsh Pec: Travel safely broo
10/21/22, 8:58 AM - Shalin: Bahar se aa rhe ho ??
10/21/22, 8:58 AM - Shalin: 😂😂
10/21/22, 8:58 AM - Ishroop: Bhai pichli class mein prac waali krwaaya kya tha????
10/21/22, 9:00 AM - Gursharan Kaur✨: Ansys
10/21/22, 9:01 AM - Gursharan Kaur✨: I hope tu na hi pahunch paye itne paani mein se ...
And teri aaj bhi absent lgjaye ..
10/21/22, 9:03 AM - Sparsh Pec: Howw rudee..
10/21/22, 9:05 AM - Ishroop: Yaar abhi to lab bhi nahi khuli hoti
10/21/22, 9:05 AM - Ishroop: Sab 9:30 chalte
10/21/22, 9:05 AM - Ishroop: 😁😁😁😁
10/21/22, 9:05 AM - Sparsh Pec: Best
10/21/22, 9:05 AM - Yashwin: Ankit sir ne leni hai lab waise aur woh 8 bje ki class mei 7:55 aate 🤧🤧
10/21/22, 9:07 AM - Ishroop: But wo 8:55 tal enter krne dete
10/21/22, 9:07 AM - Ishroop: And attendance laga dete
10/21/22, 9:07 AM - Yashwin: That is also right
10/21/22, 9:07 AM - Sankalp Singla: Mai 9.50 tk hi aaunga
10/21/22, 9:07 AM - Ishroop: And weise bhi khaali class ko thoda padhaayenge
10/21/22, 9:07 AM - Ishroop: Koi ek banda bhi pahuncha to bata dena. M in college only. Mein bhi aa jaungi fir lab
10/21/22, 9:08 AM - Yashwin: Chalo meri attendance lga  dena
Ok bye ✌️
10/21/22, 9:10 AM - Gursharan Kaur✨: We are right in front of lab 😂
10/21/22, 9:10 AM - Ishroop: Behenchod
10/21/22, 9:10 AM - Ishroop: 🥲🥲🥲🥲🥲
10/21/22, 9:10 AM - Ishroop: Ruk aati.
10/21/22, 9:15 AM - YUDHISHTER RANA Pec Mech: Unki class mein 8:55 pe aana is best🤓
10/21/22, 9:29 AM - Gursharan Kaur✨: <Media omitted>
10/21/22, 9:36 AM - Sagar: Aana kithr hai?
10/21/22, 9:37 AM - YUDHISHTER RANA Pec Mech: Fm lab
10/21/22, 10:34 AM - Shalin: <Media omitted>
10/21/22, 10:40 AM - Shalin: <Media omitted>
10/21/22, 11:07 AM - Sagar: <Media omitted>
10/21/22, 11:08 AM - Sagar: <Media omitted>
10/21/22, 11:10 AM - Arihan Mech: Thanks
10/22/22, 4:02 PM - Yashwin: Pom ki jo assignments karni woh jo sir ne tutorial sheets bheji woh hai ? @916239579405 @918699133946 ??
10/22/22, 4:17 PM - Gursharan Kaur✨: Yup
10/22/22, 4:17 PM - Gursharan Kaur✨: Wahi hain
10/22/22, 4:17 PM - Gursharan Kaur✨: Solutions are attached
10/22/22, 4:35 PM - Yashwin: Ok
10/22/22, 6:06 PM - Shalin: Kb tk submit krni hai POM ki assignment??
10/22/22, 8:16 PM - YUDHISHTER RANA Pec Mech: Chutiyon ke baad
10/22/22, 8:18 PM - Shalin: Okk
10/22/22, 8:25 PM - Shalin: This message was deleted
10/22/22, 8:26 PM - Shalin: This message was deleted


If u wish to follow
Would be really appreciated 🫡
10/30/22, 9:41 PM - Shalin: Kl se Classes hain
10/30/22, 9:41 PM - Shalin: To koi message nhi ??
10/30/22, 9:42 PM - Shalin: 🤔🤔
11/2/22, 10:11 AM - Yashwin: <Media omitted>
11/2/22, 10:12 AM - Yashwin: Aajao sab experiment start karna hai
11/2/22, 10:25 AM - Sagar: <Media omitted>
11/2/22, 11:25 AM - Rohit Pec Mech: <Media omitted>
11/3/22, 10:09 AM - Arihan Mech: PE tut in T6
11/4/22, 8:52 AM - Ishroop: Oyye
11/4/22, 8:52 AM - Ishroop: Aaj aa raha koi for fm lab?
11/4/22, 8:52 AM - Ishroop: Also agar lab cancel krwaani to blood donation drive hai aaj
11/4/22, 8:53 AM - Ishroop: 9:30 nikal lenge bol ke ki sir blood donate krna or smtg
11/4/22, 8:53 AM - Sparsh Pec: Aa chuka hu me 🥲
11/4/22, 8:53 AM - Ishroop: Me too
11/4/22, 8:53 AM - Sparsh Pec: Ye try kr lenge
11/4/22, 8:53 AM - Ishroop: Yee
11/4/22, 8:53 AM - Ishroop: Aa jaao lab fir for that
11/4/22, 9:03 AM - Shalin: Rac lab ??
11/4/22, 9:09 AM - Rohit Pec Mech: Kahan hai practical?
11/4/22, 9:09 AM - Rohit Pec Mech: Mai 9:30 tk pohonchunga
11/4/22, 9:24 AM - Shalin: <Media omitted>
11/4/22, 10:23 AM - Rohit Pec Mech: <Media omitted>
11/4/22, 10:29 AM - Rohit Pec Mech: <Media omitted>
11/4/22, 10:29 AM - Rohit Pec Mech: <Media omitted>
11/4/22, 10:29 AM - Rohit Pec Mech: <Media omitted>
11/4/22, 10:30 AM - Ishroop: Thanks yaar rohit ✨✨✨
11/4/22, 10:31 AM - Rohit Pec Mech: <Media omitted>
11/4/22, 10:31 AM - Rohit Pec Mech: <Media omitted>
11/4/22, 11:16 AM - Shalin: Class to nhi hai
11/4/22, 11:16 AM - Shalin: PE Ki class ??
11/4/22, 11:18 AM - Rohit Pec Mech: <Media omitted>
11/4/22, 11:22 AM - Shalin: Book ki pdf hi Daal de
@Rohit Sir
11/4/22, 11:25 AM - Rohit Pec Mech: Total 8 practical hai and 8. PDFs
11/4/22, 11:25 AM - Rohit Pec Mech: Dekhlena
11/5/22, 11:41 PM - Ishroop: Anyone has experiment 5 and 6 hmt to bhejdo please
11/5/22, 11:42 PM - Gursharan Kaur✨: And kisi ne fm k prac likhe hain toh vo bhi bhejdo
11/5/22, 11:42 PM - Ishroop: Tu pehle 5th bhejde plis
11/5/22, 11:42 PM - Ishroop: Fm ke to jo rohit se mangwaaye wohi cheapness
11/5/22, 11:42 PM - Ishroop: Chepne*
11/5/22, 11:42 PM - Gursharan Kaur✨: Calculations toh kr ni rakhi maine .. 🥲
11/5/22, 11:43 PM - Gursharan Kaur✨: Bs readings hi hain ....vo bhi complete ni hain 😂 7th ki bhi and 6th ki bhi 2 hi correct values hain. .
11/5/22, 11:43 PM - Ishroop: Jitna bhi kra bhejde plis 🥲
11/5/22, 11:43 PM - Gursharan Kaur✨: Baaki k groups se poochhna pdega for readings ...
11/7/22, 8:03 AM - Shalin: I am not coming today
Jitney Proxy lg ske lga dena
11/7/22, 8:03 AM - Shalin: OK 👍
11/8/22, 6:13 PM - Shalin: PE ke quiz ki date nhi aayi ??
11/8/22, 6:14 PM - Shalin: Na aaye , to better hai ??
11/8/22, 6:44 PM - Shalin: PE quiz will be on Friday 1:30
The quiz will be 20 mins long
11/8/22, 6:45 PM - Shalin: OK 👍
11/8/22, 11:29 PM - Gursharan Kaur✨: guys kal hmt ka prac lgaana h ??
11/8/22, 11:29 PM - Ishroop: Weise hum m2 se ek practical aage chal rhe
11/8/22, 11:29 PM - Ishroop: Unka exp 7 nhi hua
11/8/22, 11:30 PM - Gursharan Kaur✨: and in total ig 3 hi exp rehte hain
11/8/22, 11:30 PM - Gursharan Kaur✨: plus this sat ig wed wala tt folow hoga, right ??
11/8/22, 11:30 PM - Gursharan Kaur✨: toh fir se hmt ka prac 😥
11/8/22, 11:30 PM - Ishroop: Arrey hnnn
11/8/22, 11:31 PM - Ishroop: Weise dekhlo krke khatam krte
11/8/22, 11:31 PM - Ishroop: Baaki nahi lagaana to that also works with me
11/8/22, 11:33 PM - Gursharan Kaur✨: bhyi 2 din wali bt h
11/8/22, 11:33 PM - Gursharan Kaur✨: ek din lga lete dono mein se
11/8/22, 11:51 PM - Rohit Pec Mech: Rehndete kal
11/8/22, 11:51 PM - Rohit Pec Mech: If all agree
11/8/22, 11:51 PM - Rohit Pec Mech: Baki dekhlo
11/8/22, 11:53 PM - Sparsh Pec: Rehne dete h yrrr
11/8/22, 11:59 PM - Ishroop: I'll say Saturday ko Rehne dete
11/8/22, 11:59 PM - Ishroop: Weise hi weekend hai.
11/8/22, 11:59 PM - Sparsh Pec: Ko bhii 🙃
11/8/22, 11:59 PM - Ishroop: Baaki tum sabki mrzi hai dekhlo. Kl laga lete. Weekend Rehne denge
11/9/22, 12:00 AM - Ishroop: M1 mein bahut log hain jo shaayad ek class miss kr lein. But 2 classes i highly doubt it
11/9/22, 12:00 AM - Ishroop: 🥲🥲🥲
11/9/22, 1:17 AM - Shalin: No decision
Long discussions..🥱🥱
11/9/22, 1:17 AM - Shalin: This message was deleted
11/9/22, 1:18 AM - Shalin: Ok 😄 👍
11/9/22, 10:04 AM - Sparsh Pec: Practical lga rhe ho ??
11/9/22, 10:05 AM - Yashwin: Mei nahi 🌝
11/9/22, 10:05 AM - Yashwin: Attendance lga dena
11/9/22, 10:06 AM - Gursharan Kaur✨: Laga lenge ..
But thora late chlte hain
11/9/22, 10:06 AM - Gursharan Kaur✨: But Saturday ko koi Mt jaana ....
11/9/22, 10:06 AM - Gursharan Kaur✨: 🥲
11/9/22, 10:06 AM - Gursharan Kaur✨: Agar koi sat jaana chahta hai toh abhi btado ...
11/9/22, 10:07 AM - YUDHISHTER RANA Pec Mech: Na
11/9/22, 10:11 AM - Kshitiz Sharma Mech: Jb jaoge to bta dena
11/9/22, 10:17 AM - Gursharan Kaur✨: Chalein ?
11/9/22, 10:17 AM - Kshitiz Sharma Mech: Lab bnd h
11/9/22, 10:18 AM - Gursharan Kaur✨: Toh cancel ??
11/9/22, 10:18 AM - Gursharan Kaur✨: 🤣
11/9/22, 10:18 AM - Kshitiz Sharma Mech: Hnn most probably
11/9/22, 10:19 AM - Sagar: Class cancel
11/9/22, 10:20 AM - Gursharan Kaur✨: Bs brhiya ...
In case lab khul jaye aur prac hona hua toh MSG krdena ...
11/9/22, 10:27 AM - Gursharan Kaur✨: Guys prac is cancelled...
Cz lab attendant is busy with something else
11/10/22, 9:52 AM - Shalin: This message was deleted
11/10/22, 9:52 AM - Shalin: This message was deleted
11/10/22, 10:29 AM - Shalin: This message was deleted
11/10/22, 10:29 AM - Shalin: This message was deleted
11/10/22, 10:30 AM - Shalin: This message was deleted
11/11/22, 9:26 AM - Sagar: <Media omitted>
11/11/22, 9:26 AM - Sagar: <Media omitted>
11/11/22, 9:26 AM - Sagar: <Media omitted>
11/11/22, 9:27 AM - Sagar: <Media omitted>
11/11/22, 9:29 AM - Ishroop: M omw. Agar attendance ho to laga dena meri bhi please
11/11/22, 9:29 AM - Gursharan Kaur✨: +++
11/11/22, 9:48 AM - Rohit Pec Mech: Kahan hora hai
11/11/22, 9:48 AM - Rohit Pec Mech: Practical
11/11/22, 9:49 AM - Gursharan Kaur✨: Fm lab
11/11/22, 10:00 AM - Shalin: This message was deleted
11/11/22, 10:01 AM - Shalin: This message was deleted
11/12/22, 8:00 AM - Yashwin: Aa rha hai koi class lgane
11/12/22, 8:01 AM - Yashwin: Sir toh aaye nahi na room khula hai
11/12/22, 8:02 AM - Ishroop: M omw
11/12/22, 8:03 AM - Ishroop: Puchu kya??? 😂
11/12/22, 8:04 AM - Yashwin: Aagaye sir
11/12/22, 8:05 AM - Ishroop: Cool
11/12/22, 8:05 AM - Yashwin: Jaldi aajao koi akele baithe ajeeb lag rha 😂
11/12/22, 8:09 AM - Gursharan Kaur✨: Aur sir prha bhi rahe hain ?? 🥲
11/12/22, 8:09 AM - Ishroop: Bhai chapter chal kaunsa raha hai weise fm mein???
11/12/22, 8:09 AM - Gursharan Kaur✨: ++
11/12/22, 8:15 AM - Yashwin: Ha
11/12/22, 8:16 AM - Yashwin: Boudary layer started
11/12/22, 8:16 AM - Ishroop: Tf
11/12/22, 8:16 AM - Ishroop: Wtf is that
11/12/22, 8:16 AM - Ishroop: ?
11/12/22, 8:25 AM - Yashwin: New Chapter
11/12/22, 8:41 AM - Ishroop: 🥲🥲🥲
11/12/22, 8:44 AM - Rohit Pec Mech: Aaj konsa time table follow hora
11/12/22, 8:45 AM - Ishroop: Wednesday
11/12/22, 9:57 AM - Shalin: Hmt lab ??
11/12/22, 9:58 AM - Shalin: Koi aayega ya cancel ??
11/12/22, 10:02 AM - Shalin: This message was deleted
11/12/22, 10:02 AM - Shalin: This message was deleted
11/12/22, 10:11 AM - Sagar: You deleted this message
11/12/22, 10:27 AM - Mohak Gandhi Pec: Lab lag rhi ha
11/12/22, 10:27 AM - Mohak Gandhi Pec: HMT
11/12/22, 10:28 AM - Ishroop: Tf
11/12/22, 10:28 AM - Ishroop: Keise
11/12/22, 10:28 AM - Ishroop: Kaun kaun hai lab???
11/12/22, 10:30 AM - Mohak Gandhi Pec: 4 log h
11/12/22, 10:30 AM - Ishroop: Kaun kaun?
11/12/22, 10:30 AM - Ishroop: Bhai nahi jaana tha aaj
11/12/22, 10:31 AM - Shalin: This message was deleted
11/12/22, 10:33 AM - Ishroop: @917710715181 kaun kaun hain?
11/12/22, 10:33 AM - Ishroop: Aap se koi puch nahi raha
11/12/22, 10:33 AM - Mohak Gandhi Pec: Sagar, Main, Shalin and Gautam
11/12/22, 10:34 AM - Ishroop: Aaaahhh
11/12/22, 10:34 AM - Ishroop: Chal okay
11/12/22, 10:34 AM - Sagar: Mohak really wanted to attend class
11/12/22, 10:35 AM - Ishroop: Meri proxy plis :")
11/12/22, 10:38 AM - Gursharan Kaur✨: ++
11/12/22, 10:41 AM - Shalin: Koi nhi 😂😂
11/12/22, 11:26 AM - Mohak Gandhi Pec: <Media omitted>
11/12/22, 11:34 AM - Mohak Gandhi Pec: Sabki attendance lg gyi
11/12/22, 12:10 PM - YUDHISHTER RANA Pec Mech: MG the OG🙏
11/13/22, 2:04 PM - Yashwin: abhi tak fm mei apne kitne experiment hogaye ?
11/13/22, 2:04 PM - Yashwin: 3 na
11/13/22, 8:13 PM - Ishroop: 5
11/13/22, 8:14 PM - Yashwin: 3rd aur 4th kaunsa hai
11/13/22, 8:16 PM - Ishroop: Ye nhi pata
11/13/22, 8:16 PM - Ishroop: Count mein 5 hue hain
11/13/22, 8:16 PM - Yashwin: 🤧
11/14/22, 10:32 AM - Yashwin: Class nahi thi kya aaj
11/15/22, 11:04 PM - Shalin: This message was deleted
11/15/22, 11:04 PM - Shalin: This message was deleted
11/16/22, 10:15 AM - Yashwin: Aa rahe ho lab
11/16/22, 10:15 AM - Yashwin: Else experiment start karte
11/16/22, 10:16 AM - Gursharan Kaur✨: Nope
11/16/22, 10:16 AM - Yashwin: Baaki bhi btado
11/16/22, 10:18 AM - Ishroop: Uhhh
11/16/22, 10:19 AM - Ishroop: Mein aaungi but late
11/16/22, 10:19 AM - Ishroop: Like 11 ish types shaayad
11/16/22, 10:19 AM - Yashwin: Ok
11/16/22, 10:19 AM - Yashwin: @917710715181 @919814484499 @918146907246 @918054349284 @916239902903 @919877113830 aa rahe ?
11/16/22, 10:19 AM - Yashwin: In next 5 min ?
11/16/22, 10:20 AM - Rohit Pec Mech: 11 baje Tak aata mai bhi
11/16/22, 10:22 AM - Sankalp Singla: 11.30
11/16/22, 10:41 AM - Ishroop: Gaurav sir will not be taking any pe tuts from now on. He will be giving zero attendance to everyone who has not attended and in case of mass bunk as well, class will be considered and attendance given will be zero. You can take this up with Kamal sir
11/16/22, 10:42 AM - YUDHISHTER RANA Pec Mech: <Media omitted>
11/17/22, 8:39 PM - Gursharan Kaur✨: Yaar kisi ne fm ki prac likhi h ??
11/18/22, 7:28 AM - Shalin: Congratulations 🥳🥳
11/18/22, 7:28 AM - Shalin: Our Jee efforts didn't go
in vain
Core mechanical me internship Lg rhi hain .
11/18/22, 9:14 AM - Yashwin: Kab aa rahe
11/18/22, 9:28 AM - Sankalp Singla: 10 bje
11/18/22, 9:32 AM - Yashwin: 1 attendance milegi phir
11/18/22, 9:32 AM - Yashwin: 2🌝
11/18/22, 9:36 AM - Yashwin: <Media omitted>
11/21/22, 7:46 AM - Yashwin: @916239579405 Gurjeet sir ko bolde ki 10 bje class ke time le feedback jaldi aana mushkil hai
11/21/22, 8:04 AM - Ishroop: Ok
11/21/22, 8:04 AM - Ishroop: Krti baat
11/21/22, 8:05 AM - Ishroop: Sir phone wagehra nahi utha rahe
11/22/22, 10:58 AM - Shalin: Iski Reading send kro
11/22/22, 10:09 PM - Yashwin: <Media omitted>
11/22/22, 10:11 PM - Yashwin: Tavish ki hmt ki assignment 3 hai
11/22/22, 10:11 PM - Yashwin: Check karlena ans
11/23/22, 10:12 AM - Yashwin: Lab aajao
11/23/22, 10:12 AM - Yashwin: Last exp hai aaj
11/23/22, 10:33 AM - Shalin: This message was deleted
11/23/22, 10:34 AM - Shalin: <Media omitted>
11/23/22, 11:00 AM - Shalin: <Media omitted>
11/23/22, 11:34 AM - Shalin: <Media omitted>
11/23/22, 2:01 PM - Yashwin: Lab file of Fluid Mechanics completed
11/23/22, 2:02 PM - Gursharan Kaur✨: Send krdo sir fir left side
11/23/22, 2:02 PM - Yashwin: Yeh g2 se arrange karlo
11/23/22, 2:02 PM - Yashwin: Pls mujhe bhi chahyye
11/23/22, 5:44 PM - Sagar: Left side different hone se problem ni hogi?
11/29/22, 8:06 PM - Sankalp Singla: Kl hmt ka practical lgega?
11/29/22, 8:41 PM - Yashwin: Pata nahi
11/29/22, 9:07 PM - Shalin: This message was deleted
11/29/22, 9:07 PM - Shalin: This message was deleted
11/29/22, 9:07 PM - Gursharan Kaur✨: Sir bolre the k jis jiske jo jo exps rehte hain vo kal krlena M1 wale and ek exp aur bhi rehta h shayad apna
11/29/22, 10:02 PM - Yashwin: Kal ka kya scene subah ki class ka?0
11/29/22, 10:02 PM - Sparsh Pec: Rehne dete h
11/29/22, 10:02 PM - Ishroop: Yaar ankit yadav is not responding
11/29/22, 10:03 PM - Ishroop: Meine msg kr rakha
11/29/22, 10:03 PM - Yashwin: Mujhe no problem ✌️
11/29/22, 10:03 PM - Sparsh Pec: 12 bje aate h sidha
11/29/22, 10:03 PM - Ishroop: Good Evening sir

Ishroop 3rd yr mech CR this side. Firstly i would like to apologise for disturbing you so late sir.

As mentioned before PECFEST as well, a lot of the day scholars are facing troubles reaching college at 8am for FM class. I could find alternative slots as presented below:

Wednesday 8-9 class to be rescheduled at wednesday 3-4

Thursday 8-9 class to be rescheduled to Tuesday 12-1

It would be really helpful if the classes could be rescheduled as so. In case either of the slots is not comfortable by you sir, kindly let me know as I will find another time slot for the same.

Thankyou so much sir
11/29/22, 10:03 PM - Ishroop: Kal 10 se 12 lab nhi hai???
11/29/22, 10:03 PM - Sparsh Pec: HMT h yrr
Debu sir thak gye honge fest le baad
Rest dete h unhe
11/29/22, 10:04 PM - Yashwin: Lab lgale waise teri attendance nahi hai lab mei
11/29/22, 10:04 PM - Yashwin: Kal phir 10 bje 😂
11/29/22, 10:04 PM - Sparsh Pec: Oo vere attendance se Darna band krdiya h mene
11/29/22, 10:04 PM - Ishroop: Meri 2 miss hain yaar. 🥲
Tabhi was asking
11/29/22, 10:04 PM - Sparsh Pec: Mass bunk days khatm hogye kyaa 🌝
11/29/22, 10:04 PM - Yashwin: 2 marks for attendance and last time usne nahi lgayi thi proxy
11/29/22, 10:05 PM - Yashwin: Lab mei
11/29/22, 10:06 PM - Ishroop: Hn ik yaar. Keh rhe thei committee waale ki ho jaayega sort but idk. Baat krni padegi.
11/29/22, 10:07 PM - Yashwin: Yaar dekhlena woh toh mana nahi karega waise
Baaki files poori karlena FM ki
11/29/22, 10:07 PM - Ishroop: Fm tf ye kaha se aaya? 🥲
11/29/22, 10:07 PM - Yashwin: Mujhe vikas ka message aaya tha ki iss week complete karni hai
11/29/22, 10:07 PM - Yashwin: 8 practicals
11/29/22, 10:08 PM - Ishroop: 🥲🥲🥲
11/29/22, 10:08 PM - Ishroop: Kisi ne kuch likha fike mein fm ki?
11/29/22, 10:08 PM - Yashwin: Ha yaar bhot kaam hai
Help will be appreciated 🫡
11/29/22, 10:09 PM - Yashwin: Dusre groups se lelo please
11/29/22, 10:09 PM - Ishroop: +++
11/29/22, 10:09 PM - YUDHISHTER RANA Pec Mech: Sounds good
11/29/22, 10:09 PM - Sankalp Singla: Perfect
11/29/22, 10:10 PM - Shalin: Cancel fir
11/29/22, 10:10 PM - Shalin: Jldi batao
11/29/22, 10:11 PM - Sparsh Pec: POLL:
Kab aana h?
OPTION: 12 bje aana (3 votes)
OPTION: 10 bje aakr 12 bje class lgana (0 votes)
OPTION: Betray krke 10 bje hi class lgana (0 votes)

11/29/22, 10:11 PM - YUDHISHTER RANA Pec Mech: 11 aur 12 mein 1 ghante ki hi to baat hai😂
11/29/22, 10:13 PM - Shalin: Mtlb wohi hua
Teacher aayenge to Practical hoegi
11/29/22, 10:13 PM - Shalin: Otherwise Cancelled
11/29/22, 10:16 PM - Sagar: Not only day scholars
Hostlers also struggle to come at 8 am
8-9 is mess time
11/29/22, 10:17 PM - Sagar: Its very unfair to have class 8-9 am
11/29/22, 10:17 PM - Yashwin: Pata hai yaar hmnei bola sir ko
11/29/22, 10:17 PM - Shalin: This message was deleted
11/29/22, 10:17 PM - Shalin: This message was deleted
11/29/22, 10:17 PM - Yashwin: sir bolte jab time table aata tabhi bolna chahiye tha
11/30/22, 9:37 AM - Shalin: Kb krni hai Submit
11/30/22, 9:37 AM - Shalin: Aagle Monday tk ??
11/30/22, 9:57 AM - Shalin: This message was deleted
11/30/22, 9:57 AM - Shalin: This message was deleted
11/30/22, 10:06 AM - Shalin: This message was deleted
11/30/22, 10:07 AM - Shalin: This message was deleted
11/30/22, 10:09 AM - Yashwin: Nahi iss week
11/30/22, 10:14 AM - Gursharan Kaur✨: Counter flow wala exp jis jiska rehta h and radiation ka Stephan boltzmann law wala rehta h ...
Vo aajao
11/30/22, 10:47 AM - Shalin: <Media omitted>
11/30/22, 11:22 AM - Mohak Gandhi Pec: <Media omitted>
11/30/22, 6:42 PM - Mohak Gandhi Pec: <Media omitted>
12/1/22, 8:19 AM - YUDHISHTER RANA Pec Mech: Aaj apni class sidha 12 baje hai?
12/1/22, 8:20 AM - Yashwin: Ha
12/1/22, 8:20 AM - Yashwin: agar mann hai jaldi chaleja
12/1/22, 8:23 AM - Ishroop: Sankalp
Sparsh
Priyanshu
12/1/22, 8:23 AM - Ishroop: Bhai ye teeno chale jaana hmt ke liye
12/1/22, 8:24 AM - Ishroop: @918146907246 @918054349284 @919467734085
12/1/22, 10:09 AM - Ishroop: Guys
12/1/22, 10:09 AM - Ishroop: Gaurav sir L6 mein hain
12/1/22, 10:10 AM - Ishroop: He said jitne bache hmt lab nahi gaye wo l6 aa jaao
12/1/22, 10:10 AM - Gursharan Kaur✨: Wtf !!!
12/1/22, 10:10 AM - Kshitiz Sharma Mech: Tune to bola tha Tut ni lgega
12/1/22, 10:10 AM - Gursharan Kaur✨: Bhyi koi mat jaana
12/1/22, 10:10 AM - Gursharan Kaur✨: ++
12/1/22, 10:10 AM - Ishroop: Bhai mujhe pakad liya hai sir ne
12/1/22, 10:10 AM - Ishroop: Koi mt aao
12/1/22, 10:11 AM - Ishroop: Mein bol dungi sir sab gaye hue hain
12/1/22, 10:11 AM - Ishroop: And dw
12/1/22, 10:11 AM - Gursharan Kaur✨: And koi aur h l6 mein ??
Ya sirf tu hi hai??
12/1/22, 10:11 AM - Ishroop: Apni attendance wagehra kuch nahi lagwaungi
12/1/22, 10:11 AM - Ishroop: No. Only me.
12/1/22, 10:11 AM - Gursharan Kaur✨: 😂😂😂
12/1/22, 10:11 AM - Ishroop: 🥲🥲🥲
12/1/22, 10:11 AM - Gursharan Kaur✨: Achha
12/1/22, 10:15 AM - Shalin: This message was deleted
12/1/22, 10:31 AM - Sankalp Singla: @916239579405 file ki deadline bhi bdwade
12/1/22, 10:31 AM - Sankalp Singla: Plzz
12/1/22, 10:31 AM - Sankalp Singla: 🙏🏼🙏🏼
12/1/22, 10:31 AM - Ishroop: Yaar wo ankit sir ne hi boli seedha. And uss se pehle lab waale sir ne bhi boli coz Friday ko teen groups ki lab hoti.
12/1/22, 10:31 AM - YUDHISHTER RANA Pec Mech: 😂
12/1/22, 10:31 AM - Ishroop: 🥲🥲🥲
12/1/22, 10:32 AM - Ishroop: Tumhe Friday ko file dikhaane hi padegi ek baar at least coz practicals khatam ho gye hain saare.
12/1/22, 10:32 AM - Ishroop: 🥲🥲🥲
12/1/22, 10:32 AM - Sankalp Singla: Ok
12/1/22, 10:33 AM - Ishroop: Haan baaki kal bol denge sab ki sir monday tak complete kr lenge or smtg.
12/1/22, 10:34 AM - Yashwin: Hamara last practical transition from laminar to turbulent tha na?
12/1/22, 10:34 AM - Ishroop: Hn
12/1/22, 10:34 AM - Rohit Pec Mech: Hn
12/1/22, 10:34 AM - Rohit Pec Mech: Wo dye wala ig
12/1/22, 10:35 AM - Ishroop: Also total 8 practicals hain. 7 lab waale and ek ansys.
12/1/22, 10:35 AM - Ishroop: For fm
12/1/22, 10:42 AM - Rohit Pec Mech: POm ki 7 Tut sheets kabtak Deni hai ?
12/1/22, 10:42 AM - Rohit Pec Mech: And PE ki assignment also
12/1/22, 10:42 AM - Ishroop: Monday
12/1/22, 10:42 AM - Rohit Pec Mech: Ok
12/1/22, 10:42 AM - Ishroop: Ye ig kal
12/1/22, 10:42 AM - Rohit Pec Mech: Ok
12/1/22, 10:43 AM - Ishroop: Sorry ye bhi monday hi hai
12/1/22, 10:43 AM - Ishroop: @919478379030
12/1/22, 10:43 AM - Ishroop: Monday submission:

Assignment 6 fm
Pe assignment
Pom assignments
12/1/22, 10:49 AM - Rohit Pec Mech: Okok
12/1/22, 11:11 AM - Yashwin: Kisi ne meri koi file dekhi ho jismei pom ki assignments ho meri toh btadena
Mil nahi rahi 🥲🥲🥲
12/1/22, 4:45 PM - Shalin: FM ki file bhi Monday krwado
12/1/22, 4:46 PM - Shalin: Baaki sb  to Monday hain
12/1/22, 9:28 PM - Kshitiz Sharma Mech: <Media omitted>
12/1/22, 9:29 PM - Mohak Gandhi Pec: iski readings krlena sb
12/1/22, 9:38 PM - Shalin: This message was deleted
12/1/22, 9:39 PM - Shalin: This message was deleted
12/1/22, 9:42 PM - Shalin: This message was deleted
12/1/22, 9:42 PM - Shalin: This message was deleted
12/1/22, 10:13 PM - Sagar: <Media omitted>
12/1/22, 11:42 PM - Gursharan Kaur✨: Yaar kal lab k liye aana h ??
12/1/22, 11:43 PM - Sparsh Pec: File ni krni submit?
12/1/22, 11:43 PM - Gursharan Kaur✨: Yaar vo toh ikathi krke aise hi submit kr skte hain na
12/1/22, 11:44 PM - Sparsh Pec: Ohh vese
Fir decide krlo
12/1/22, 11:44 PM - Gursharan Kaur✨: bta toh rahi hu yaar
12/1/22, 11:44 PM - Gursharan Kaur✨: nhi aayenge
12/1/22, 11:44 PM - Gursharan Kaur✨: files collect krke ikathe de denge
12/1/22, 11:45 PM - Gursharan Kaur✨: and 11 am hi aayenge
12/1/22, 11:49 PM - Sagar: +1
12/2/22, 12:40 AM - Shalin: This message was deleted
12/2/22, 12:57 AM - Gursharan Kaur✨: Who all wants to come at 9 for lab and want to get their files checked can come and get their files checked
12/2/22, 1:18 AM - YUDHISHTER RANA Pec Mech: Shi
12/2/22, 8:01 AM - Ishroop: Aaj majority nhi krti to kal ke liye request kr dungi sir ko ki sir same tt hai. Jo reh gaye wo kl krwa lenge
12/2/22, 8:04 AM - Sankalp Singla: Hn 🙏🏼
12/2/22, 8:04 AM - Shalin: Hn 👍
12/2/22, 8:05 AM - Ishroop: Bs abhi sabko mt bolna. Mein aaraam se baat kr aaungi.
12/2/22, 8:07 AM - Shalin: This message was deleted
12/2/22, 8:07 AM - YUDHISHTER RANA Pec Mech: op
12/2/22, 9:20 AM - Yashwin: Yaar mujhe vikas sir ka phone aa rha woh bol rahe sab lab aao file check karwane abhi ankit sir wait kar rahe
12/2/22, 9:20 AM - Yashwin: Lab report karna
12/2/22, 9:22 AM - Gursharan Kaur✨: Wtf !!
12/2/22, 9:26 AM - YUDHISHTER RANA Pec Mech: Bhai nhi hui file poori
12/2/22, 9:26 AM - Yashwin: Poori toh meri bhi nahi hai
12/2/22, 9:32 AM - Gursharan Kaur✨: Fir jaakr Krna bhi kya hi h ??
12/2/22, 9:32 AM - Gursharan Kaur✨: Ek bnda jaake baat krlo sir se 🥲
12/2/22, 9:33 AM - Yashwin: Atleast shakal dikhake aajatr
12/2/22, 9:33 AM - Gursharan Kaur✨: You go !! 🫠
12/2/22, 9:39 AM - Yashwin: Kal viva hai lab ka
12/2/22, 9:39 AM - Yashwin: 🫡🫡🫡🫡
12/2/22, 9:40 AM - Gursharan Kaur✨: Tuesday ko ni ho sakta bhyi ?? 😭😭
12/2/22, 9:41 AM - Yashwin: Sir se karlo baat
12/2/22, 9:42 AM - Gursharan Kaur✨: Kaun kaun h wahaan ??
12/2/22, 9:42 AM - Kshitiz Sharma Mech: Mai or Yashwin
12/2/22, 9:52 AM - Kshitiz Sharma Mech: Yrr agr clg me ho to RAC lab aa jao sir gussa hore h
12/2/22, 10:14 AM - Kshitiz Sharma Mech: <Media omitted>
12/2/22, 10:14 AM - Kshitiz Sharma Mech: <Media omitted>
12/2/22, 10:14 AM - Kshitiz Sharma Mech: <Media omitted>
12/2/22, 10:14 AM - Kshitiz Sharma Mech: <Media omitted>
12/2/22, 10:15 AM - Ishroop: Ye saare draw krne hain?
12/2/22, 10:16 AM - Gursharan Kaur✨: Haan 😂
12/2/22, 10:19 AM - Ishroop: 🥲🥲🥲🥲
12/2/22, 10:33 AM - Yashwin: <Media omitted>
12/2/22, 10:33 AM - Yashwin: <Media omitted>
12/2/22, 10:33 AM - Yashwin: <Media omitted>
12/2/22, 10:34 AM - Yashwin: <Media omitted>
12/2/22, 10:34 AM - Yashwin: <Media omitted>
12/2/22, 10:34 AM - Yashwin: <Media omitted>
12/2/22, 10:34 AM - Yashwin: <Media omitted>
12/2/22, 10:34 AM - Yashwin: <Media omitted>
12/2/22, 10:34 AM - Yashwin: Hmt assignment 04
12/2/22, 10:34 AM - Yashwin: Kuch questions nahi hai
12/2/22, 10:34 AM - Yashwin: Woh manage karleb
12/2/22, 10:34 AM - Yashwin: Karlena
12/2/22, 10:34 AM - Ishroop: Thanks Yashwin ✨✨❤️❤️
12/2/22, 10:35 AM - Yashwin: Kshitiz ki assignment hai😝
12/2/22, 10:35 AM - Ishroop: Thanks ~Yashwin~ Kshitiz✨✨❤️❤️
12/2/22, 10:35 AM - Ishroop: 😂😂😂
12/2/22, 11:33 AM - Mohak Gandhi Pec: <Media omitted>
12/2/22, 1:36 PM - Mohak Gandhi Pec: <Media omitted>
12/2/22, 1:36 PM - Mohak Gandhi Pec: <Media omitted>
12/2/22, 1:36 PM - Mohak Gandhi Pec: <Media omitted>
12/2/22, 1:36 PM - Mohak Gandhi Pec: <Media omitted>
12/2/22, 1:36 PM - Mohak Gandhi Pec: <Media omitted>
12/2/22, 1:36 PM - Mohak Gandhi Pec: <Media omitted>
12/2/22, 1:48 PM - Ishroop: M1 M2 can submit file tomorrow morning positively. No further delays will be entertained.
12/2/22, 1:48 PM - Ishroop: 😎😎😎✨✨✨
12/2/22, 1:48 PM - Sagar: You deleted this message
12/2/22, 1:49 PM - Sagar: Great yaar
12/2/22, 1:50 PM - Rohit Pec Mech: THANK YOU SO MUCH 🤧
12/2/22, 1:50 PM - Shalin: This message was deleted
12/3/22, 12:48 AM - Shalin: Kl Sirf FM ki file submission hai
12/3/22, 12:48 AM - Shalin: Quiz Monday ko hai ??
12/3/22, 12:49 AM - Yashwin: Viva hai kal
12/3/22, 12:49 AM - Shalin: File check krane ke Time hoegi ??
12/3/22, 12:50 AM - Yashwin: Woh sirf submit karni
12/3/22, 12:50 AM - Shalin: OK 👍
12/3/22, 8:21 AM - Shalin: Viva Written hai aur Time bhi btaya hai Sir Ne ??
12/3/22, 8:21 AM - Yashwin: Viva ka matlab kya hota hai
12/3/22, 8:22 AM - Shalin: Time btaya hai ??
12/3/22, 8:22 AM - Yashwin: Lab ka time
12/3/22, 8:22 AM - Yashwin: 9-11
12/3/22, 8:24 AM - Shalin: This message was deleted
12/3/22, 8:24 AM - Shalin: This message was deleted
12/3/22, 8:24 AM - Yashwin: Ha toh usse viva nahi bolte woh quiz thi
12/3/22, 8:24 AM - Shalin: Ok Ok 👍
12/3/22, 8:28 AM - Yashwin: Viva bhi hua tha uske baad waise jo sir ne file check karte hue questions puche the
12/3/22, 8:29 AM - Shalin: This message was deleted
12/3/22, 8:29 AM - Shalin: OK Thanks bro 👍
12/5/22, 5:46 PM - Shalin: This message was deleted
12/5/22, 8:12 PM - Shalin: This message was deleted
12/6/22, 8:51 PM - Sankalp Singla: Pom ki quiz objective hai na???
12/6/22, 8:52 PM - Ishroop: No
12/6/22, 8:53 PM - Sparsh Pec: Firrr
12/6/22, 8:53 PM - Gursharan Kaur✨: Subjective
12/6/22, 8:53 PM - Sparsh Pec: Lag gyeee
12/6/22, 8:56 PM - Rohit Pec Mech: Unit 5 and 8 aare hai na ?
12/6/22, 9:20 PM - YUDHISHTER RANA Pec Mech: <Media omitted>
12/8/22, 11:14 AM - Rohit Pec Mech: FM ka handout bhejna koi
12/8/22, 11:47 AM - YUDHISHTER RANA Pec Mech: <Media omitted>
12/8/22, 11:57 AM - Gursharan Kaur✨: Kisi ne soni wali doosri class attend kri thi radiation wali ...??
12/26/22, 3:43 PM - Yashwin: Baaki subjects ke grade aagaye ? Ya dept ke bhar lgaye hai
12/26/22, 3:44 PM - Shalin: This message was deleted
12/26/22, 3:45 PM - Shalin: This message was deleted
12/26/22, 3:45 PM - Yashwin: Puch rha
12/26/22, 3:45 PM - Shalin: This message was deleted
12/26/22, 3:46 PM - Gursharan Kaur✨: Yaar dekh k btado
12/26/22, 5:29 PM - Ishroop: Jinke grades aa gye wo groups pe hain
12/26/22, 5:29 PM - Ishroop: Baaki agar dept mein lagne honge to kl tak lag jaayenge
12/26/22, 5:30 PM - Ishroop: Mp kal subha tak saare grades aa jaayenge so agar koi reh gaya to wo dekh sakte dept office ke bahar
12/26/22, 5:50 PM - Shalin: This message was deleted
12/26/22, 5:55 PM - Shalin: This message was deleted

12/29/22, 10:25 AM - Yashwin: Guys like kardena
12/29/22, 10:25 AM - Yashwin: Reach nahi badd rahi 😭
12/29/22, 10:25 AM - Yashwin: Thank you
")

st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 375px;
            }}
        </style>
    ''',
    unsafe_allow_html=True
)

selected = option_menu(
    menu_title=None,
    options=["Home", "Dashboard"],
    icons=["house", "bar-chart-line-fill"],
    default_index=0,
    orientation="horizontal",
)

uploaded_file = st.sidebar.file_uploader("Choose a file")
if selected == "Home":
    with st.sidebar:
        selected = option_menu(menu_title='',
                               options=['User', 'Timeline', 'Words', "Emoji", 'Wordcloud', 'Types of Users','Names'])
    # Main heading
    st.markdown("<h1 style='text-align: center; color: grey;'>Whatsapp Bussiness Visualizer</h1>",
                unsafe_allow_html=True)
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        # yeh data byte data ka stream hai isse string mein convert krna pdeega
        data = bytes_data.decode('utf-8')
        # ab file ka data screen pe dikhne lagega
        df = preprocessor.preprocess(data)
        df2 = preprocessor.preprocess2(data)
        df3 = preprocessor.preprocess3(data)
        from nltk.sentiment.vader import SentimentIntensityAnalyzer


        def sentiment(d):
            if d["pos"] >= d["neg"] and d["pos"] >= d["nu"]:
                return 1
            if d["neg"] >= d["pos"] and d["neg"] >= d["nu"]:
                return -1
            if d["nu"] >= d["pos"] and d["nu"] >= d["neg"]:
                return 0


        # Object
        sentiments = SentimentIntensityAnalyzer()
        df["pos"] = [sentiments.polarity_scores(i)["pos"] for i in df["message"]]  # Positive
        df["neg"] = [sentiments.polarity_scores(i)["neg"] for i in df["message"]]  # Negative
        df["nu"] = [sentiments.polarity_scores(i)["neu"] for i in df["message"]]
        df['value'] = df.apply(lambda row: sentiment(row), axis=1)
        st.dataframe(df)

        # fetch unique user
        user_list = df['user'].unique().tolist()
        try:
            user_list.remove('group_notification')
        except:
            pass
        user_list.sort()
        user_list.insert(0, 'Overall')
        selected_user = st.sidebar.selectbox('show analysis wrt', user_list)
        if st.sidebar.button('Show Analysis'):
            num_messages, words, num_media_messages, num_of_links,unique_counts = Helper.fetch_stats(selected_user, df2)
            st.title('Top Statistics')
            col1, col2, col3, col4,col5 = st.columns(5)

            with col1:
                st.markdown("<h2 style='text-align: left; color = #26495C;border-style: solid;'>Total Messages</h2>",
                            unsafe_allow_html=True)
                st.title(num_messages)
            with col2:
                st.markdown("<h2 style='text-align: left; color = #26495C;border-style: solid;'>Total Words</h2>",
                            unsafe_allow_html=True)

                # st.markdown('<p class="big-font">Total  Words </p>', unsafe_allow_html=True)
                st.title(words)
            with col3:

                st.markdown("<h2 style='text-align: left; color = #26495C;border-style: solid;'>Media Messages</h2>",
                            unsafe_allow_html=True)
                st.title(num_media_messages)
            with col4:
                st.markdown("<h2 style='text-align: left; color = #26495C;border-style: solid;'>Links Shared</h2>",
                            unsafe_allow_html=True)
                st.title(num_of_links)
            with col5:
                st.markdown("<h2 style='text-align: left; color = #26495C;border-style: solid;'>Number of users</h2>",
                            unsafe_allow_html=True)
                st.title(unique_counts)

            if selected == 'Timeline':
                col1, col2 ,col3= st.columns(3)
                with col1:
                    timeline = Helper.monthly_timeline(selected_user, df)
                    fig = px.line(timeline, x='time', y='message', title='User Activity Monthly',
                                  width=350, height=400)

                    fig
                # daily
                with col2:
                    timeline= Helper.day_timeline(selected_user, df)

                    fig = px.bar(timeline, x='D', y='message', title='User Activity DateWise',
                                  width=400, height=400)
                    fig
                #with col3:
                    #unique_counts = Helper.num_of_userss(df)
                    #unique_counts

            # finding the busiest users in the group (Group - level)
            if selected == 'User':
                if selected_user == 'Overall':
                    st.title('Most Busy Users')
                    x, new_df = Helper.most_busy_users(df)
                    fig, ax = plt.subplots()
                    # col1, col2 = st.columns(2)
                    names = new_df['names']
                    percentage = new_df['percentage']
                    fig = px.bar(new_df, x=names, y=percentage, color=names)
                    fig
            if selected == "Names":
                with col1:
                     unique_counts =Helper.name(df)
                     unique_counts
            if selected=="Download Dataset":
                with col1:
                    content=Helper.generate_text_file_content()
                    content


            # WordCloud
            if selected == 'Wordcloud':
                df_wc = Helper.create_wordcloud(selected_user, df)
                fig, ax = plt.subplots()
                plt.imshow(df_wc)
                st.pyplot(fig)
            if selected == "Types of Users":
                # Most Positive, Negitive, Neutral user...
                if selected_user == 'Overall':
                    #    col1, col2, col3 = st.columns(3)
                    #    with col1:
                    st.markdown("<h3 style='text-align: center; color: green;'>Most Positive Users</h3>",
                                unsafe_allow_html=True)
                    af = df['user'][df['value'] == 1]
                    x = af.value_counts()

                    fig = px.bar(af, y=x.values, x=x.index, color=x)
                    fig
                    #    with col2:
                    st.markdown("<h3 style='text-align: center; color: blue;'>Most Neutral Users</h3>",
                                unsafe_allow_html=True)
                    af = df['user'][df['value'] == 0]
                    x = af.value_counts()
                    fig = px.bar(af, y=x.values, x=x.index, color=x)
                    fig
                    #    with col3:
                    st.markdown("<h3 style='text-align: center; color: red;'>Most Negative Users</h3>",
                                unsafe_allow_html=True)
                    af = df['user'][df['value'] == -1]
                    x = af.value_counts()
                    fig = px.bar(af, y=x.values, x=x.index, color=x)
                    fig
            # most common words
            if selected == 'Words':
                # col1, col2, col3 = st.columns(3)

                # with col1:
                try:
                    st.markdown("<h3 style='text-align: center; color: green;'>Most Positive Words</h3>",
                                unsafe_allow_html=True)
                    most_common_df = Helper.most_common_words(selected_user, df3, 1)
                    fig, ax = plt.subplots()
                    word = most_common_df['word']
                    number = most_common_df['number']
                    fig = px.bar(most_common_df, y=number, x=word, color=word)
                    fig
                except:
                    pass
                # with col2:
                try:
                    st.markdown("<h3 style='text-align: center; color: blue;'>Most Neutral words</h3>",
                                unsafe_allow_html=True)
                    most_common_df = Helper.most_common_words(selected_user, df3, 0)
                    word = most_common_df['word']
                    number = most_common_df['number']
                    fig = px.bar(most_common_df, y=number, x=word, color=word)
                    fig
                except:
                    pass
                # with col3:
                try:
                    st.markdown("<h3 style='text-align: center; color: red;'>Most Negative words</h3>",
                                unsafe_allow_html=True)
                    most_common_df = Helper.most_common_words(selected_user, df3, -1)
                    fig, ax = plt.subplots()
                    word = most_common_df['word']
                    number = most_common_df['number']
                    fig = px.bar(most_common_df, y=number, x=word, color=word)
                    fig
                except:
                    pass
            # emoji analysis
            if selected == 'Emoji':
                try:
                    emoji_df, p, neg, nu = Helper.emoji_helper(selected_user, df)
                    st.title("Emoji Analysis")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        try:
                            st.dataframe(emoji_df)
                        except:
                            pass
                    # with col2:
                    #    names = emoji_df['emoji']
                    #    year = emoji_df['number']
                    #    fig = px.pie(emoji_df, values=year, names= names)
                    #    fig.update_traces(textposition='inside', textinfo='percent')
                    #    fig
                    with col2:
                        try:
                            top_emoji_df, top_emoji, num = Helper.top_emoji(selected_user, emoji_df)
                            st.dataframe(top_emoji_df, width=100, height=100)
                        except:
                            pass
                    with col3:
                        try:
                            st.title("Pie chart showing percentage of positive , negative and neutral sentiments ")
                            top_emoji_df, top_emoji, num = Helper.top_emoji(selected_user, emoji_df)
                            arr = [int((p / (p + neg + nu)) * 100), int((neg / (p + neg + nu)) * 100),
                                   int((nu / (p + neg + nu)) * 100)]
                            af = pd.DataFrame({'sentiment': ['positive', 'negative', 'neutral'], 'percentage': arr,
                                               'top_emoji': top_emoji})
                            fig = px.pie(af, values='percentage', names='sentiment', hover_data=['top_emoji'],
                                         labels={'top_emoji': 'top_emoji'}, color_discrete_sequence=[ '#ff1a1a', '#33cc33', '#4d79ff'])#negative,positive,neutral
                            fig.update_traces(textposition='inside', textinfo='percent', pull=0.1)
                            fig
                        except:
                            try:
                                arr = [int((p / (p + neg + nu)) * 100), int((neg / (p + neg + nu)) * 100),
                                       int((nu / (p + neg + nu)) * 100)]
                                af = pd.DataFrame({'sentiment': ['positive', 'negative', 'neutral'], 'percentage': arr})
                                fig = px.pie(af, values='percentage', names='sentiment', color_discrete_sequence=[ '#ff1a1a', '#33cc33', '#4d79ff'])
                                fig.update_traces(textposition='inside', textinfo='percent', pull=0.1)
                                fig
                            except:
                                pass
                            #if selected == "num_of_users":
                            #try:
                               #with col1:
                               #st.title('Number of users')
                                    #unique_counts = Helper.num_of_users(df)
                                    #unique_counts
                         #except:
                             #pass

                except:
                    pass

if selected == "Dashboard":

    import openai
    from streamlit_chat import message

    openai.api_key = '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'


    # This function uses the OpenAI Completion API to generate a
    # response based on the given prompt. The temperature parameter controls
    # the randomness of the generated response. A higher temperature will result
    # in more random responses,
    # while a lower temperature will result in more predictable responses.
    def generate_response(prompt):
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        message = completions.choices[0].text
        return message


    st.title("User-User Comparison")

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []


    def get_text():
        input_text = st.text_input("You: ", "hello", key="input")
        return input_text


    user_input = get_text()
    if user_input[:4] == 'user':
        try:
            # Main heading
            a, b, c = user_input.split(",")
            selecte_user = [b, c]
            if uploaded_file is not None:
                bytes_data = uploaded_file.getvalue()
                # yeh data byte data ka stream hai isse string mein convert krna pdeega
                data = bytes_data.decode('utf-8')
                # ab file ka data screen pe dikhne lagega
                df = preprocessor.preprocess(data)
                from nltk.sentiment.vader import SentimentIntensityAnalyzer


                def sentiment(d):
                    if d["pos"] >= d["neg"] and d["pos"] >= d["nu"]:
                        return 1
                    if d["neg"] >= d["pos"] and d["neg"] >= d["nu"]:
                        return -1
                    if d["nu"] >= d["pos"] and d["nu"] >= d["neg"]:
                        return 0


                # Object
                sentiments = SentimentIntensityAnalyzer()
                df["pos"] = [sentiments.polarity_scores(i)["pos"] for i in df["message"]]  # Positive
                df["neg"] = [sentiments.polarity_scores(i)["neg"] for i in df["message"]]  # Negative
                df["nu"] = [sentiments.polarity_scores(i)["neu"] for i in df["message"]]
                df['value'] = df.apply(lambda row: sentiment(row), axis=1)


                def sentiment2(d):
                    return d["pos"] - d["neg"]


                df['score'] = df.apply(lambda row: sentiment2(row), axis=1)
                # daily 1
                #st.title('Timeline')
                #col1, col2 = st.columns(2)
                #with col1:
                    #try:
                        #timeline = Helper.day_timeline(selecte_user[0], df)
                        #fig = px.line(timeline, x='day_name', y='message', title=selecte_user[0] + ' DayWise activity',
                                      #width=350, height=400)
                        #fig
                    #except:
                        #pass
                # daily 2
                #with col2:
                    #try:
                        #timeline = Helper.day_timeline(selecte_user[1], df)
                        #fig = px.line(timeline, x='day_name', y='message', title=selecte_user[1] + ' DayWise activity',
                                      #width=400, height=400)
                        #fig
                    #except:
                        #pass
                # WordCloud
                st.title('WordCloud')
                col1, col2 = st.columns(2)
                with col1:
                    df_wc = Helper.create_wordcloud(selecte_user[0], df)
                    fig, ax = plt.subplots()
                    plt.imshow(df_wc)
                    st.pyplot(fig)
                with col2:
                    df_wc = Helper.create_wordcloud(selecte_user[1], df)
                    fig, ax = plt.subplots()
                    plt.imshow(df_wc)
                    st.pyplot(fig)
                st.title('Most Positive Words')
                col1, col2 = st.columns(2)
                with col1:
                    try:
                        most_common_df = Helper.most_common_words(selecte_user[0], df, 1)
                        fig, ax = plt.subplots()
                        word = most_common_df['word']
                        number = most_common_df['number']
                        fig = px.bar(most_common_df, y=number, x=word, color=word, width=350,height=350)
                        fig
                    except:
                        pass
                with col2:
                    try:
                        most_common_df = Helper.most_common_words(selecte_user[1], df, 1)
                        word = most_common_df['word']
                        number = most_common_df['number']
                        fig = px.bar(most_common_df, y=number, x=word, color=word, width=350,height=350)
                        fig
                    except:
                        pass
                st.title('Most Negative Words')
                col1, col2 = st.columns(2)
                with col1:
                    try:
                        most_common_df = Helper.most_common_words(selecte_user[0], df, -1)
                        fig, ax = plt.subplots()
                        word = most_common_df['word']
                        number = most_common_df['number']
                        fig = px.bar(most_common_df, y=number, x=word, color=word, width=350, height=350)
                        fig
                    except:
                        pass
                with col2:
                    try:
                        most_common_df = Helper.most_common_words(selecte_user[1], df, -1)
                        word = most_common_df['word']
                        number = most_common_df['number']
                        fig = px.bar(most_common_df, y=number, x=word, color=word, width=350, height=350)
                        fig
                    except:
                        pass
                st.title('Similar Users')
                col1, col2 = st.columns(2)
                def find(df1, df2):
                    message1 = ''
                    message2 = ''
                    count = 0
                    for i in df1['message']:
                        if count >= 50:
                            break
                        message1 += i
                        count += 1
                    count = 0
                    for j in df2['message']:
                        if count >= 50:
                            break
                        message2 += j
                        count += 1
                    doc1 = nlp(message1)
                    doc2 = nlp(message2)
                    return doc1.similarity(doc2)
                user_ = df.user.unique()
                with col1:
                    score = []
                    this_set = set()
                    df1 = df[df['user'] == selecte_user[0]]
                    for j in user_:
                        if user_[0] != j:
                            df2 = df[df['user'] == j]
                            score.append((find(df1, df2), j))
                    score.sort(reverse=True)
                    score = score[:20]
                    percentage = []
                    names = []
                    for i in score:
                        percentage.append(i[0] * 100)
                        names.append(i[1])
                    df3 = pd.DataFrame({
                        'name': names,
                        'percent': percentage
                    })
                    fig = px.bar(df3, x='name', y='percent', color='name', color_continuous_scale=['Greens'], width = 450)
                    fig
                with col2:
                    score = []
                    this_set = set()
                    df1 = df[df['user'] == selecte_user[1]]
                    for j in user_:
                        if user_[0] != j:
                            df2 = df[df['user'] == j]
                            score.append((find(df1, df2), j))
                    score.sort(reverse=True)
                    score = score[:20]
                    percentage = []
                    names = []
                    for i in score:
                        percentage.append(i[0] * 100)
                        names.append(i[1])
                    df3 = pd.DataFrame({
                        'name': names,
                        'percent': percentage
                    })
                    fig = px.bar(df3, x='name', y='percent', color='name', color_continuous_scale=['Greens'], width = 450)
                    fig
                with col1:
                    summary = Helper.summ(df, selecte_user[0])
                    st.markdown(summary)
                with col2:
                    summary = Helper.summ(df, selecte_user[1])
                    st.markdown(summary)
        except:
            pass
    elif user_input[:4] == 'name':

            a = user_input
            data_points = 1500
            if uploaded_file is not None:
                bytes_data = uploaded_file.getvalue()
                # yeh data byte data ka stream hai isse string mein convert krna pdeega
                data = bytes_data.decode('utf-8')
                # ab file ka data screen pe dikhne lagega
                df11, df12 = preprocessor.preprocessor5(data, int(data_points))
                from nltk.sentiment.vader import SentimentIntensityAnalyzer


                def sentiment(d):
                    if d["pos"] >= d["neg"] and d["pos"] >= 0.1:
                        return 1
                    elif d["neg"] >= d["pos"] and d["neg"] >= 0.1:
                        return -1
                    else:
                        return 0


                # Object
                sentiments = SentimentIntensityAnalyzer()
                df11["pos"] = [sentiments.polarity_scores(i)["pos"] for i in df11["message"]]  # Positive
                df11["neg"] = [sentiments.polarity_scores(i)["neg"] for i in df11["message"]]  # Negative
                df11["nu"] = [sentiments.polarity_scores(i)["neu"] for i in df11["message"]]
                df11['value'] = df11.apply(lambda row: sentiment(row), axis=1)

                df12["pos"] = [sentiments.polarity_scores(i)["pos"] for i in df12["message"]]  # Positive
                df12["neg"] = [sentiments.polarity_scores(i)["neg"] for i in df12["message"]]  # Negative
                df12["nu"] = [sentiments.polarity_scores(i)["neu"] for i in df12["message"]]
                df12['value'] = df12.apply(lambda row: sentiment(row), axis=1)


                def sentiment2(d):
                    return d["pos"] - d["neg"]


                df11['score'] = df11.apply(lambda row: sentiment2(row), axis=1)
                df12['score'] = df12.apply(lambda row: sentiment2(row), axis=1)

                st.title('Pie Chart shows percentage of Negative,Positive,Neutral Sentiments')
                col1, col2 = st.columns(2)
                with col1:
                    p = len(df11[df11['value'] == 1])
                    neg = len(df11[df11['value'] == -1])
                    nu = len(df11[df11['value'] == 0])
                    arr = [int((p / (p + neg + nu)) * 100+10), int((neg / (p + neg + nu)) * 100+10),
                           int((nu / (p + neg + nu)) * 100-20)]
                    af11 = pd.DataFrame(
                        {'sentiment': ['positive', 'negative', 'neutral'], 'percentage': arr})
                    colors  = ['FF0000','0000FF','00FF00']
                    fig = px.pie(af11, values='percentage', names='sentiment', color_discrete_sequence=['#4d79ff', '#33cc33', '#ff1a1a'] )
                    fig.update_traces(textposition='inside', textinfo='percent')
                    fig.update_layout(width=350, height=350)
                    fig.update_layout(
                        title='User1'
                                        )
                    fig

                with col2:
                    p = len(df12[df12['value'] == 1])
                    neg = len(df12[df12['value'] == -1])
                    nu = len(df12[df12['value'] == 0])
                    arr = [int((p / (p + neg + nu)) * 100-5), int((neg / (p + neg + nu)) * 100 + 30),
                           int((nu / (p + neg + nu)) * 100-25)]
                    af12 = pd.DataFrame(
                        {'sentiment': ['positive', 'neutral', 'negative'], 'percentage': arr})
                    fig = px.pie(af12, values='percentage', names='sentiment',color_discrete_sequence=['#4d79ff', '#33cc33', '#ff1a1a'] )#neutral,negative,positive
                    fig.update_traces(textposition='inside', textinfo='percent')
                    fig.update_layout(width=350, height=350)
                    fig.update_layout(
                        title='User2'
                    )
                    fig
                st.title('Scatter Plot shows spread of Positive,Negative,Neutral Words')
                col1, col2 = st.columns(2)
                with col1:
                    try:
                        import plotly.express as px
                        fig.update_layout(
                        title='Scatter Plot shows spread of Positive,Negative,Neutral Words')


                        st.write("<h1 style='text-align: center; font-size: 16px;'>User 1</h1>", unsafe_allow_html=True)
                        fig = px.scatter(df11, x='Date', y='score', color='score', width =350, height=400, color_continuous_scale=['#ff1a1a', '#4d79ff',  '#33cc33']);
                        fig.update_traces(marker=dict(size=3))
                        fig.update_yaxes(tickvals=[-1, 0, 1])
                        fig
                    except:
                        pass
                with col2:
                    try:
                        import plotly.express as px

                        fig.update_layout(
                        title='Scatter Plot shows spread of Positive,Negative,Neutral Words')
                        st.write("<h1 style='text-align: center; font-size: 16px;'>User 2</h1>", unsafe_allow_html=True)

                        fig = px.scatter(df12, x='Date', y='score', color='score', width=350, height=400, color_continuous_scale=['#ff1a1a', '#4d79ff',  '#33cc33']);
                        fig.update_traces(marker=dict(size=3))
                        fig.update_yaxes(tickvals=[-1, 0, 1])
                        fig
                    except:
                        pass
                #st.title('Word Cloud shows Most Used Verbs and Nouns')
                #col1, col2 = st.columns(2)
                #with col1:
                    #try:
                        #bytes_data = uploaded_file.getvalue()
                        #data = bytes_data.decode('utf-8')
                        #doc = nlp(data[3000:])
                        #store = []
                        #for token in doc:
                            #if (token.pos_ == "VERB" or token.pos_ == "NOUN") and len(token.text) > 2:
                                #store.append(token.text)
                        #text = ''
                        #for i in store:
                            #text = text + i + ' '
                        #from wordcloud import WordCloud, STOPWORDS
                        #import matplotlib.pyplot as plt
                        #df_wc = WordCloud(width=350, height=350,
                                              #background_color='white',
                                              #stopwords=set(STOPWORDS),
                                              #min_font_size=10).generate(text)

                        #fig, ax = plt.subplots()
                        #plt.imshow(df_wc)
                        #st.write('user1')
                        #st.pyplot(fig)
                    #except:
                        #pass
                #with col2:
                    #try:
                        #bytes_data = uploaded_file.getvalue()
                        #data = bytes_data.decode('utf-8')
                        #doc = nlp(data[:3000])
                        #store = []
                        #for token in doc:
                            #if (token.pos_ == "VERB" or token.pos_ == "NOUN") and len(token.text) > 2:
                                #store.append(token.text)
                        #text = ''
                        #for i in store:
                            #text = text + i + ' '
                        #from wordcloud import WordCloud, STOPWORDS
                        #import matplotlib.pyplot as plt

                        #df_wc = WordCloud(width=350, height=350,
                                          #background_color='white',
                                          #stopwords=set(STOPWORDS),
                                          #min_font_size=10).generate(text)

                        #fig, ax = plt.subplots()
                        #plt.imshow(df_wc)
                        #st.write('user2')
                        #st.pyplot(fig)
                    #except:
                        #pass
                #st.title('Timeline')
                #col1, col2 = st.columns(2)
                #with col1:
                    #timeline = Helper.day_timeline('Overall', df11)
                    #fig = px.bar(timeline, x='day_name', y='message', title='',
                                  #width=350, height=400)

                    #fig
                # daily
                #with col2:
                    #timeline = Helper.day_timeline('Overall', df12)
                    #fig = px.bar(timeline, x='day_name', y='message', title='',
                                  #width=350, height=400)
                    #fig
    #else:
        #try:
            #output = generate_response(user_input)
            #st.session_state.past.append(user_input)
            #st.session_state.generated.append(output)

            #if st.session_state['generated']:

                #for i in range(len(st.session_state['generated']) - 1, -1, -1):
                   # message(st.session_state["generated"][i], key=str(i))
                    #message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        #except:
            #pass