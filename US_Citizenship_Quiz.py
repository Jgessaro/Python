# First introduction
# At later time, input more info about the random

print("""Hello! Welcome to the Quiz!
	This is the 2008 version of the US Civis Test. 
	It consists of 100 questions.""")

quiz_start = input('Are you ready to begin? ' ).lower()
score = 0

if quiz_start != "yes":
	quit()

print("Okay! Let's begin!")


q_1 = input("1.) What is the supreme law of the land? ")
if q_1 == "the Constitution":
	print("Correct!")
	score += 1
else:
	print("Incorrect! Answer: the Consitution")

q_2 = input("2.) What does the Constitution do? ").lower()
if q_2 in ["sets up the government", "defines the government", "protects basic rights of americans"]:
	print("Correct!")
	score += 1
else:
	print("Incorrect! Answers: sets up the government, defines the government, or protects basic rights of americans")

q_3 = input("3.) The idea of self-government is in the first three words of the Constitution. What are these THREE words? ")
if q_3 == "We the People":
	print("Correct!")
	score += 1
else:
	print("Incorrect! Answer: We the People")

q_4 = input("4.) What is an amendment? ")
if q_4 in ["a change", "an addition"]:
	print("Correct!")
	print('Note: this is in regards to the Constitution')
	score += 1
else:
	print("Incorrect! Answers: a change, or an addition")

q_5 = input("5.) What do we call the first ten amendments to the Constitution? ")
if q_5 == "the Bill of Rights":
	print("Correct!")
	score += 1
else:
	print("Incorrect! Answer: the Bill of Rights")

q_6 = input("6.) What is ONE right or freedom from the First Amendment? ")
if q_6 in ["speech", "religion", "assembly", "press", "petition the govnerment"]:
	print("Correct!")
	score += 1
else:
	print("Incorrect! Answers: speech, religion, assembly, press, or petition the government")

q_7 = input("7.) How many amendments does the Constitution have? ")
if q_7 == '27':
	print("Correct!")
	score += 1
else:
	print("Incorrect! Answer: 27")

q_8 = input("8.) What did the Declaration of Independence do? ")
if q_8 in ['announced our independence', 'declared our independence', 'said that the United States is free']:
	print("Correct!")
	score += 1
else:
	print("Incorrect! Answers: announced our independence, declared our independence, or said that the United States is free")

q_9 = input("9.) What are two rights in the Declaration of Independence? ").lower()
if q_9 in ['life and liberty', 'liberty and the pursuit of happiness', 'life and the pursuit of happiness','liberty and life','the pursuit of happiness and liberty','the pursuit of happiness and life']:
	print("Correct!")
	score += 1
else:
	print("Incorrect! Answers: life, liberty, or purusit of happiness")

q_10 = input("10.) What is freedom of religion? ").lower()
if q_10 == "can practice any religion":
	print("Correct!")
	score += 1
else:
	print("Incorrect! Answer: you can practice any religion")
	
q_11 = input("11.) What is the economic system in the United States? ").lower()
if q_11 in ['capitalist economy', 'market economy']:
	print("Correct!")
	score += 1
else:
	print("Incorrect! Answers: capitalist economy, or markey economy")

q_12 = input("12.) What is the 'rule of law'? ").lower()
if q_12 in ['everyone must follow the law','leaders must obey the law','government must obey the law','no one is above the law']:
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answers: everyone must follow the law, leaders must obey the law, government must obey the law, or no one is above the law')

# This starts Part B
q_13 = input("13.) Name one branch or part of the government: ").lower()
if q_13 in ["congress","legislative","president","executive","the courts","judicial"]:
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answers: Congress, legislative, President, executive, the courts, or judicial')

q_14 = input("14.) What stops one branch of government from becoming too powerful? ").lower()
if q_14 in ["checks and balances","separation of powers"]:
	print("Correct!")
	score += 1
else:
	print("Incorrect! Answers: checks and balances, or separation of powers")

q_15 = input("15.) Who is in charge of the executive branch? ").lower()
if q_15 == "the president":
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: the President')

q_16 = input("16.) Who makes federal laws? ").lower()
if q_16 in ['congress','senate and the house','legislative branch']:
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answers: Congress, Senate and the House, or legislative branch')

x_17,y_17 = input("17.) What are the TWO parts of the US Congress? Enter first: ").lower(), input("Enter second: ").lower()
if x_17 and y_17 in ['the senate', 'house of representatives']:
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: the Senate and House of Representatives')

q_18 = input("18.) How many US Senators are there? ")
if q_18 == "100":
	print('Correct! NOTE: there are 2 per state.')
	score += 1
else:
	print('Incorrect! Answer: 100; there are 2 per state')

q_19 = input("19.) We elect a US Senator for how many years? ")
if q_19 == "6":
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: 6')

q_20 = input("20.) Who is ONE of your state's Senators now? ")
if q_20 in ['Richard Burr','Thom Tillis'] :
	print('Correct! As of August 19, 2022')
	score += 1
else:
	print('Incorrect! Answers: Richard Burr or Thom Tillis')

q_21 = input("21.) The House of Representatives has how many voting members? ")
if q_21 == "435":
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: 435')

q_22 = input("22.) We elect a US Representative for how many years? ")
if q_22 == "2":
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: 2')

q_23 = input("23.) Name your US Representative: ")
if q_23 == "Richard Hudson":
	print('Correct! NOTE: As of August 19, 2022.')
	score += 1
else:
	print('Incorrect! Answer: Richard Hudson')

q_24 = input("24.) Who does a US Senator represent? ").lower()
if q_24 == "all people of the state":
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: all people of the state')

q_25 = input("25.) Why do some states have more Representatives than others? ").lower()
if q_25 in ["the state's population",'they have more people','some states have more people']:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: the state's population, they have more people, some states have more people")

q_26 = input("26.) We elect a President for how many years? ")
if q_26 == "4":
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: 4')

q_27 = input("27.) In what month do we vote for President? ").lower()
if q_27 == "november":
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: November')

q_28 = input("28.) What is the name of the President of the United States now? ")
if q_28 == "Joe Biden":
	print('Correct! NOTE: As of August 19, 2022')
	score += 1
else:
	print('Incorrect! Answer: Joe Biden')

q_29 = input("29.) What is the name of the Vice President now? ")
if q_29 == "Kamala Harris":
	print('Correct! NOTE: As of August 19, 2022')
	score += 1
else:
	print('Incorrect! Answer: Kamala Harris')

q_30 = input("30.) If the President can no longer serve, who becomes President? ").lower()
if q_30 == 'the vice president':
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: the Vice President')

q_31 = input("31.) If both the President and Vice President can no longer serve, who becomes President? ").lower()
if q_31 == 'the speaker of the house':
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: the Speaker of the House')

q_32 = input("32.) Who is the Commander in Chief of the military? ").lower()
if q_32 == 'the president':
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: the President')

q_33 = input("33.) Who signs bills to become laws? ").lower()
if q_33 == 'the president':
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: the President')

q_34 = input("34.) Who vetoes bills? ").lower()
if q_34 == 'the president':
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: the President')

q_35 = input("35.) What does the President's Cabinet do? ").lower()
if q_35 in ['advises the president','advise the president']:
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: advises the President')

x_36,y_36 = input("36.) What are TWO Cabinet-level positions? Enter first: ").lower(), input("Enter second: ").lower()
if x_36 and y_36 in ['secretary of agriculture','secretary of commerce','secretary of defense','secretary of education','secretary of energy','secretary of health and human services','secretary of homeland security','secretary of housing and urban development','secretary of the interior','secretary of labor','secretary of state','secretary of transportation','secretary of the treasury','secretary of veteran affairs','attorney general','vice president']:
	print('Correct! There are 16 total positions')
	score += 1
else:
	print('Incorrect! Answers: Secretary of Agriculture, Secretary of Commerce, Secretary of Defense, Secretary of Education, Secretary of Energy, Secretary of Health and Human Services, Secretary of Homeland Security, Secretary of Housing and Urban Development, Secretary of the Interior, Secretary of Labor, Secretary of State, Secretary of Transportation, Secretary of the Treasury, Secretary of Veteran Affairs, Attorney General, or Vice President')

q_37 = input("37.) What does the judicial branch do? ").lower()
if q_37 in ['reviews laws','explains laws','resolves disputes','interprets the constitution'] :
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answers: reviews laws, explains laws, resolves disputes, interprets the Constitution')

q_38 = input("38.) What is the highest court in the United States? ").lower()
if q_38 == "the supreme court":
	print('Correct!')
	score += 1
else:
	print('Incorrect! Answer: the Supreme Court')

q_39 = input("How many justices are on the Supreme Court? ")
if q_39 == ("9"):
	print('Correct! As of August 20, 2022')
	score += 1
else:
	print("Incorrect! Answer: 9")

q_40 = input("Who is the Chief Justice of the United States now? ").lower()
if q_40 == ("john roberts"):
	print('Correct! As of August 20, 2022')
	score += 1
else:
	print("Incorrect! Answer: ")

q_41 = input("Under our Constitution, some powers belong to the federal government. What is ONE power of the federal government? ").lower()
if q_41 in ["to print money","to declare war","to create an army","to make treaties"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: to print money, to declare war, to create an army, or to make treaties")

q_42 = input("Under our Constitution, some powers belong to the states. What is ONE power of the states? ").lower()
if q_42 in ["provide schooling and education","provide protection","provide safety","give a driver's license","approve zoning and land use"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: provide schooling and education, provide protection, provide safety, give a driver's license, or approve zoning and land use")

q_43 = input("Who is the Governor of your state now? ").lower()
if q_43 == ("roy cooper"):
	print('Correct! As of August 20, 2022')
	score += 1
else:
	print("Incorrect! Answer: Roy Cooper")

q_44 = input("What is the capital of your state? ").lower()
if q_44 == ("raleigh"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: Raliegh")

x_45,y_45 = input("What are the TWO major political parties in the United States? Enter first: ").lower(),input("Enter second: ")
if x_45 and y_45 in ["democratic","republican"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: Democractic, Republican")

q_46 = input("What is the political party of the President now? ").lower()
if q_46 == ("democratic"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: Democratic")

q_47 = input("What is the name of the Speaker of the House of Representatives now? ").lower()
if q_47 == ("nancy pelosi"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: Nancy Pelosi")
# Part C Rights and Responsibilities
q_48 = input("There are four amendments to the Constitution about who can vote. Describe ONE of them. ")
if q_48 in ["citizens 18 and older can vote","you don't have to pay a tax to vote","any citizen can vote","a male citizen of any race can vote"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: citizens 18 and older can vote, you don't have to pay a tax to vote, any citizen can vote, a male citizen of any race can vote")

q_49 = input("What is ONE responsibility that is only for United States citizens? ")
if q_49 in ["serve on a jury","vote in a federal election"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: serve on a jury, or vote in a federal election")

q_50 = input("Name ONE right only for United States citizens. ")
if q_50 in ["vote in a federal election","run for federal office"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: vote in a federal election, or run for federal office")

x_56,y_56 = input("What are two rights of everyone living in the United States? Enter first: ").lower(),input("Enter second: ").lower()
if x_56 and y_56 in ["freedom of expression","freedom of speech","freedom of assembly","freedom to petition the government","freedom of religion","the right to bear arms"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: freedom of expression, freedom of speech, freedom of assembly, freedom to petition the government, freedom of religion, or the right to bear arms")

q_52 = input("What do we show loyalty to when we say the Pledge of Allegiance? ").lower()
if q_52 in ["the united states","the flag"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: the United States, or the flag")

q_53 = input("What is one promise you make when you become a United States citizen? ").lower()
if q_53 in ["give up loyalty to other countries","defend the constitution and laws of the united states","obey the laws of the united states","serve in the us military","serve the nation","be loyal to the united states"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: give up loyalty to other countries, defend the Constitution and laws of the United States, obey the laws of the United States, serve in the US military, serve the nation, or be loyal to the United States")

q_54 = input("How old do citizens have to be to vote for President? ")
if q_54 == ("18"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: 18")

x_55,y_55 = input("What are TWO ways that Americans can participate in their democracy? Enter first: ").lower(),input("Enter second: ").lower()
if x_55 and y_55 in ["vote","join a political party","help with a campaign","join a civic group","join a community group","give an elected official your opinion on an issue","call senators and representatives","publicly support or oppose an issue or policy","run for office","write to a newspaper"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: vote, join a political pary, help with a campaign, join a civic group, join a community group, give an elected official your opinion on an issue, call senators and representatives, publicly support or oppose an issue or policy, run for office, write to a newspaper")

q_56 = input("When is the last day you can send in federal income tax forms? ").lower()
if q_56 == (" april 15"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: April 15")

q_57 = input("When must all men register for the Selective Service? ").lower()
if q_57 in ["at 18"," between 18 and 26"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: at 18, or between 18 and 26")
#Part A Colonial Period and Independence
q_58 = input("What is one reason colonists came to America? ")
if q_58 in ["freedom","political liberty","religious freedom","economic opportunity","practice their religion","escape persecution"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: freedom, political liberty, religious freedom, economic opportunity, practice their religion, escape persecution")

q_59 = input("Who lived in America before the Europeans arrived? ").lower()
if q_59 in ["american indians","native americans"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: ")

q_60 = input("What group of people was taken to America and sold as slaves? ").lower()
if q_60 == ("africans "):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: Africans")

q_61 = input("Why did the colonists fight the British? ").lower()
if q_61 in ["because of high taxes","because the british army stayed in their homes","because they didn't have self-government"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: because of high taxes, because the British army stayed in their homes, or because they didn't have self-government")

q_62 = input("Who wrote the Declaration of Independence? ").lower()
if q_62 == ("thomas jefferson"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: Thomas Jefferson")

q_63 = input("When was the Declaration of Independence adopted? ").lower()
if q_63 == ("july 4, 1776"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: July 4, 1776")

x_64,y_64,z_64 = input("There were 13 original states. Name three. Enter first: ").lower(),input("Enter second: ").lower(),input("Enter third: ").lower()
if x_64 and y_64 and z_64 in ["new hampshire","massachusetts","rhode island","connecticut","new york","new jersey","pennsylvania","delaware","maryland","virginia","north carolina","south carolina","georgia"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: new hampshire, massachusetts, rhode island, connecticut, new york, new jersey, pennsylvania, delaware, maryland, virginia, north carolina, south carolina, georgia")

q_65 = input("What happened at the Constitutional Convention? ").lower()
if q_65 in ["the constitution was written","the founding fathers wrote the constitution"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: the Constitution was written, or the Founding Fathers wrote the Constitution")

q_66 = input("When was the Constitution written? ")
if q_66 == ("1787"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: 1787")

q_67 = input("The Federalist Papers supported the passage of the U.S. Constitution. Name one of the writers. ").lower()
if q_67 in ["james madison","alexander hamilton","john jay","publius"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: James Madison, Alexander Hamilton, John Jay, Publius")

q_68 = input("Who is the 'Father of Our Country'? ").lower()
if q_68 == ("george washington"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: George Washington")

q_69 = input("Who was the first President? ").lower()
if q_69 == ("george washington"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: George Washington")
#Part B 1800s
q_70 = input("What territory did the United States buy from France in 1803? ").lower()
if q_70 == ("louisiana"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: Louisiana")

q_71 = input("Name ONE war fought by the United States in the 1800s. ").lower()
if q_71 in ["war of 1812","mexican-american war","civil war","spanish-american war"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: War of 1812, Mexican-American War, Civil War, Spanish-American War")

q_72 = input("Name the U.S. war between the North and the South. ").lower()
if q_72 == ("civil war"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: Civil War")

q_73 = input("Name ONE problem that led to the Civil War. ").lower()
if q_73 in ["slavery","economic reasons","states' rights"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: Slavery, Economic reasons, or states' rights")

q_74 = input("What was ONE important thing that Abraham Lincoln did? ").lower()
if q_74 in ["freed the slaves","saved the union","led the united states during the civil war"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: freed the slaves, saved the Union, led the United States during the Civil War")

q_75 = input("What did the Emancipation Proclamation do? ").lower()
if q_75 in ["freed the slaves","freed slaves in the confederacy","freed slaves in the confederate states","freed slaves in most southern states"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: freed the slaves, freed slaves in the Confederacy, freed slaves in the Confederate states, freed slaves in most Southern states")

q_76 = input("What did Susan B. Anthony do? ").lower()
if q_76 in ["fought for women's rights","fought for civil rights"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: fought for women's rights, or fought for civil rights")
#Part C: Recent American History and Other Important Historical Information
q_77 = input("Name ONE war fought by the United States in the 1900s. ").lower()
if q_77 in ["world war 1","world war 2","korean war","vietnam war","gulf war"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: World War 1, World War 2, Korean War, Vietnam War, Gulf War")

q_78 = input("Who was President during World War I? ").lower()
if q_78 == ("woodrow wilson"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: Woodrow Wilson")

q_79 = input("Who was President during the Great Depression and World War II? ").lower()
if q_79 == ("franklin roosevelt"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: Franklin Roosevelt")

x_80,y_80,z_80 = input("Who did the United States fight in World War II? Enter first: ").lower(),input("Enter second: ").lower(),input("Enter third: ").lower()
if x_80 and y_80 and z_80 in ["japan","germany","italy"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: Japan, Germany, and Italy")

q_81 = input("Before he was President, Eisenhower was a general. What war was he in? ").lower()
if q_81 == ("world war 2"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: World War 2")

q_82 = input("During the Cold War, what was the main concern of the United States? ").lower()
if q_82 == ("communism"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: Communism")

q_83 = input("What movement tried to end racial discrimination? ").lower()
if q_83 == ("civil rights"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: Civil Rights")

q_84 = input("What did Martin Luther King, Jr. do? ").lower()
if q_84 in ["fought for civil rights","worked for equality for all americans"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: fought for civil rights, or fought for equality for all Americans")

q_85 = input("What major event happened on September 11, 2001, in the United States? ").lower()
if q_85 == ("terrorists attacked the united states "):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: terrorists attacked the United States")

q_86 = input("Name ONE American Indian tribe in the United States. ").lower()
if q_86 in ["cherokee","navajo","sioux","chippewa","choctaw","pueblo","apache","iroquois","creek","blackfeet","seminole","cheyenne","arawak","shawnee","mohegan","huron","oneida","lakota","crow","teton","hopi","inuit"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: Cherokee, Navajo, Sioux, Chippewa, Choctaw, Pueblo, \nApache, Iroquois, Creek, Blackfeet, Seminole, Cheyenne, Arawak, \nShawnee, Mohegan, Huron, Oneida, Lakota, Crow, Teton, Hopi, Inuit")

q_87 = input("Name ONE of the two longest rivers in the United States. ").lower()
if q_87 in ["mississippi","missouri"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: Mississippi, or Missouri")

q_88 = input("What ocean is on the West Coast of the United States? ").lower()
if q_88 in ["pacific", "pacific ocean"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: Pacific or Pacific Ocean")

q_89 = input("What ocean is on the East Coast of the United States? ").lower()
if q_89 in ["atlantic","atlantic ocean"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: Atlantic, or Atlantic Ocean")

q_90 = input("Name ONE U.S. territory. ").lower()
if q_90 in ["puerto rico","us virgin islands","american samoa","nothern mariana islands","guam"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: Puerto Rico, US Virgin Islands, American Samoa, Nothern Mariana Islands, Guam")

q_91 = input("Name ONE state that borders Canada. ").lower()
if q_91 in ["maine","new hampshire","vermont","new york","pennsylvania","ohio","michigan","minnesota","north dakota","montana","idaho","washington","alaska"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: Maine, New Hampshire, Vermont, New York, Pennsylvania, Ohio, Michigan, Minnesota, North Dakota, Montana, Idaho, Washington, or Alaska")

q_92 = input("Name ONE state that borders Mexico. ").lower()
if q_92 in ["california","arizona","new mexico","texas"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: California, Arizona, New Mexico, or Texas")

q_93 = input("What is the capital of the United States? ").lower()
if q_93 == ("washington, dc"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: Washington, DC")

q_94 = input("Where is the Statue of Liberty? ").lower()
if q_94 == ("new york"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: New York")

q_95 = input("Why does the US flag have 13 stripes? ").lower()
if q_95 in ["to represent the original 13 colonies","to represent the original colonies","to represent the colonies"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: to represent the original 13 colonies, to represent the original colonies, or to represent the colonies")

q_96 = input("Why does the US flag have 50 stars? ").lower()
if q_96 in ["because each star represents a state","because there is a star for each state","because there is one for each state","because there are 50 states"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: because each star represents a state, because there is a star for each state, because there is one for each state, or because there are 50 states")

q_97 = input("What is the name of the National Anthem? ").lower()
if q_97 == ("the star-spangled banner"):
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: The Star-Spangled Banner")

q_98 = input("When do we celebrate Independence Day? ").lower()
if q_98 in ["july 4","july 4th"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answer: July 4 or July 4th")

x_99,y_99 = input("Name TWO national US holidays. Enter first: ").lower(),input("Enter second: ").lower()
if x_99 and y_99 in ["new year's day","martin luther king jr day","presidents day","memorial day","independence day","labor day","columbus day","veterans day","thanksgiving","christmas"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: New Year's Day, Martin Luther King Jr Day, Presidents Day, Memorial Day, Independence Day, \nLabor Day, Columbus Day, Veterans Day, Thanksgiving, or Christmas")

q_100 = input("What is ONE thing Benjamin Franklin is famous for? ").lower()
if q_100 in ["us diplomat","oldest member of the constitutional convention","first postmaster general of the us","writer of 'poor richards almanac","started the first free libraries"]:
	print('Correct!')
	score += 1
else:
	print("Incorrect! Answers: US diplomat, oldest member of the Constitutional Convention, first Postmaster General of the US, writer of 'Poor Richards Alamanc, or started the first free libraries")

print("Congragulations! You have completed all 100 questions! Your score is:",score)