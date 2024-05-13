import os


"""
Plant_Details = plant_data = {
    'Aloevera': [
        {
            'scientific_name': 'Aloe vera',
            'scientific_medicinal_properties': 'Aloe vera contains various vitamins and minerals such as vitamins A, C, and E, as well as antioxidants and enzymes.',
            'common_location': 'Aloe vera is native to the Arabian Peninsula, but it is cultivated worldwide, especially in tropical climates.',
            'popular_usecase': 'Aloe vera gel is commonly used topically for skin conditions such as burns, wounds, and sunburns. It is also used in cosmetic products for its moisturizing properties.',
            'Disclaimer': 'Consult a healthcare professional before using aloe vera, especially if you have any skin allergies or medical conditions.',
            'lament_medicinal_property': 'Aloe vera gel is soothing and moisturizing for the skin. It has anti-inflammatory properties and may help promote wound healing.'
        }
    ],
    'Amla': [
        {
            'scientific_name': 'Phyllanthus emblica',
            'scientific_medicinal_properties': 'Amla, also known as Indian gooseberry, is rich in vitamin C, antioxidants, and other nutrients.',
            'common_location': 'Amla trees are native to India and are cultivated in various parts of Asia.',
            'popular_usecase': 'Amla is used in Ayurvedic medicine for its rejuvenating properties and is believed to promote longevity. It is also used in culinary dishes and as a dietary supplement for its health benefits.',
            'Disclaimer': 'Consult a healthcare professional before using amla, especially if you have any medical conditions or are taking medications.',
            'lament_medicinal_property': 'Amla is known for its high vitamin C content, which supports immune health and is beneficial for hair and skin.'
        }
    ],
    'Amruta_Balli': [
        {
            'scientific_name': 'Tinospora cordifolia',
            'scientific_medicinal_properties': 'Tinospora cordifolia, also known as guduchi or amruta, has been used in Ayurvedic medicine for its immunomodulatory, anti-inflammatory, and antioxidant properties.',
            'common_location': 'Tinospora cordifolia is native to the Indian subcontinent and is found growing in tropical and subtropical regions.',
            'popular_usecase': 'In Ayurveda, amruta balli is used to boost immunity, promote overall health, and treat various ailments such as fever, diabetes, and digestive disorders. It is also used in Ayurvedic formulations for its anti-aging and rejuvenating effects.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using amruta balli, especially if you are pregnant, breastfeeding, or have any medical conditions.',
            'lament_medicinal_property': 'Amruta balli is valued for its ability to enhance immunity, support liver function, and promote overall well-being.'
        }
    ],
    'Arali': [
        {
            'scientific_name': 'Aralia elata',
            'scientific_medicinal_properties': 'Aralia elata, also known as Japanese angelica tree, is a deciduous shrub native to East Asia.',
            'common_location': 'Aralia elata grows in forests and mountainous regions of China, Korea, and Japan.',
            'popular_usecase': 'In traditional Chinese medicine, arali is used for its diuretic, antipyretic, and analgesic properties. It is believed to promote circulation, reduce inflammation, and alleviate pain. Arali root is also used as a culinary ingredient in Korean cuisine.',
            'Disclaimer': 'Consult a healthcare professional before using arali, especially if you have any medical conditions or are taking medications.',
            'lament_medicinal_property': 'Arali is valued for its anti-inflammatory and analgesic effects. It is used to relieve pain, reduce fever, and promote overall well-being.'
        }
    ],
    'Ashoka': [
        {
            'scientific_name': 'Saraca asoca',
            'scientific_medicinal_properties': 'Saraca asoca, commonly known as ashoka or sorrowless tree, is a medicinal plant native to India and Southeast Asia.',
            'common_location': 'Ashoka trees are found in the wild as well as cultivated in gardens and parks. They prefer tropical and subtropical climates.',
            'popular_usecase': 'In Ayurvedic medicine, ashoka is used to treat various gynecological disorders such as menstrual irregularities, menorrhagia, and uterine fibroids. It is also used to relieve pain, reduce inflammation, and promote overall reproductive health in women.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using ashoka, especially if you have any reproductive health concerns or are pregnant.',
            'lament_medicinal_property': 'Ashoka is valued for its beneficial effects on women\'s health. It is used to regulate menstrual cycles, reduce menstrual pain, and support reproductive wellness.'
        }
    ],
    'Ashwagandha': [
        {
            'scientific_name': 'Withania somnifera',
            'scientific_medicinal_properties': 'Withania somnifera, commonly known as ashwagandha or Indian ginseng, is a medicinal herb used in traditional Ayurvedic and Unani medicine.',
            'common_location': 'Ashwagandha is native to India, the Middle East, and parts of Africa. It is cultivated in various regions for its medicinal properties.',
            'popular_usecase': 'Ashwagandha is used to reduce stress, improve cognitive function, and enhance overall vitality and longevity. It is also used to treat various health conditions such as anxiety, depression, insomnia, and arthritis.',
            'Disclaimer': 'Consult a healthcare professional before using ashwagandha, especially if you have any medical conditions or are taking medications.',
            'lament_medicinal_property': 'Ashwagandha is known as an adaptogen, helping the body adapt to stress and promoting balance. It is used to support mental clarity, physical endurance, and emotional well-being.'
        }
    ],
    'Avacado': [
        {
            'scientific_name': 'Persea americana',
            'scientific_medicinal_properties': 'Persea americana, commonly known as avocado, is a fruit tree native to South Central Mexico.',
            'common_location': 'Avocado trees are cultivated in subtropical and tropical regions worldwide, including California, Florida, and Mediterranean countries.',
            'popular_usecase': 'Avocado fruit is prized for its nutritional value, containing healthy fats, vitamins, minerals, and antioxidants. It is used in culinary dishes such as salads, sandwiches, and smoothies for its creamy texture and flavor.',
            'Disclaimer': 'Consult a healthcare professional before consuming avocado, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Avocado is valued for its heart-healthy fats, fiber, and nutrients. It is used to support cardiovascular health, improve digestion, and promote skin and hair health.'
        }
    ],
    'Bamboo': [
        {
            'scientific_name': 'Bambusoideae',
            'scientific_medicinal_properties': 'Bamboo is a fast-growing perennial grass belonging to the Bambusoideae subfamily of the Poaceae family.',
            'common_location': 'Bamboo is native to various regions worldwide, including Asia, Africa, and the Americas. It grows in diverse climates, from tropical rainforests to temperate forests.',
            'popular_usecase': 'Bamboo has numerous uses in construction, furniture making, paper production, culinary arts, and traditional medicine. It is used in Ayurveda and traditional Chinese medicine for its medicinal properties, including antimicrobial, anti-inflammatory, and antipyretic effects.',
            'Disclaimer': 'Consult a qualified healthcare professional before using bamboo for medicinal purposes, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Bamboo is valued for its versatility and sustainability. It is used to promote wound healing, reduce inflammation, and support overall health and well-being.'
        }
    ],
    'Basale': [
        {
            'scientific_name': 'Basella alba',
            'scientific_medicinal_properties': 'Basella alba, also known as Malabar spinach or vine spinach, is a leafy green vegetable native to tropical Asia and Africa.',
            'common_location': 'Basella alba grows in warm, humid climates and is cultivated in tropical and subtropical regions worldwide.',
            'popular_usecase': 'Basale is rich in vitamins, minerals, and antioxidants. It is used as a culinary vegetable in various cuisines, including Indian, Thai, and Filipino cuisine. Basale leaves are cooked and eaten as a nutritious green vegetable.',
            'Disclaimer': 'Consult a healthcare professional before consuming basale, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Basale is valued for its nutritional content and health benefits. It is used to support eye health, boost immunity, and promote overall well-being.'
        }
    ],
    'Betel': [
        {
            'scientific_name': 'Piper betle',
            'scientific_medicinal_properties': 'Piper betle, commonly known as betel vine or betel leaf, is a perennial creeper native to South and Southeast Asia.',
            'common_location': 'Betel vines are cultivated in tropical and subtropical regions for their leaves, which are used in religious, cultural, and medicinal practices.',
            'popular_usecase': 'Betel leaves are used in traditional medicine for their antiseptic, anti-inflammatory, and digestive properties. They are chewed with betel nut and other ingredients in betel quids for their stimulant and euphoric effects. Betel leaves are also used in Ayurvedic formulations and as a mouth freshener.',
            'Disclaimer': 'Chewing betel quids can have adverse health effects, including oral cancer, gum disease, and addiction. Consult a healthcare professional before using betel leaves for medicinal purposes.',
            'lament_medicinal_property': 'Betel leaves are valued for their aromatic flavor and medicinal properties. They are used to freshen breath, aid digestion, and promote oral health.'
        }
    ],
    'Betel_Nut': [
        {
            'scientific_name': 'Areca catechu',
            'scientific_medicinal_properties': 'Areca catechu, commonly known as betel nut or areca nut, is the seed of the areca palm tree native to South and Southeast Asia.',
            'common_location': 'Areca palm trees are cultivated in tropical and subtropical regions for their nuts, which are used in cultural, religious, and medicinal practices.',
            'popular_usecase': 'Betel nuts are chewed with betel leaves and other ingredients in betel quids for their stimulant and psychoactive effects. They are also used in traditional medicine for their digestive, carminative, and aphrodisiac properties. In some cultures, betel nuts are consumed as a social and ceremonial tradition.',
            'Disclaimer': 'Chewing betel quids can have adverse health effects, including oral cancer, gum disease, and addiction. Consult a healthcare professional before using betel nuts for medicinal purposes.',
            'lament_medicinal_property': 'Betel nuts are valued for their stimulating effects on the nervous system. They are used to enhance alertness, improve digestion, and promote feelings of well-being.'
        }
    ],
    'Brahmi': [
        {
            'scientific_name': 'Bacopa monnieri',
            'scientific_medicinal_properties': 'Bacopa monnieri, commonly known as brahmi or water hyssop, is a perennial herb native to wetlands and marshy areas of India, Southeast Asia, and Australia.',
            'common_location': 'Bacopa monnieri grows in aquatic and semi-aquatic habitats such as ponds, rivers, and marshes. It is cultivated in gardens and farms for its medicinal properties.',
            'popular_usecase': 'Brahmi is used in Ayurvedic medicine for its cognitive-enhancing, adaptogenic, and neuroprotective properties. It is believed to improve memory, concentration, and learning ability. Brahmi is also used to reduce stress, anxiety, and symptoms of depression.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using brahmi, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Brahmi is valued for its ability to support brain health and cognitive function. It is used to enhance memory, mental clarity, and overall mental well-being.'
        }
    ],
    'Castor': [
        {
            'scientific_name': 'Ricinus communis',
            'scientific_medicinal_properties': 'Ricinus communis, commonly known as castor bean or castor oil plant, is a fast-growing perennial shrub native to the Mediterranean region, Eastern Africa, and India.',
            'common_location': 'Castor plants grow in tropical and subtropical regions worldwide, where they are cultivated for their seeds, which contain castor oil.',
            'popular_usecase': 'Castor oil is used in various applications, including pharmaceuticals, cosmetics, lubricants, and biodiesel production. It is known for its purgative, emollient, and anti-inflammatory properties. Castor oil is used topically for skin conditions, hair care, and massage, as well as orally for constipation relief and detoxification.',
            'Disclaimer': 'Castor beans contain toxic compounds, including ricin, which can be harmful if ingested or applied improperly. Consult a healthcare professional before using castor oil or castor beans for medicinal or other purposes.',
            'lament_medicinal_property': 'Castor oil is valued for its moisturizing and healing properties. It is used to soothe dry skin, promote hair growth, and relieve constipation.'
        }
    ],
    'Curry_Leaf': [
        {
            'scientific_name': 'Murraya koenigii',
            'scientific_medicinal_properties': 'Murraya koenigii, commonly known as curry leaf or sweet neem, is a tropical tree native to India and Sri Lanka.',
            'common_location': 'Curry leaf trees are cultivated in tropical and subtropical regions for their aromatic leaves, which are used as a culinary herb in Indian cuisine.',
            'popular_usecase': 'Curry leaves are used in Indian cooking to add flavor and aroma to dishes such as curries, rice, and soups. They are also used in traditional medicine for their digestive, carminative, and antioxidant properties. Curry leaves are believed to aid digestion, reduce cholesterol levels, and promote hair growth.',
            'Disclaimer': 'Consult a healthcare professional before using curry leaves, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Curry leaves are valued for their aromatic flavor and health benefits. They are used to improve digestion, lower cholesterol, and support hair and scalp health.'
        }
    ],
    'Doddapatre': [
        {
            'scientific_name': 'Plectranthus amboinicus',
            'scientific_medicinal_properties': 'Plectranthus amboinicus, commonly known as Cuban oregano, Indian borage, or doddapatre, is a perennial herb native to Southern and Eastern Africa, Madagascar, and the Indian subcontinent.',
            'common_location': 'Plectranthus amboinicus grows in tropical and subtropical regions worldwide and is cultivated for its culinary and medicinal uses.',
            'popular_usecase': 'Doddapatre leaves are used in culinary dishes, herbal teas, and traditional medicine for their aromatic flavor and medicinal properties. They are believed to have antibacterial, antifungal, anti-inflammatory, and antioxidant effects. Doddapatre leaves are used to treat respiratory conditions, digestive disorders, skin problems, and fever.',
            'Disclaimer': 'Consult a healthcare professional before using doddapatre, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Doddapatre leaves are valued for their aromatic flavor and health-promoting properties. They are used to relieve coughs, colds, indigestion, and skin irritations.'
        }
    ],
    'Ekka': [
        {
            'scientific_name': 'Azadirachta indica',
            'scientific_medicinal_properties': 'Azadirachta indica, commonly known as neem or Indian lilac, is a fast-growing evergreen tree native to the Indian subcontinent.',
            'common_location': 'Neem trees are found in tropical and subtropical regions of South Asia, including India, Nepal, Pakistan, Bangladesh, and Sri Lanka.',
            'popular_usecase': 'Neem is used in Ayurvedic medicine for its antiseptic, antibacterial, antiviral, antifungal, and anti-inflammatory properties. It is used to treat various skin conditions such as acne, eczema, psoriasis, and fungal infections. Neem is also used in dental care products, herbal remedies, and organic agriculture.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using neem, especially if you have any skin allergies or medical conditions.',
            'lament_medicinal_property': 'Neem is valued for its broad-spectrum antimicrobial and anti-inflammatory effects. It is used to cleanse and purify the skin, promote wound healing, and support overall skin health.'
        }
    ],
    'Ganike': [
        {
            'scientific_name': 'Solanum nigrum',
            'scientific_medicinal_properties': 'Solanum nigrum, commonly known as black nightshade or makoi, is a flowering plant native to Eurasia and North Africa.',
            'common_location': 'Black nightshade grows as a weed in cultivated fields, gardens, and waste areas. It is found in temperate, subtropical, and tropical regions worldwide.',
            'popular_usecase': 'In traditional medicine, black nightshade is used for its diuretic, anti-inflammatory, and antipyretic properties. It is used to treat various health conditions such as fever, cough, asthma, rheumatism, skin diseases, and digestive disorders. Black nightshade leaves and berries are also used as a culinary vegetable in some cuisines, although caution is advised due to potential toxicity.',
            'Disclaimer': 'Consult a qualified healthcare professional before using black nightshade, especially if you are pregnant, breastfeeding, or have any medical conditions.',
            'lament_medicinal_property': 'Black nightshade is valued for its medicinal properties, but caution is advised due to potential toxicity. It is used to reduce fever, relieve pain, and treat various health conditions, but its use should be supervised by a healthcare professional.'
        }
    ],
    'Gauva': [
        {
            'scientific_name': 'Psidium guajava',
            'scientific_medicinal_properties': 'Psidium guajava, commonly known as guava, is a tropical fruit tree native to Central America and the Caribbean.',
            'common_location': 'Guava trees are cultivated in tropical and subtropical regions worldwide for their edible fruits, which are rich in vitamins, minerals, and antioxidants.',
            'popular_usecase': 'Guava fruit is consumed fresh or processed into juice, jams, jellies, and other food products. It is known for its high vitamin C content, which supports immune health and collagen production. Guava leaves are used in traditional medicine for their antidiarrheal, antimicrobial, and antiparasitic properties. Guava leaf tea is consumed for its digestive and detoxifying effects.',
            'Disclaimer': 'Consult a healthcare professional before using guava, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Guava fruit and leaves are valued for their nutritional content and health benefits. They are used to support immune health, aid digestion, and promote overall well-being.'
        }
    ],
    'Geranium': [
        {
            'scientific_name': 'Pelargonium graveolens',
            'scientific_medicinal_properties': 'Pelargonium graveolens, commonly known as geranium or rose geranium, is a perennial shrub native to South Africa.',
            'common_location': 'Geranium plants are cultivated worldwide for their fragrant leaves and flowers, which are used in perfumery, aromatherapy, and traditional medicine.',
            'popular_usecase': 'Geranium essential oil is used in aromatherapy for its calming, uplifting, and balancing effects on the mind and body. It is believed to relieve stress, anxiety, depression, and insomnia. Geranium oil is also used in skincare products for its astringent, antiseptic, and anti-inflammatory properties. It is used to balance oily and combination skin, reduce acne and inflammation, and promote wound healing.',
            'Disclaimer': 'Consult a qualified aromatherapist or healthcare professional before using geranium essential oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Geranium essential oil is valued for its calming and skin-soothing properties. It is used to reduce stress, balance emotions, and promote clear, healthy skin.'
        }
    ],
    'Henna': [
        {
            'scientific_name': 'Lawsonia inermis',
            'scientific_medicinal_properties': 'Lawsonia inermis, commonly known as henna, is a flowering plant native to North Africa, West Asia, and South Asia.',
            'common_location': 'Henna plants are cultivated in arid and semi-arid regions for their leaves, which are dried and ground into a fine powder. Henna powder is used to dye hair, skin, and nails in various cultures.',
            'popular_usecase': 'Henna is used in traditional medicine and cosmetics for its cooling, astringent, and antimicrobial properties. It is used topically to soothe skin irritation, treat burns, and condition hair. Henna is also used as a natural dye for body art, temporary tattoos, and hair coloring.',
            'Disclaimer': 'Consult a qualified healthcare professional before using henna, especially if you have any skin allergies or medical conditions.',
            'lament_medicinal_property': 'Henna is valued for its natural coloring and conditioning properties. It is used to enhance hair color, nourish the scalp, and promote healthy skin.'
        }
    ],
    'Hibiscus': [
        {
            'scientific_name': 'Hibiscus rosa-sinensis',
            'scientific_medicinal_properties': 'Hibiscus rosa-sinensis, commonly known as hibiscus or Chinese hibiscus, is a flowering plant native to East Asia.',
            'common_location': 'Hibiscus plants are cultivated worldwide for their ornamental flowers, which are used in landscaping, gardens, and horticulture. They are also grown for their medicinal and culinary uses.',
            'popular_usecase': 'Hibiscus flowers are used in traditional medicine and herbal teas for their health benefits. Hibiscus tea is rich in antioxidants, vitamins, and minerals. It is believed to lower blood pressure, reduce cholesterol levels, promote weight loss, and improve liver health. Hibiscus flowers are also used in hair and skincare products for their moisturizing, anti-aging, and anti-inflammatory properties.',
            'Disclaimer': 'Consult a healthcare professional before using hibiscus, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Hibiscus tea is valued for its refreshing taste and health-promoting properties. It is used to support cardiovascular health, promote hydration, and enhance skin and hair health.'
        }
    ],
    'Honge': [
        {
            'scientific_name': 'Pongamia pinnata',
            'scientific_medicinal_properties': 'Pongamia pinnata, commonly known as honge or Indian beech, is a fast-growing tree native to South Asia, Southeast Asia, and northern Australia.',
            'common_location': 'Honge trees grow in tropical and subtropical regions, where they are cultivated for their seeds, which contain bioactive compounds with medicinal properties.',
            'popular_usecase': 'Honge oil, also known as pongamia oil, is extracted from the seeds of the honge tree and used in traditional medicine, cosmetics, and biofuels. It is used topically for its antimicrobial, anti-inflammatory, and wound-healing properties. Honge oil is also used as a natural insect repellent, fertilizer, and lubricant.',
            'Disclaimer': 'Consult a qualified healthcare professional before using honge oil, especially if you have any skin allergies or medical conditions.',
            'lament_medicinal_property': 'Honge oil is valued for its therapeutic properties and versatility. It is used to soothe skin irritation, promote wound healing, and protect against insect bites and infections.'
        }
    ],
    'Insulin': [
        {
            'scientific_name': 'Syzygium cumini',
            'scientific_medicinal_properties': 'Syzygium cumini, commonly known as jamun or Indian blackberry, is a tropical evergreen tree native to India, Bangladesh, Nepal, Pakistan, and Indonesia.',
            'common_location': 'Jamun trees are found in tropical and subtropical regions, where they are cultivated for their edible fruits, seeds, and leaves, which have medicinal properties.',
            'popular_usecase': 'Jamun fruits are consumed fresh or processed into juice, jams, jellies, and culinary dishes. They are known for their sweet and tangy flavor, as well as their nutritional value. Jamun seeds and leaves are used in traditional medicine for their antidiabetic, antihyperlipidemic, and antioxidant properties. Jamun is believed to regulate blood sugar levels, improve insulin sensitivity, and prevent complications of diabetes.',
            'Disclaimer': 'Consult a healthcare professional before using jamun, especially if you have diabetes or are taking medications.',
            'lament_medicinal_property': 'Jamun is valued for its antidiabetic properties and is used to support blood sugar control and metabolic health.'
        }
    ],
    'Jasmine': [
        {
            'scientific_name': 'Jasminum officinale',
            'scientific_medicinal_properties': 'Jasminum officinale, commonly known as jasmine or common jasmine, is a flowering plant native to South Asia, Southeast Asia, and East Asia.',
            'common_location': 'Jasmine plants are cultivated worldwide for their fragrant flowers, which are used in perfumery, aromatherapy, and traditional medicine.',
            'popular_usecase': 'Jasmine essential oil is used in aromatherapy for its uplifting, calming, and aphrodisiac effects. It is believed to relieve stress, anxiety, depression, and insomnia. Jasmine oil is also used in skincare products for its moisturizing, soothing, and rejuvenating properties. It is used to hydrate dry skin, reduce inflammation, and promote a radiant complexion.',
            'Disclaimer': 'Consult a qualified aromatherapist or healthcare professional before using jasmine essential oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Jasmine essential oil is valued for its sensual aroma and skin-nourishing properties. It is used to uplift the mood, promote relaxation, and enhance skin health.'
        }
    ],
    'Lemon': [
        {
            'scientific_name': 'Citrus limon',
            'scientific_medicinal_properties': 'Citrus limon, commonly known as lemon, is a citrus fruit tree native to South Asia.',
            'common_location': 'Lemon trees are cultivated in subtropical and tropical regions worldwide for their acidic fruits, which are used in culinary, medicinal, and cosmetic applications.',
            'popular_usecase': 'Lemon juice is used as a flavoring agent in cooking, baking, beverages, and condiments. It is also used in household cleaning products and natural remedies for its antiseptic, antibacterial, and deodorizing properties. Lemon essential oil is used in aromatherapy for its invigorating, uplifting, and cleansing effects. It is believed to improve mood, boost energy, and support immune health.',
            'Disclaimer': 'Consult a healthcare professional before using lemon, especially if you have any citrus allergies or medical conditions.',
            'lament_medicinal_property': 'Lemon is valued for its refreshing flavor and versatile uses. It is used to cleanse, purify, and revitalize the body and mind.'
        }
    ],
    'Lemon_grass': [
        {
            'scientific_name': 'Cymbopogon citratus',
            'scientific_medicinal_properties': 'Cymbopogon citratus, commonly known as lemongrass, is a tropical grass native to South Asia and Southeast Asia.',
            'common_location': 'Lemongrass grows in warm, humid climates and is cultivated in tropical and subtropical regions worldwide for its culinary, medicinal, and aromatic properties.',
            'popular_usecase': 'Lemongrass is used in culinary dishes, herbal teas, and essential oils for its lemony flavor and fragrance. It is also used in traditional medicine for its antimicrobial, anti-inflammatory, and digestive properties. Lemongrass tea is consumed for its calming, detoxifying, and digestive benefits. Lemongrass essential oil is used in aromatherapy for its refreshing, energizing, and insect-repellent effects.',
            'Disclaimer': 'Consult a qualified healthcare professional before using lemongrass, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Lemongrass is valued for its citrusy aroma and health-promoting properties. It is used to soothe digestive discomfort, relieve stress, and repel insects.'
        }
    ],
    'Mango': [
        {
            'scientific_name': 'Mangifera indica',
            'scientific_medicinal_properties': 'Mangifera indica, commonly known as mango, is a tropical fruit tree native to South Asia.',
            'common_location': 'Mango trees are cultivated in subtropical and tropical regions worldwide for their sweet and juicy fruits, which are consumed fresh or processed into juice, jams, jellies, and culinary dishes.',
            'popular_usecase': 'Mango fruit is known for its delicious flavor, vibrant color, and nutritional value. It is rich in vitamins, minerals, and antioxidants, including vitamins A and C, potassium, and beta-carotene. Mangoes are used in culinary dishes, desserts, smoothies, and beverages. They are also used in traditional medicine for their anti-inflammatory, antioxidant, and immune-boosting properties. Mango leaves, bark, and seeds are used in herbal remedies for various health conditions such as diarrhea, dysentery, and diabetes.',
            'Disclaimer': 'Consult a healthcare professional before using mango, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Mango is valued for its delicious taste and health benefits. It is used to support immune health, promote digestion, and enhance overall well-being.'
        }
    ],
    'Mint': [
        {
            'scientific_name': 'Mentha',
            'scientific_medicinal_properties': 'Mentha is a genus of aromatic perennial herbs in the Lamiaceae family, which includes species such as spearmint (Mentha spicata) and peppermint (Mentha × piperita).',
            'common_location': 'Mint plants grow in temperate and subtropical regions worldwide, where they are cultivated for their aromatic leaves, which are used in culinary, medicinal, and cosmetic applications.',
            'popular_usecase': 'Mint leaves are used in culinary dishes, herbal teas, and essential oils for their refreshing flavor and fragrance. Peppermint oil is used in aromatherapy for its invigorating, cooling, and digestive properties. It is believed to relieve headaches, nausea, indigestion, and respiratory congestion. Peppermint tea is consumed for its digestive, calming, and decongestant effects. Mint leaves are also used in herbal remedies for digestive disorders, respiratory ailments, and headaches.',
            'Disclaimer': 'Consult a qualified healthcare professional before using mint, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Mint is valued for its refreshing taste and cooling properties. It is used to soothe digestive discomfort, alleviate respiratory congestion, and promote relaxation.'
        }
    ],
    'Nagadali': [
        {
            'scientific_name': 'Sesbania grandiflora',
            'scientific_medicinal_properties': 'Sesbania grandiflora, commonly known as sesban or agati, is a fast-growing perennial tree native to South Asia and Southeast Asia.',
            'common_location': 'Sesbania grandiflora grows in tropical and subtropical regions, where it is cultivated for its edible flowers, leaves, and pods, which have medicinal properties.',
            'popular_usecase': 'Sesbania flowers, leaves, and pods are used in culinary dishes, herbal teas, and traditional medicine for their nutritional and medicinal benefits. They are rich in vitamins, minerals, and antioxidants, including vitamins A, C, and E, calcium, and iron. Sesbania is used to promote overall health, boost immunity, and treat various health conditions such as anemia, diabetes, inflammation, and respiratory disorders.',
            'Disclaimer': 'Consult a healthcare professional before using sesbania, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Sesbania is valued for its nutritious flowers, leaves, and pods. It is used to support immune health, enhance energy levels, and promote overall well-being.'
        }
    ],
    'Neem': [
        {
            'scientific_name': 'Azadirachta indica',
            'scientific_medicinal_properties': 'Azadirachta indica, commonly known as neem or Indian lilac, is a fast-growing evergreen tree native to the Indian subcontinent.',
            'common_location': 'Neem trees are found in tropical and subtropical regions of South Asia, including India, Nepal, Pakistan, Bangladesh, and Sri Lanka.',
            'popular_usecase': 'Neem is used in Ayurvedic medicine for its antiseptic, antibacterial, antiviral, antifungal, and anti-inflammatory properties. It is used to treat various skin conditions such as acne, eczema, psoriasis, and fungal infections. Neem is also used in dental care products, herbal remedies, and organic agriculture.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using neem, especially if you have any skin allergies or medical conditions.',
            'lament_medicinal_property': 'Neem is valued for its broad-spectrum antimicrobial and anti-inflammatory effects. It is used to cleanse and purify the skin, promote wound healing, and support overall skin health.'
        }
    ],
    'Nithyapushpa': [
        {
            'scientific_name': 'Vinca rosea',
            'scientific_medicinal_properties': 'Vinca rosea, commonly known as periwinkle or Madagascar periwinkle, is a flowering plant native to Madagascar and other Indian Ocean islands.',
            'common_location': 'Periwinkle plants are cultivated worldwide for their ornamental flowers, which are used in landscaping, gardens, and floral arrangements. They are also grown for their medicinal properties.',
            'popular_usecase': 'Periwinkle has been used in traditional medicine for centuries for its antidiabetic, anticancer, antimicrobial, and antihypertensive properties. It is used to treat various health conditions such as diabetes, cancer, infections, and high blood pressure. Periwinkle alkaloids, such as vincristine and vinblastine, are used in chemotherapy drugs to treat leukemia, lymphoma, and other cancers.',
            'Disclaimer': 'Consult a qualified healthcare professional before using periwinkle, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Periwinkle is valued for its medicinal properties and is used to treat a wide range of health conditions. It is known for its antidiabetic, anticancer, and antimicrobial effects.'
        }
    ],
    'Pomegranate': [
        {
            'scientific_name': 'Punica granatum',
            'scientific_medicinal_properties': 'Punica granatum, commonly known as pomegranate, is a fruit-bearing shrub or small tree native to the region from Iran to northern India.',
            'common_location': 'Pomegranate trees are cultivated in subtropical and tropical regions worldwide for their edible fruits, which are prized for their sweet and tangy flavor, as well as their nutritional value.',
            'popular_usecase': 'Pomegranate fruit is consumed fresh or processed into juice, jams, jellies, and culinary dishes. It is known for its high antioxidant content, including punicalagins, anthocyanins, and vitamin C. Pomegranate juice is believed to promote heart health, lower blood pressure, reduce inflammation, and improve cognitive function. Pomegranate seeds and peel are used in traditional medicine for their antidiabetic, anti-inflammatory, and antimicrobial properties. Pomegranate extracts are used in skincare products for their moisturizing, anti-aging, and antioxidant effects.',
            'Disclaimer': 'Consult a healthcare professional before using pomegranate, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Pomegranate is valued for its delicious taste and health benefits. It is used to support heart health, enhance cognitive function, and promote overall well-being.'
        }
    ],
    'Rosemary': [
        {
            'scientific_name': 'Rosmarinus officinalis',
            'scientific_medicinal_properties': 'Rosmarinus officinalis, commonly known as rosemary, is a woody, perennial herb native to the Mediterranean region.',
            'common_location': 'Rosemary plants are cultivated worldwide for their aromatic leaves, which are used in culinary, medicinal, and cosmetic applications.',
            'popular_usecase': 'Rosemary leaves are used as a culinary herb to flavor roasted meats, poultry, fish, vegetables, and bread. Rosemary essential oil is used in aromatherapy for its stimulating, invigorating, and memory-enhancing effects. It is believed to improve concentration, reduce stress, and boost mood. Rosemary oil is also used in skincare and hair care products for its antimicrobial, antioxidant, and anti-inflammatory properties. It is used to cleanse and tone the skin, promote hair growth, and relieve scalp irritation.',
            'Disclaimer': 'Consult a qualified aromatherapist or healthcare professional before using rosemary essential oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Rosemary is valued for its culinary and therapeutic properties. It is used to flavor food, improve memory, and promote skin and hair health.'
        }
    ],
    'Sandalwood': [
        {
            'scientific_name': 'Santalum album',
            'scientific_medicinal_properties': 'Santalum album, commonly known as sandalwood, is a tropical evergreen tree native to South Asia, Southeast Asia, and Australia.',
            'common_location': 'Sandalwood trees are cultivated in tropical and subtropical regions worldwide for their fragrant heartwood, which is used in perfumery, incense, cosmetics, and traditional medicine.',
            'popular_usecase': 'Sandalwood essential oil is used in aromatherapy for its calming, grounding, and mood-enhancing effects. It is believed to reduce anxiety, promote relaxation, and enhance meditation. Sandalwood oil is also used in skincare products for its moisturizing, anti-inflammatory, and anti-aging properties. It is used to soothe dry skin, reduce inflammation, and minimize the appearance of scars and blemishes.',
            'Disclaimer': 'Consult a qualified aromatherapist or healthcare professional before using sandalwood essential oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Sandalwood is valued for its aromatic fragrance and therapeutic properties. It is used to calm the mind, promote relaxation, and nourish the skin.'
        }
    ],
    'Sarpagandha': [
        {
            'scientific_name': 'Rauwolfia serpentina',
            'scientific_medicinal_properties': 'Rauwolfia serpentina, commonly known as Indian snakeroot or sarpagandha, is a perennial shrub native to South Asia.',
            'common_location': 'Rauwolfia serpentina grows in subtropical and tropical regions, where it is cultivated for its medicinal properties.',
            'popular_usecase': 'Sarpagandha is used in traditional medicine for its antihypertensive, sedative, and antipsychotic properties. It contains alkaloids such as reserpine, which are used in pharmaceutical drugs to treat high blood pressure, anxiety, and mental disorders. Sarpagandha is also used in Ayurvedic medicine for its calming, anti-stress, and sleep-inducing effects.',
            'Disclaimer': 'Consult a qualified healthcare professional before using sarpagandha, especially if you have any medical conditions or are taking medications.',
            'lament_medicinal_property': 'Sarpagandha is valued for its therapeutic effects on the nervous system. It is used to reduce blood pressure, relieve anxiety, and promote relaxation and sleep.'
        }
    ],
    'Sesame': [
        {
            'scientific_name': 'Sesamum indicum',
            'scientific_medicinal_properties': 'Sesamum indicum, commonly known as sesame, is an annual flowering plant native to Africa and India.',
            'common_location': 'Sesame plants are cultivated in tropical and subtropical regions worldwide for their seeds, which are used as a culinary ingredient, cooking oil, and condiment.',
            'popular_usecase': 'Sesame seeds are rich in healthy fats, protein, vitamins, minerals, and antioxidants. They are used in culinary dishes, bakery products, sweets, and snacks. Sesame oil is used in cooking, frying, and salad dressings. Sesame seed extract, known as sesame oil cake, is used as a livestock feed and organic fertilizer. Sesame seeds are also used in traditional medicine for their anti-inflammatory, antioxidant, and immune-boosting properties. Sesame oil is used topically for skin and hair care, massage, and Ayurvedic treatments.',
            'Disclaimer': 'Consult a healthcare professional before using sesame seeds or sesame oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Sesame seeds and oil are valued for their nutritional content and health benefits. They are used to support heart health, improve digestion, and nourish the skin and hair.'
        }
    ],
    'Sunflower': [
        {
            'scientific_name': 'Helianthus annuus',
            'scientific_medicinal_properties': 'Helianthus annuus, commonly known as sunflower, is an annual flowering plant native to North and South America.',
            'common_location': 'Sunflowers are cultivated worldwide for their edible seeds and oil, as well as their ornamental value.',
            'popular_usecase': 'Sunflower seeds are consumed as a snack and used as an ingredient in bakery products, salads, and snacks. Sunflower oil is used in cooking, frying, and salad dressings. Sunflower seed meal is used as a livestock feed and organic fertilizer. Sunflower petals are used in herbal teas and traditional medicine for their diuretic, expectorant, and anti-inflammatory properties. Sunflower oil is also used topically for skincare and massage.',
            'Disclaimer': 'Consult a healthcare professional before using sunflower seeds or sunflower oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Sunflower seeds and oil are valued for their nutritional content and health benefits. They are used to support heart health, improve skin health, and promote overall well-being.'
        }
    ],
    'Tulsi': [
        {
            'scientific_name': 'Ocimum tenuiflorum',
            'scientific_medicinal_properties': 'Ocimum tenuiflorum, commonly known as holy basil or tulsi, is a sacred plant in Hinduism and Ayurveda. It is native to the Indian subcontinent.',
            'common_location': 'Tulsi is cultivated in home gardens, temples, and farms throughout India and Southeast Asia for its medicinal and religious significance.',
            'popular_usecase': 'Tulsi is used in Ayurvedic medicine for its adaptogenic, immunomodulatory, and antimicrobial properties. It is considered a rasayana herb, which promotes longevity, vitality, and overall well-being. Tulsi is used to reduce stress, support respiratory health, improve digestion, and enhance cognitive function. It is also used in religious rituals, prayers, and ceremonies as an offering to the gods and goddesses.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using tulsi, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Tulsi is valued for its sacred status and health-promoting properties. It is used to reduce stress, boost immunity, and promote overall wellness.'
        }
    ],
    'Nooni': [
        {
            'scientific_name': 'Mimusops elengi',
            'scientific_medicinal_properties': 'Mimusops elengi, commonly known as nooni, is a medium-sized evergreen tree native to South Asia and Southeast Asia.',
            'common_location': 'Nooni trees are found in tropical and subtropical regions, where they are cultivated for their fragrant flowers, which are used in traditional medicine, perfumery, and religious ceremonies.',
            'popular_usecase': 'Nooni flowers are used in Ayurvedic medicine for their astringent, antibacterial, and anti-inflammatory properties. They are used to treat oral health issues such as toothache, gum disease, and bad breath. Nooni flowers are also used in skincare products for their soothing, moisturizing, and anti-aging effects. They are used to tone the skin, reduce inflammation, and promote healing. Nooni bark and leaves are used in traditional medicine for their antidiabetic, analgesic, and antimicrobial properties.',
            'Disclaimer': 'Consult a qualified healthcare professional before using nooni flowers, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Nooni flowers are valued for their aromatic fragrance and therapeutic properties. They are used to promote oral health, skin health, and overall well-being.'
        }
    ],
    'Pappaya': [
        {
            'scientific_name': 'Carica papaya',
            'scientific_medicinal_properties': 'Carica papaya, commonly known as papaya, is a tropical fruit tree native to the Americas, particularly southern Mexico and Central America.',
            'common_location': 'Papaya trees are cultivated in tropical and subtropical regions worldwide for their edible fruits, which are prized for their sweet taste, vibrant color, and nutritional value.',
            'popular_usecase': 'Papaya fruit is consumed fresh or processed into juice, jams, jellies, and culinary dishes. It is rich in vitamins, minerals, antioxidants, and enzymes such as papain and chymopapain. Papaya is known for its digestive, anti-inflammatory, and immune-boosting properties. It is used to promote digestion, relieve constipation, and support gastrointestinal health. Papaya seeds are also used in traditional medicine for their antimicrobial, antiparasitic, and anthelmintic properties. They are used to treat intestinal worms, fungal infections, and bacterial infections.',
            'Disclaimer': 'Consult a healthcare professional before using papaya, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Papaya is valued for its delicious taste and health benefits. It is used to support digestion, boost immunity, and promote overall well-being.'
        }
    ],
    'Pepper': [
        {
            'scientific_name': 'Piper nigrum',
            'scientific_medicinal_properties': 'Piper nigrum, commonly known as pepper, is a flowering vine in the family Piperaceae, cultivated for its fruit, known as a peppercorn.',
            'common_location': 'Pepper plants are native to South Asia and are cultivated in tropical regions worldwide for their fruits, which are used as a spice and seasoning.',
            'popular_usecase': 'Pepper is one of the most commonly used spices in culinary dishes worldwide. It is known for its pungent flavor and aroma, as well as its medicinal properties. Pepper contains bioactive compounds such as piperine, which have antioxidant, anti-inflammatory, and digestive properties. Pepper is used to improve digestion, stimulate appetite, and relieve gastrointestinal discomfort. It is also used in traditional medicine for its analgesic, expectorant, and antimicrobial effects. Pepper oil is used topically for its warming, analgesic, and anti-inflammatory properties. It is used to relieve muscle pain, joint pain, and arthritis symptoms.',
            'Disclaimer': 'Consult a healthcare professional before using pepper, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Pepper is valued for its spicy flavor and therapeutic properties. It is used to support digestion, relieve pain, and promote overall well-being.'
        }
    ],
    'Raktachandini': [
        {
            'scientific_name': 'Hibiscus rosa-sinensis',
            'scientific_medicinal_properties': 'Hibiscus rosa-sinensis, commonly known as hibiscus or raktachandini, is a flowering plant native to East Asia.',
            'common_location': 'Hibiscus plants are cultivated worldwide for their ornamental flowers, which are used in landscaping, gardens, and floral arrangements.',
            'popular_usecase': 'Hibiscus flowers are used in herbal teas, beverages, and culinary dishes for their tart flavor and vibrant color. Hibiscus tea is known for its refreshing taste and health benefits. It is rich in antioxidants, vitamins, and minerals, and is believed to support heart health, lower blood pressure, and improve cholesterol levels. Hibiscus flowers are also used in traditional medicine for their diuretic, antimicrobial, and anti-inflammatory properties. They are used to promote urinary tract health, relieve menstrual cramps, and soothe sore throat.',
            'Disclaimer': 'Consult a healthcare professional before using hibiscus, especially if you are pregnant, breastfeeding, or have any medical conditions.',
            'lament_medicinal_property': 'Raktachandini is valued for its beautiful flowers and health-promoting properties. It is used to support heart health, promote urinary tract health, and enhance overall well-being.'
        }
    ],
    'Rose': [
        {
            'scientific_name': 'Rosa',
            'scientific_medicinal_properties': 'Rosa is a genus of flowering plants in the family Rosaceae, commonly known as roses. There are over three hundred species and thousands of cultivars.',
            'common_location': 'Roses are cultivated worldwide for their ornamental flowers, which are used in gardens, landscaping, and floral arrangements. They are also grown for their fragrant petals, which are used in perfumery, cosmetics, and culinary applications.',
            'popular_usecase': 'Rose petals are used in herbal teas, culinary dishes, and skincare products for their delicate fragrance and flavor. Rose water is used as a culinary ingredient and flavoring agent, as well as a skincare tonic and perfume. Rose essential oil is used in aromatherapy for its calming, uplifting, and mood-enhancing effects. It is believed to reduce stress, anxiety, and depression, as well as promote relaxation and sleep. Rose oil is also used in skincare products for its moisturizing, anti-inflammatory, and anti-aging properties. It is used to hydrate the skin, reduce redness, and minimize the appearance of wrinkles and fine lines.',
            'Disclaimer': 'Consult a qualified aromatherapist or healthcare professional before using rose essential oil, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Rose is valued for its beauty, fragrance, and therapeutic properties. It is used to promote relaxation, uplift the mood, and enhance skin health.'
        }
    ],
    'Sapota': [
        {
            'scientific_name': 'Manilkara zapota',
            'scientific_medicinal_properties': 'Manilkara zapota, commonly known as sapota or chikoo, is a tropical fruit tree native to Mexico and Central America.',
            'common_location': 'Sapota trees are cultivated in tropical and subtropical regions worldwide for their edible fruits, which are prized for their sweet taste and creamy texture.',
            'popular_usecase': 'Sapota fruit is consumed fresh or processed into juice, jams, jellies, and culinary dishes. It is rich in vitamins, minerals, antioxidants, and dietary fiber. Sapota is known for its digestive, anti-inflammatory, and immune-boosting properties. It is used to promote digestion, relieve constipation, and support gastrointestinal health. Sapota seeds are also used in traditional medicine for their antimicrobial, antiparasitic, and anthelmintic properties. They are used to treat intestinal worms, fungal infections, and bacterial infections.',
            'Disclaimer': 'Consult a healthcare professional before using sapota, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Sapota is valued for its delicious taste and health benefits. It is used to support digestion, boost immunity, and promote overall well-being.'
        }
    ],
    'Tulasi': [
        {
            'scientific_name': 'Ocimum tenuiflorum',
            'scientific_medicinal_properties': 'Ocimum tenuiflorum, commonly known as holy basil or tulsi, is a sacred plant in Hinduism and Ayurveda. It is native to the Indian subcontinent.',
            'common_location': 'Tulsi is cultivated in home gardens, temples, and farms throughout India and Southeast Asia for its medicinal and religious significance.',
            'popular_usecase': 'Tulsi is used in Ayurvedic medicine for its adaptogenic, immunomodulatory, and antimicrobial properties. It is considered a rasayana herb, which promotes longevity, vitality, and overall well-being. Tulsi is used to reduce stress, support respiratory health, improve digestion, and enhance cognitive function. It is also used in religious rituals, prayers, and ceremonies as an offering to the gods and goddesses.',
            'Disclaimer': 'Consult a qualified Ayurvedic practitioner before using tulsi, especially if you have any medical conditions or are pregnant.',
            'lament_medicinal_property': 'Tulsi is valued for its sacred status and health-promoting properties. It is used to reduce stress, boost immunity, and promote overall wellness.'
        }
    ],
    'Wood_sorel': [
        {
            'scientific_name': 'Oxalis',
            'scientific_medicinal_properties': 'Oxalis is a genus of flowering plants in the family Oxalidaceae, commonly known as wood sorrel. There are over eight hundred species distributed worldwide.',
            'common_location': 'Wood sorrel plants are found in a variety of habitats, including woodlands, meadows, and gardens. They are native to temperate and subtropical regions of the Northern Hemisphere.',
            'popular_usecase': 'Wood sorrel leaves are edible and have a tangy, citrus-like flavor. They are used fresh in salads, soups, and sauces, or cooked as a potherb. Wood sorrel is rich in vitamin C, antioxidants, and dietary fiber. It is known for its diuretic, anti-inflammatory, and antimicrobial properties. Wood sorrel tea is used in traditional medicine for its cooling and detoxifying effects. It is used to promote urinary tract health, reduce inflammation, and support digestion. Wood sorrel leaves are also used topically for their astringent and soothing properties. They are applied to insect bites, rashes, and minor skin irritations to relieve itching and inflammation.',
            'Disclaimer': 'Consult a qualified healthcare professional before using wood sorrel, especially if you have any allergies or medical conditions.',
            'lament_medicinal_property': 'Wood sorrel is valued for its tangy flavor and medicinal properties. It is used to promote urinary tract health, reduce inflammation, and support overall well-being.'
        }
    ],
}
"""




Plant_Details = {
    'Aloevera': {
        'scientificName': 'Aloe vera',
        'medicinalProperty': 'Aloe vera is known for its medicinal properties. It contains various bioactive compounds, such as vitamins, minerals, enzymes, and amino acids, that contribute to its therapeutic effects. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Soothing burns and promoting wound healing: Aloe vera gel has cooling and anti-inflammatory properties, which can help soothe sunburns, minor burns, and cuts. It also supports the skin\'s natural healing process.',
            'Moisturizing and hydrating skin: Aloe vera gel is a popular moisturizer due to its ability to hydrate and soften the skin. It is often used to treat dry or irritated skin conditions.',
            'Reducing inflammation: Aloe vera contains compounds like acemannan and salicylic acid, which have anti-inflammatory properties. It may help reduce inflammation associated with conditions like acne, eczema, and psoriasis.',
            'Supporting digestive health: Aloe vera juice has been traditionally used to support digestive health. It may help alleviate symptoms of gastrointestinal disorders, such as acid reflux, indigestion, and irritable bowel syndrome (IBS). However, it\'s essential to use it cautiously and consult a healthcare professional, as excessive consumption may cause adverse effects.'
        ],
        'commonGrowthLocation': 'Aloe vera is native to the Arabian Peninsula, but it is cultivated worldwide, especially in regions with warm climates.',
        'disclaimer': 'Consult a qualified healthcare professional before using aloe vera, especially if you have any allergies or medical conditions.'
    },
    'Amla': {
        'scientificName': 'Phyllanthus emblica',
        'medicinalProperty': 'Amla is valued for its high vitamin C content and antioxidant properties, which contribute to its various medicinal benefits. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Boosting immune function: Amla is one of the richest natural sources of vitamin C, which plays a crucial role in supporting immune function. Regular consumption of amla may help strengthen the immune system and reduce the risk of infections, colds, and flu.',
            'Supporting heart health: Amla contains potent antioxidants, such as vitamin C and flavonoids, which may help protect the heart by reducing oxidative stress and inflammation. It may also help lower cholesterol levels and improve blood circulation, thereby reducing the risk of heart disease and stroke.',
            'Promoting hair and skin health: Amla is often used in traditional Ayurvedic medicine for promoting hair growth and maintaining healthy skin. It is rich in nutrients like vitamin C, which nourish the scalp and skin, improve hair texture, and prevent premature aging.',
            'Enhancing digestion: Amla is known for its digestive properties and is used to treat various digestive disorders, including indigestion, acidity, and constipation. It helps stimulate the digestive fire (agni), improve nutrient absorption, and regulate bowel movements.'
        ],
        'commonGrowthLocation': 'Amla trees are native to India and are also found in other parts of Asia, including Sri Lanka, Bangladesh, and Nepal.',
        'disclaimer': 'Consult a qualified healthcare professional before using amla, especially if you have any allergies or medical conditions.'
    },
    'Amruta_Balli': {
        'scientificName': 'Tinospora cordifolia',
        'medicinalProperty': 'Amruta Balli, also known as Tinospora cordifolia or Giloy, is a medicinal plant widely used in Ayurveda. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Boosting immune function: Amruta Balli is known for its immunomodulatory properties, which help enhance the body\'s natural defense mechanisms. It stimulates the production of white blood cells and strengthens the immune system, thereby reducing the risk of infections and diseases.',
            'Anti-inflammatory and antioxidant effects: Amruta Balli contains bioactive compounds like alkaloids, glycosides, and flavonoids, which possess potent anti-inflammatory and antioxidant properties. These compounds help reduce inflammation, neutralize free radicals, and protect against oxidative stress, thereby promoting overall health and well-being.',
            'Supporting liver health: Amruta Balli is beneficial for liver health and is used to treat various liver disorders, including hepatitis, jaundice, and fatty liver disease. It helps detoxify the liver, improve liver function, and protect against liver damage caused by toxins and free radicals.',
            'Managing diabetes: Amruta Balli may help regulate blood sugar levels and improve insulin sensitivity, making it beneficial for individuals with diabetes. It helps control blood glucose levels, prevent complications associated with diabetes, and enhance overall metabolic health.'
        ],
        'commonGrowthLocation': 'Amruta Balli is native to tropical regions of India and is also found in other parts of Southeast Asia.',
        'disclaimer': 'Consult a qualified healthcare professional before using Amruta Balli, especially if you have any allergies or medical conditions.'
    },
    'Arali': {
        'scientificName': 'Ricinus communis',
        'medicinalProperty': 'Arali, also known as Castor Plant, is known for its medicinal properties, especially the oil derived from its seeds. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Laxative and purgative effects: Castor oil is widely used as a natural laxative to relieve constipation and promote bowel movements. It contains ricinoleic acid, a fatty acid that stimulates contractions in the intestines and helps move stool through the digestive tract. However, it should be used with caution and in moderation to avoid dehydration and electrolyte imbalances.',
            'Anti-inflammatory and analgesic effects: Castor oil is applied topically to reduce inflammation and relieve pain associated with various conditions, such as arthritis, muscle strains, and joint pain. It penetrates the skin easily and has a soothing effect on inflamed tissues, promoting healing and pain relief.',
            'Moisturizing and nourishing skin: Castor oil is a common ingredient in skincare products due to its moisturizing and emollient properties. It helps hydrate the skin, improve its elasticity, and reduce dryness and flakiness. It is often used to treat dry skin conditions like eczema, psoriasis, and dermatitis.',
            'Promoting hair growth: Castor oil is beneficial for hair health and is used to promote hair growth, thicken hair strands, and prevent hair loss. It nourishes the scalp, strengthens the hair follicles, and improves blood circulation to the scalp, resulting in healthier and more luscious hair.'
        ],
        'commonGrowthLocation': 'Castor plants are native to tropical regions of Africa and Asia but are cultivated worldwide for their seeds, which are used to extract castor oil.',
        'disclaimer': 'Consult a qualified healthcare professional before using Arali or castor oil, especially if you have any allergies or medical conditions.'
    },


    'Ashoka': {
        'scientificName': 'Saraca asoca',
        'medicinalProperty': 'Ashoka, also known as Saraca asoca, is a medicinal tree valued for its various therapeutic properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Regulating menstrual cycle: Ashoka bark is traditionally used in Ayurvedic medicine to regulate the menstrual cycle and relieve symptoms associated with menstrual disorders, such as irregular periods, menstrual cramps, and excessive bleeding. It helps balance hormonal levels, improve uterine health, and promote regular menstruation.',
            'Supporting reproductive health: Ashoka is beneficial for women\'s reproductive health and is used to treat various gynecological conditions, including uterine fibroids, ovarian cysts, and polycystic ovary syndrome (PCOS). It helps reduce inflammation, shrink fibroids and cysts, and alleviate symptoms like pelvic pain and discomfort.',
            'Aiding in postpartum recovery: Ashoka is used to promote postpartum recovery and support lactation in new mothers. It helps tone the uterus, reduce postpartum bleeding, and enhance milk production, thereby facilitating faster recovery and better maternal health.',
            'Relieving menopausal symptoms: Ashoka may help alleviate menopausal symptoms like hot flashes, night sweats, mood swings, and vaginal dryness. It helps balance hormonal levels, support emotional well-being, and improve overall quality of life during the menopausal transition.'
        ],
        'commonGrowthLocation': 'Ashoka trees are native to India and are also found in other parts of South Asia, Southeast Asia, and Australia.',
        'disclaimer': 'Consult a qualified healthcare professional before using Ashoka, especially if you have any allergies or medical conditions.'
    },


    'Ashwagandha': {
        'scientificName': 'Withania somnifera',
        'medicinalProperty': 'Ashwagandha, also known as Indian ginseng or winter cherry, is a medicinal herb with adaptogenic properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Reducing stress and anxiety: Ashwagandha is known for its adaptogenic properties, which help the body cope with stress and reduce anxiety levels. It modulates the stress response by regulating cortisol levels, enhancing the body\'s resilience to stressors, and promoting relaxation and calmness.',
            'Improving cognitive function: Ashwagandha has neuroprotective effects and is used to enhance cognitive function, memory, and concentration. It helps support brain health, improve nerve signaling, and protect against age-related cognitive decline and neurodegenerative disorders, such as Alzheimer\'s disease and Parkinson\'s disease.',
            'Boosting energy and vitality: Ashwagandha is traditionally used as a rejuvenating tonic to increase energy levels, stamina, and vitality. It helps enhance physical performance, reduce fatigue, and improve overall endurance and resilience.',
            'Supporting hormonal balance: Ashwagandha has hormone-balancing effects and is used to regulate hormonal imbalances in both men and women. It helps support thyroid function, balance cortisol levels, and improve reproductive hormone levels, thereby promoting overall hormonal health and well-being.'
        ],
        'commonGrowthLocation': 'Ashwagandha is native to the Indian subcontinent and is found in various parts of India, Pakistan, Sri Lanka, and Nepal. It is also cultivated in other regions with similar climatic conditions, such as parts of Africa, the Middle East, and Southeast Asia.',
        'disclaimer': 'Consult a qualified healthcare professional before using Ashwagandha, especially if you are pregnant, breastfeeding, or have any underlying health conditions.'
    },
    'Avocado': {
        'scientificName': 'Persea americana',
        'medicinalProperty': 'Avocado, scientifically known as Persea americana, is a fruit valued for its nutritional and medicinal properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Heart health: Avocado is rich in monounsaturated fats, particularly oleic acid, which may help reduce LDL (bad) cholesterol levels and lower the risk of heart disease. It also contains potassium, which helps regulate blood pressure and prevent hypertension, a risk factor for heart disease.',
            'Skin health: Avocado is a good source of vitamins E and C, antioxidants that help protect the skin from oxidative damage caused by free radicals. These nutrients promote skin health, reduce inflammation, and accelerate wound healing. Avocado oil is also used topically to moisturize and nourish the skin.',
            'Eye health: Avocado contains lutein and zeaxanthin, two carotenoid antioxidants that are beneficial for eye health. These compounds help protect the eyes from age-related macular degeneration and cataracts by filtering harmful blue light and reducing oxidative stress in the retina.',
            'Weight management: Despite being high in calories, avocado consumption is associated with weight management and satiety. The fiber and healthy fats in avocados help increase feelings of fullness, reduce appetite, and regulate blood sugar levels, making it a valuable addition to weight loss and maintenance diets.'
        ],
        'commonGrowthLocation': 'Avocado trees are native to Central America and Mexico but are now cultivated in various tropical and subtropical regions worldwide, including California, Florida, and Mediterranean countries.',
        'disclaimer': 'Consult a qualified healthcare professional before using avocado or avocado products, especially if you have any allergies or medical conditions.'
    },
    'Bamboo': {
        'scientificName': 'Bambusoideae',
        'medicinalProperty': 'Bamboo is a versatile plant with various medicinal properties. Different parts of the bamboo plant, including the shoots, leaves, and stems, are used in traditional medicine for their therapeutic effects. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Antioxidant and anti-inflammatory effects: Bamboo contains bioactive compounds like flavonoids, phenolic acids, and lignans, which possess antioxidant and anti-inflammatory properties. These compounds help neutralize free radicals, reduce inflammation, and protect against chronic diseases like cancer, diabetes, and cardiovascular disorders.',
            'Promoting bone health: Bamboo extract is rich in silica, a mineral essential for bone health and connective tissue formation. Silica helps strengthen bones, improve bone density, and prevent conditions like osteoporosis and osteoarthritis. It also supports collagen synthesis, contributing to healthy joints and cartilage.',
            'Supporting skin health: Bamboo extract is used in skincare products for its moisturizing, soothing, and anti-aging properties. It helps hydrate the skin, improve elasticity, and reduce wrinkles and fine lines. Bamboo sap, obtained from bamboo stems, is rich in amino acids, vitamins, and minerals that nourish and rejuvenate the skin.',
            'Detoxifying and purifying properties: Bamboo charcoal, derived from bamboo stems, is known for its detoxifying and purifying properties. It absorbs toxins, pollutants, and impurities from the skin, making it an effective ingredient in detox masks, cleansers, and skincare products. Bamboo charcoal also helps regulate oil production, minimize pores, and prevent acne and blackheads.'
        ],
        'commonGrowthLocation': 'Bamboo is native to Asia but is now cultivated in various parts of the world with suitable climates, including China, India, Southeast Asia, and parts of Africa and South America.',
        'disclaimer': 'Consult a qualified healthcare professional before using bamboo or bamboo-derived products, especially if you have any allergies or medical conditions.'
    },
    'Basale': {
        'scientificName': 'Basella alba',
        'medicinalProperty': 'Basale, also known as Malabar spinach or Indian spinach, is a leafy green vegetable with various medicinal properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Nutrient-rich: Basale is rich in vitamins, minerals, and antioxidants, making it a highly nutritious food. It is particularly high in vitamin A, vitamin C, iron, calcium, and folate, which are essential for maintaining overall health and well-being.',
            'Supporting digestive health: Basale is a good source of dietary fiber, which helps promote digestive health by regulating bowel movements, preventing constipation, and supporting a healthy gut microbiome. Fiber also helps reduce the risk of digestive disorders like diverticulitis and hemorrhoids.',
            'Boosting immune function: Basale contains antioxidants like vitamin C, beta-carotene, and flavonoids, which help strengthen the immune system and protect against infections and diseases. Regular consumption of Basale may help reduce the risk of colds, flu, and other respiratory infections.',
            'Anti-inflammatory effects: Basale contains phytochemicals with anti-inflammatory properties, which help reduce inflammation and alleviate symptoms of inflammatory conditions like arthritis, asthma, and inflammatory bowel disease (IBD). Including Basale in the diet may help manage chronic inflammatory conditions and promote overall health.'
        ],
        'commonGrowthLocation': 'Basale is native to tropical regions of Asia and Africa and is cultivated in various parts of the world, including India, Sri Lanka, Malaysia, and Nigeria.',
        'disclaimer': 'Consult a qualified healthcare professional before using Basale, especially if you have any allergies or medical conditions.'
    },


    'Betel': {
        'scientificName': 'Piper betle',
        'medicinalProperty': 'Betel, also known as Piper betle, is a vine belonging to the Piperaceae family, valued for its medicinal and cultural significance. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Stimulating digestion: Betel leaves are traditionally chewed after meals to aid digestion and freshen breath. They contain bioactive compounds like eugenol, tannins, and essential oils, which stimulate saliva production, improve gastric motility, and enhance digestive enzyme activity. Betel leaves also possess carminative properties, relieving gas and bloating.',
            'Oral health benefits: Betel leaves have antiseptic and analgesic properties, making them beneficial for oral health. Chewing betel leaves helps cleanse the mouth, prevent bacterial growth, and reduce plaque formation, reducing the risk of cavities, gum disease, and bad breath. Betel leaves are also used in traditional medicine to relieve toothache and oral ulcers.',
            'Refreshing and energizing effects: Betel leaves have stimulating and refreshing effects on the body and mind. They contain alkaloids like arecoline and chavibetol, which act as mild stimulants, improving alertness, concentration, and mood. Chewing betel leaves is a common practice in many cultures to boost energy and relieve fatigue.',
            'Anti-inflammatory and analgesic effects: Betel leaves have anti-inflammatory and analgesic properties, making them useful for relieving pain and inflammation associated with various conditions, such as arthritis, muscle sprains, and insect bites. Topical application of betel leaf extract or oil may help reduce swelling, redness, and discomfort.'
        ],
        'commonGrowthLocation': 'Betel vines are native to Southeast Asia but are cultivated in other tropical regions of the world, including India, Sri Lanka, Indonesia, and the Philippines.',
        'disclaimer': 'Consult a qualified healthcare professional before using betel leaves or betel-derived products, especially if you have any oral health issues or medical conditions.'
    },
    'Betel_Nut': {
        'scientificName': 'Areca catechu',
        'medicinalProperty': 'Betel nut, also known as Areca catechu or areca palm, is the seed of the betel palm tree, valued for its medicinal and cultural significance. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Stimulating digestion: Betel nuts are traditionally chewed after meals to aid digestion and freshen breath. They contain bioactive compounds like arecoline, alkaloids, and tannins, which stimulate saliva production, improve gastric motility, and enhance digestive enzyme activity. Betel nuts also possess carminative properties, relieving gas and bloating.',
            'Energizing effects: Betel nuts have stimulant properties due to the presence of alkaloids like arecoline and arecaidine. Chewing betel nuts stimulates the central nervous system, increasing alertness, concentration, and mood. It is a common practice in many cultures to chew betel nuts to boost energy and relieve fatigue.',
            'Appetite suppression: Betel nuts have appetite-suppressing effects and are used as a natural remedy for weight loss. The stimulant properties of betel nuts help reduce feelings of hunger and promote satiety, making it easier to control food intake and prevent overeating.',
            'Oral health benefits: Betel nuts have antiseptic properties and are beneficial for oral health. Chewing betel nuts helps cleanse the mouth, prevent bacterial growth, and reduce plaque formation, reducing the risk of cavities, gum disease, and bad breath. However, excessive consumption of betel nuts may stain the teeth and cause oral health problems.'
        ],
        'commonGrowthLocation': 'Betel palms are native to Southeast Asia but are cultivated in other tropical regions of the world, including India, Sri Lanka, Indonesia, and the Philippines.',
        'disclaimer': 'Consult a qualified healthcare professional before using betel nuts or betel-derived products, especially if you have any oral health issues or medical conditions.'
    },
    'Brahmi': {
        'scientificName': 'Bacopa monnieri',
        'medicinalProperty': 'Brahmi, also known as Bacopa monnieri or water hyssop, is a medicinal herb valued for its cognitive-enhancing properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Improving cognitive function: Brahmi is known for its nootropic effects, which help enhance memory, concentration, and learning ability. It contains active compounds like bacosides, which promote nerve cell communication, increase neurotransmitter levels, and protect brain cells from oxidative damage.',
            'Reducing anxiety and stress: Brahmi has adaptogenic properties that help the body cope with stress and reduce anxiety levels. It modulates the stress response by regulating cortisol levels, enhancing resilience to stressors, and promoting relaxation and calmness. Regular consumption of Brahmi may help improve mood stability and reduce symptoms of anxiety and depression.',
            'Supporting brain health: Brahmi is beneficial for overall brain health and is used to prevent age-related cognitive decline and neurodegenerative disorders, such as Alzheimer\'s disease and dementia. It enhances brain circulation, increases oxygen and nutrient supply to the brain, and improves neuronal function, promoting cognitive longevity and vitality.',
            'Enhancing sleep quality: Brahmi has sedative properties and is used to improve sleep quality and duration. It helps relax the mind and body, reduce insomnia symptoms, and promote restful sleep. Brahmi is often included in herbal sleep aids and relaxation formulas to support healthy sleep patterns.'
        ],
        'commonGrowthLocation': 'Brahmi is native to wetlands and marshy areas of India, Nepal, Sri Lanka, and other parts of Southeast Asia. It is also cultivated in other tropical regions of the world for its medicinal properties.',
        'disclaimer': 'Consult a qualified healthcare professional before using Brahmi, especially if you are pregnant, breastfeeding, or have any underlying health conditions.'
    },
    'Castor': {
        'scientificName': 'Ricinus communis',
        'medicinalProperty': 'Castor, also known as Ricinus communis, is a plant valued for its medicinal properties, especially the oil derived from its seeds. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Laxative and purgative effects: Castor oil is widely used as a natural laxative to relieve constipation and promote bowel movements. It contains ricinoleic acid, a fatty acid that stimulates contractions in the intestines and helps move stool through the digestive tract. However, it should be used with caution and in moderation to avoid dehydration and electrolyte imbalances.',
            'Anti-inflammatory and analgesic effects: Castor oil is applied topically to reduce inflammation and relieve pain associated with various conditions, such as arthritis, muscle strains, and joint pain. It penetrates the skin easily and has a soothing effect on inflamed tissues, promoting healing and pain relief.',
            'Moisturizing and nourishing skin: Castor oil is a common ingredient in skincare products due to its moisturizing and emollient properties. It helps hydrate the skin, improve its elasticity, and reduce dryness and flakiness. It is often used to treat dry skin conditions like eczema, psoriasis, and dermatitis.',
            'Promoting hair growth: Castor oil is beneficial for hair health and is used to promote hair growth, thicken hair strands, and prevent hair loss. It nourishes the scalp, strengthens the hair follicles, and improves blood circulation to the scalp, resulting in healthier and more luscious hair.'
        ],
        'commonGrowthLocation': 'Castor plants are native to tropical regions of Africa and Asia but are cultivated worldwide for their seeds, which are used to extract castor oil.',
        'disclaimer': 'Consult a qualified healthcare professional before using Castor or castor oil, especially if you have any allergies or medical conditions.'
    },
    'Curry_Leaf': {
        'scientificName': 'Murraya koenigii',
        'medicinalProperty': 'Curry leaf, scientifically known as Murraya koenigii, is a medicinal plant valued for its culinary and therapeutic properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Improving digestion: Curry leaves are traditionally used to aid digestion and relieve gastrointestinal issues like indigestion, bloating, and constipation. They contain carbazole alkaloids, which stimulate digestive enzymes, enhance gastric motility, and improve nutrient absorption, promoting overall digestive health.',
            'Regulating blood sugar levels: Curry leaves have hypoglycemic properties and are beneficial for managing diabetes and insulin resistance. They help lower blood sugar levels by inhibiting carbohydrate digestion and absorption, increasing insulin sensitivity, and improving glucose utilization by cells.',
            'Protecting liver health: Curry leaves possess hepatoprotective properties and are used to support liver function and prevent liver damage. They help detoxify the liver, eliminate toxins and free radicals, and reduce inflammation, thereby promoting liver health and preventing liver disorders like fatty liver disease and hepatitis.',
            'Promoting hair growth: Curry leaves are rich in antioxidants, vitamins, and minerals that nourish the scalp and hair follicles, promoting hair growth and preventing hair loss. They help strengthen hair roots, improve hair texture, and reduce scalp irritation, dandruff, and premature graying.'
        ],
        'commonGrowthLocation': 'Curry leaf plants are native to tropical regions of India and Sri Lanka but are now cultivated in other parts of Asia, Africa, and the Americas.',
        'disclaimer': 'Consult a qualified healthcare professional before using curry leaves or curry leaf-derived products, especially if you have any allergies or medical conditions.'
    },
    'Doddapatre': {
        'scientificName': 'Plectranthus amboinicus',
        'medicinalProperty': 'Doddapatre, also known as Cuban oregano or Indian borage, is a medicinal herb with various therapeutic properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Relieving respiratory symptoms: Doddapatre leaves are traditionally used to alleviate respiratory symptoms like cough, cold, asthma, and bronchitis. They contain bioactive compounds like carvacrol, thymol, and eugenol, which have expectorant, bronchodilator, and antimicrobial properties, helping clear airway congestion and reduce inflammation.',
            'Supporting digestive health: Doddapatre is beneficial for digestive health and is used to treat gastrointestinal disorders like indigestion, bloating, and diarrhea. It helps stimulate digestive enzymes, improve nutrient absorption, and regulate bowel movements, promoting overall digestive wellness.',
            'Reducing inflammation: Doddapatre possesses anti-inflammatory properties and is used to reduce inflammation and pain associated with various conditions, such as arthritis, gout, and insect bites. It helps inhibit inflammatory mediators, suppress inflammatory pathways, and promote tissue healing.',
            'Promoting wound healing: Doddapatre leaves are applied topically to wounds, cuts, and insect bites to promote healing and prevent infections. They have antiseptic and antimicrobial properties, which help cleanse the wound, inhibit bacterial growth, and accelerate tissue repair and regeneration.'
        ],
        'commonGrowthLocation': 'Doddapatre is native to tropical and subtropical regions of Asia and Africa and is cultivated in home gardens and herbal farms for its medicinal and culinary uses.',
        'disclaimer': 'Consult a qualified healthcare professional before using Doddapatre, especially if you have any allergies or medical conditions.'
    },
    'Ekka': {
        'scientificName': 'Madhuca longifolia',
        'medicinalProperty': 'Ekka, also known as Madhuca longifolia or Indian butter tree, is a medicinal plant valued for its various therapeutic properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Relieving joint pain and inflammation: Ekka oil, extracted from the seeds of the Ekka tree, is used topically to reduce joint pain, inflammation, and stiffness associated with conditions like arthritis, rheumatism, and gout. It has analgesic, anti-inflammatory, and warming properties, which help soothe sore muscles and improve joint mobility.',
            'Nourishing and moisturizing skin: Ekka oil is a rich source of fatty acids, vitamins, and antioxidants that nourish and moisturize the skin. It helps hydrate dry skin, restore skin elasticity, and protect against moisture loss, making it beneficial for dry, rough, or irritated skin conditions.',
            'Promoting hair growth: Ekka oil is used to promote hair growth, prevent hair loss, and improve hair texture and shine. It penetrates the scalp easily, nourishing the hair follicles, stimulating blood circulation, and promoting healthy hair growth. Ekka oil is often used in hair care formulations like hair oils and hair masks.',
            'Supporting respiratory health: Ekka leaves are used in traditional medicine to relieve respiratory symptoms like cough, cold, and bronchitis. They have expectorant, bronchodilator, and antimicrobial properties, which help clear airway congestion, reduce inflammation, and inhibit bacterial growth in the respiratory tract.'
        ],
        'commonGrowthLocation': 'Ekka trees are native to the Indian subcontinent and are found in various parts of India, Nepal, Bangladesh, and Sri Lanka. They are also cultivated in other tropical and subtropical regions of Asia and Africa for their medicinal and economic value.',
        'disclaimer': 'Consult a qualified healthcare professional before using Ekka or Ekka-derived products, especially if you have any allergies or medical conditions.'
    },
    'Ganike': {
        'scientificName': 'Piper nigrum',
        'medicinalProperty': 'Ganike, also known as Piper nigrum or black pepper, is a spice valued for its culinary and medicinal properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Improving digestion: Ganike stimulates digestion and helps relieve gastrointestinal issues like indigestion, bloating, and constipation. It contains piperine, a bioactive compound that increases digestive enzyme activity, enhances gastric motility, and improves nutrient absorption, promoting overall digestive wellness.',
            'Boosting metabolism: Ganike is known to boost metabolism and promote weight loss by increasing thermogenesis and fat oxidation. Piperine, the active compound in black pepper, enhances metabolic rate, improves insulin sensitivity, and reduces fat accumulation, making it beneficial for weight management.',
            'Enhancing nutrient absorption: Ganike enhances the bioavailability of nutrients by inhibiting enzymes that metabolize drugs and nutrients in the liver and intestine. Piperine helps increase the absorption of vitamins, minerals, and phytonutrients, maximizing their health benefits and efficacy in the body.',
            'Supporting respiratory health: Ganike has expectorant and decongestant properties, making it beneficial for respiratory health. It helps relieve respiratory symptoms like cough, cold, and congestion by loosening mucus, clearing airway passages, and reducing inflammation in the respiratory tract.'
        ],
        'commonGrowthLocation': 'Black pepper plants are native to South India but are cultivated in other tropical regions of Asia, Africa, and the Americas. They thrive in warm, humid climates with well-drained soil and ample sunlight.',
        'disclaimer': 'Consult a qualified healthcare professional before using Ganike or black pepper, especially if you have any allergies or medical conditions.'
    },
    'Gauva': {
        'scientificName': 'Psidium guajava',
        'medicinalProperty': 'Guava, scientifically known as Psidium guajava, is a tropical fruit valued for its nutritional and medicinal properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Boosting immune function: Guava is rich in vitamin C, an essential nutrient for immune function. Regular consumption of guava helps strengthen the immune system, reduce the risk of infections, and enhance the body\'s ability to fight off pathogens like bacteria and viruses.',
            'Improving digestive health: Guava is a good source of dietary fiber, which promotes digestive health by regulating bowel movements, preventing constipation, and supporting a healthy gut microbiome. Fiber also helps reduce the risk of digestive disorders like diverticulitis and hemorrhoids.',
            'Lowering blood sugar levels: Guava has hypoglycemic properties and is beneficial for managing diabetes and insulin resistance. It helps regulate blood sugar levels by inhibiting carbohydrate digestion and absorption, improving insulin sensitivity, and enhancing glucose utilization by cells.',
            'Protecting cardiovascular health: Guava contains antioxidants like vitamins A and C, flavonoids, and polyphenols, which help reduce oxidative stress, inflammation, and cholesterol levels in the blood. Regular consumption of guava may help lower the risk of heart disease, stroke, and other cardiovascular disorders.'
        ],
        'commonGrowthLocation': 'Guava trees are native to Central America and Mexico but are now cultivated in tropical and subtropical regions worldwide, including Asia, Africa, and the Americas.',
        'disclaimer': 'Consult a qualified healthcare professional before using guava or guava-derived products, especially if you have any allergies or medical conditions.'
    },
    
    'Geranium': {
        'scientificName': 'Pelargonium graveolens',
        'medicinalProperty': 'Geranium, scientifically known as Pelargonium graveolens, is a medicinal plant valued for its therapeutic properties, particularly in aromatherapy and skincare. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Balancing hormones: Geranium essential oil is used in aromatherapy to balance hormones and alleviate symptoms associated with hormonal imbalances, such as menstrual cramps, PMS, and menopausal symptoms. It helps regulate estrogen and progesterone levels, reduce mood swings, and promote emotional well-being.',
            'Improving skin health: Geranium oil is beneficial for skin health and is used in skincare products for its moisturizing, anti-inflammatory, and astringent properties. It helps hydrate the skin, reduce inflammation, and tighten pores, making it suitable for all skin types, including dry, oily, and acne-prone skin.',
            'Relieving stress and anxiety: Geranium oil has calming and uplifting effects on the mind and body, making it useful for reducing stress, anxiety, and tension. It helps promote relaxation, improve mood, and enhance mental clarity, creating a sense of well-being and balance.',
            'Repelling insects: Geranium oil has insect-repelling properties and is used as a natural alternative to chemical insecticides. It repels mosquitoes, flies, ticks, and other pests, making it an effective ingredient in insect repellent sprays, lotions, and candles.'
        ],
        'commonGrowthLocation': 'Geranium plants are native to South Africa but are now cultivated in other parts of the world for their aromatic and medicinal properties. They thrive in temperate climates and well-drained soil.',
        'disclaimer': 'Consult a qualified healthcare professional before using geranium oil or geranium-derived products, especially if you have any allergies or medical conditions.'
    },
    'Henna': {
        'scientificName': 'Lawsonia inermis',
        'medicinalProperty': 'Henna, scientifically known as Lawsonia inermis, is a plant valued for its dyeing and medicinal properties, particularly in traditional medicine and cosmetic applications. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Hair conditioning and coloring: Henna leaves are used to make a natural hair dye that conditions the hair, adds shine, and enhances hair color. Henna dye binds to the hair shaft, coating it with a translucent color that reflects light and creates depth and dimension. It is a popular natural alternative to chemical hair dyes.',
            'Skin cooling and soothing: Henna paste is applied topically to the skin to cool and soothe various skin conditions, including burns, rashes, and insect bites. It has a cooling effect on the skin, reducing inflammation, itching, and discomfort. Henna is also used to create intricate temporary tattoos (mehndi) for festive and ceremonial occasions.',
            'Wound healing: Henna has antiseptic and antimicrobial properties, which help prevent infections and promote wound healing. Applying henna paste to cuts, wounds, and minor burns creates a protective barrier against bacteria and other pathogens, reducing the risk of infection and accelerating the healing process.',
            'Treating dandruff and scalp conditions: Henna is used in hair care formulations to treat dandruff, dry scalp, and other scalp conditions. It has antifungal properties that help control dandruff-causing fungi, soothe scalp irritation, and restore scalp health.'
        ],
        'commonGrowthLocation': 'Henna plants are native to North Africa, the Middle East, and South Asia but are now cultivated in other parts of the world with suitable climates, including India, Pakistan, Egypt, and Sudan.',
        'disclaimer': 'Consult a qualified healthcare professional before using henna or henna-derived products, especially if you have any allergies or skin sensitivities.'
    },
    'Hibiscus': {
        'scientificName': 'Hibiscus rosa-sinensis',
        'medicinalProperty': 'Hibiscus, scientifically known as Hibiscus rosa-sinensis, is a flowering plant valued for its medicinal properties, particularly in traditional medicine systems like Ayurveda and Chinese medicine. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Lowering blood pressure: Hibiscus tea is rich in polyphenols and anthocyanins, antioxidants that help lower blood pressure by relaxing blood vessels and improving blood flow. Regular consumption of hibiscus tea may help reduce hypertension, a risk factor for heart disease and stroke.',
            'Supporting liver health: Hibiscus contains bioactive compounds like flavonoids and polyphenols, which have hepatoprotective properties and support liver function. It helps detoxify the liver, reduce oxidative stress, and prevent liver damage caused by toxins, alcohol, and free radicals.',
            'Promoting weight loss: Hibiscus tea is often used as a natural weight loss aid due to its diuretic and metabolism-boosting effects. It helps flush out excess fluids and toxins from the body, reduce water retention, and increase fat metabolism, leading to weight loss and improved body composition.',
            'Enhancing skin and hair health: Hibiscus is rich in vitamins A, C, and E, antioxidants that nourish and protect the skin and hair from oxidative damage. It helps promote collagen production, improve skin elasticity, and reduce wrinkles and fine lines. Hibiscus is also used in hair care formulations to strengthen hair follicles, prevent hair loss, and promote healthy hair growth.'
        ],
        'commonGrowthLocation': 'Hibiscus plants are native to tropical and subtropical regions of Asia, Africa, and the Americas but are now cultivated worldwide for their ornamental and medicinal value.',
        'disclaimer': 'Consult a qualified healthcare professional before using hibiscus or hibiscus-derived products, especially if you have any allergies or medical conditions.'
    },
    'Honge': {
        'scientificName': 'Pongamia pinnata',
        'medicinalProperty': 'Honge, also known as Pongamia pinnata or Indian beech, is a medicinal tree valued for its various therapeutic properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Skin healing and protection: Honge oil, extracted from the seeds of the Honge tree, is used topically to promote skin healing and protect against skin infections. It has antiseptic, antimicrobial, and anti-inflammatory properties, which help prevent bacterial growth, reduce inflammation, and accelerate wound healing. Honge oil is often used to treat skin conditions like eczema, psoriasis, acne, and dermatitis.',
            'Insect repellent: Honge oil is used as a natural insect repellent to protect against mosquitoes, flies, ticks, and other pests. It contains compounds like pongamol and karanjin, which repel insects by interfering with their feeding, mating, and egg-laying behaviors. Honge oil is applied topically to the skin or used in insect repellent formulations like sprays and lotions.',
            'Promoting hair growth: Honge oil is beneficial for hair health and is used to promote hair growth, prevent hair loss, and improve hair texture and shine. It nourishes the scalp, strengthens the hair follicles, and stimulates blood circulation to the scalp, promoting healthy hair growth. Honge oil is often used in hair care products like shampoos, conditioners, and hair oils.',
            'Supporting wound healing: Honge leaves and bark are used in traditional medicine to promote wound healing and relieve pain and inflammation. They contain bioactive compounds with antimicrobial, anti-inflammatory, and analgesic properties, which help cleanse wounds, prevent infections, and reduce swelling and discomfort.'
        ],
        'commonGrowthLocation': 'Honge trees are native to South Asia and Southeast Asia and are found in various parts of India, Nepal, Sri Lanka, Myanmar, Thailand, and Indonesia. They are also cultivated in other tropical and subtropical regions of the world for their medicinal and economic value.',
        'disclaimer': 'Consult a qualified healthcare professional before using Honge or Honge-derived products, especially if you have any allergies or medical conditions.'
    },


    'Insulin': {
    'scientificName': 'Coccinia grandis',
    'medicinalProperty': 'Insulin plant, scientifically known as Coccinia grandis, is a medicinal plant valued for its antidiabetic properties. Some of its key medicinal properties include:',
    'medicinalDetails': [
      'Lowering blood sugar levels: Insulin plant leaves contain bioactive compounds like flavonoids, alkaloids, and saponins, which help lower blood sugar levels by stimulating insulin production and improving insulin sensitivity. Regular consumption of insulin plant leaves may help manage diabetes and reduce the risk of complications associated with high blood sugar levels.',
      'Supporting liver health: Insulin plant has hepatoprotective properties and is beneficial for liver health. It helps detoxify the liver, reduce oxidative stress, and prevent liver damage caused by toxins, alcohol, and free radicals. Insulin plant leaves are used in traditional medicine to support liver function and treat liver disorders like fatty liver disease and hepatitis.',
      'Reducing inflammation: Insulin plant possesses anti-inflammatory properties, which help reduce inflammation and pain associated with various conditions, such as arthritis, gout, and inflammatory bowel disease (IBD). It helps inhibit inflammatory mediators, suppress inflammatory pathways, and promote tissue healing, improving overall health and well-being.',
      'Promoting wound healing: Insulin plant leaves are applied topically to wounds, cuts, and insect bites to promote healing and prevent infections. They have antiseptic and antimicrobial properties, which help cleanse the wound, inhibit bacterial growth, and accelerate tissue repair and regeneration.'
    ],
    'commonGrowthLocation': 'Insulin plants are native to tropical and subtropical regions of Asia, Africa, and Australia and are cultivated in home gardens and herbal farms for their medicinal and culinary uses.',
    'disclaimer': 'Consult a qualified healthcare professional before using insulin plant leaves or insulin plant-derived products, especially if you have any allergies or medical conditions.'
  },
  'Jasmine': {
    'scientificName': 'Jasminum sambac',
    'medicinalProperty': 'Jasmine, scientifically known as Jasminum sambac, is a flowering plant valued for its aromatic flowers and medicinal properties. Some of its key medicinal properties include:',
    'medicinalDetails': [
      'Relieving stress and anxiety: Jasmine essential oil is used in aromatherapy to reduce stress, anxiety, and depression and promote relaxation and emotional well-being. Its sweet, floral scent has a calming effect on the mind and body, helping alleviate tension, improve mood, and induce feelings of comfort and tranquility.',
      'Improving sleep quality: Jasmine oil is beneficial for promoting restful sleep and treating insomnia and sleep disorders. Its sedative properties help relax the nervous system, reduce sleep latency, and improve sleep duration and quality. Inhaling jasmine oil or using it in a diffuser before bedtime can help create a soothing sleep environment and enhance sleep hygiene.',
      'Enhancing skin health: Jasmine oil is used in skincare products for its moisturizing, toning, and rejuvenating properties. It helps hydrate the skin, reduce dryness and irritation, and improve skin elasticity and texture. Jasmine oil is suitable for all skin types and is often used in facial oils, serums, and moisturizers to promote healthy, radiant skin.',
      'Relieving muscle pain and spasms: Jasmine oil has analgesic and antispasmodic properties, making it useful for relieving muscle pain, cramps, and spasms. It helps relax tense muscles, reduce inflammation, and improve blood circulation, providing relief from soreness, stiffness, and discomfort.'
    ],
    'commonGrowthLocation': 'Jasmine plants are native to tropical and subtropical regions of Asia, Africa, and Australasia but are now cultivated worldwide for their ornamental and medicinal value.',
    'disclaimer': 'Consult a qualified healthcare professional before using jasmine oil or jasmine-derived products, especially if you have any allergies or medical conditions.'
  },
  'Lemon': {
    'scientificName': 'Citrus limon',
    'medicinalProperty': 'Lemon, scientifically known as Citrus limon, is a citrus fruit valued for its nutritional and medicinal properties. Some of its key medicinal properties include:',
    'medicinalDetails': [
      'Boosting immune function: Lemons are rich in vitamin C, an essential nutrient for immune function. Regular consumption of lemon juice helps strengthen the immune system, reduce the risk of infections, and enhance the body\'s ability to fight off pathogens like bacteria and viruses.',
      'Supporting digestion: Lemon juice has digestive properties and is used to alleviate gastrointestinal issues like indigestion, bloating, and constipation. It helps stimulate digestive enzymes, enhance gastric motility, and improve nutrient absorption, promoting overall digestive wellness.',
      'Alkalizing the body: Despite being acidic in nature, lemons have an alkalizing effect on the body when metabolized. They help balance the body\'s pH levels, reduce acidity, and create a more alkaline environment, which is believed to promote overall health and well-being.',
      'Detoxifying the liver: Lemons contain compounds like citric acid and flavonoids, which help detoxify the liver, stimulate bile production, and eliminate toxins and waste products from the body. Regular consumption of lemon water or lemon juice may help support liver function and improve liver health.'
    ],
    'commonGrowthLocation': 'Lemon trees are native to South Asia but are now cultivated in other tropical and subtropical regions worldwide, including India, China, Mexico, and the Mediterranean countries.',
    'disclaimer': 'Consult a qualified healthcare professional before using lemons or lemon-derived products, especially if you have any allergies or medical conditions.'
  },
  'Lemon_grass': {
    'scientificName': 'Cymbopogon citratus',
    'medicinalProperty': 'Lemongrass, scientifically known as Cymbopogon citratus, is a medicinal herb valued for its various therapeutic properties, particularly in traditional medicine systems like Ayurveda and Traditional Chinese Medicine (TCM). Some of its key medicinal properties include:',
    'medicinalDetails': [
      'Relieving digestive issues: Lemongrass is used to alleviate digestive issues like indigestion, bloating, and stomach cramps. It contains compounds like citral, which help relax the stomach muscles, improve digestion, and reduce gastrointestinal discomfort.',
      'Reducing inflammation: Lemongrass has anti-inflammatory properties that help reduce inflammation and pain associated with conditions like arthritis, muscle aches, and headaches. It inhibits the production of inflammatory compounds in the body, providing relief from swelling and discomfort.',
      'Lowering cholesterol levels: Lemongrass tea is believed to help lower cholesterol levels and improve heart health. It contains antioxidants like flavonoids, which help reduce oxidative stress and inflammation in the arteries, lowering the risk of cardiovascular diseases like atherosclerosis and heart attacks.',
      'Promoting relaxation and sleep: Lemongrass has calming and sedative effects on the nervous system, making it beneficial for reducing stress, anxiety, and insomnia. Drinking lemongrass tea or inhaling its aroma helps promote relaxation, improve mood, and induce restful sleep.'
    ],
    'commonGrowthLocation': 'Lemongrass is native to tropical regions of Asia, Africa, and Australia but is now cultivated in other parts of the world for its culinary and medicinal uses. It thrives in warm climates with well-drained soil and ample sunlight.',
    'disclaimer': 'Consult a qualified healthcare professional before using lemongrass or lemongrass-derived products, especially if you have any allergies or medical conditions.'
  },


   'Mango': {
    'scientificName': 'Mangifera indica',
    'medicinalProperty': 'Mango, scientifically known as Mangifera indica, is a tropical fruit valued for its delicious taste and various health benefits. Some of its key medicinal properties include:',
    'medicinalDetails': [
      'Boosting immune function: Mangoes are rich in vitamins A and C, antioxidants that help strengthen the immune system and protect against infections. Regular consumption of mangoes may help reduce the risk of colds, flu, and other respiratory infections.',
      'Improving digestion: Mangoes contain dietary fiber and enzymes like amylases, which aid digestion and promote gastrointestinal health. They help regulate bowel movements, prevent constipation, and support a healthy gut microbiome, reducing the risk of digestive disorders like irritable bowel syndrome (IBS) and colon cancer.',
      'Supporting heart health: Mangoes contain potassium, magnesium, and antioxidants like quercetin and beta-carotene, which help regulate blood pressure, reduce cholesterol levels, and protect against oxidative stress and inflammation in the cardiovascular system. Regular consumption of mangoes may help lower the risk of heart disease, stroke, and other cardiovascular disorders.',
      'Promoting skin health: Mangoes are rich in vitamins A and E, antioxidants that nourish and protect the skin from oxidative damage caused by UV radiation, pollution, and other environmental factors. They help promote collagen production, improve skin elasticity, and reduce wrinkles and fine lines, enhancing overall skin health and appearance.'
    ],
    'commonGrowthLocation': 'Mango trees are native to South Asia but are now cultivated in tropical and subtropical regions worldwide, including India, Southeast Asia, Africa, and the Americas.',
    'disclaimer': 'Consult a qualified healthcare professional before using mangoes or mango-derived products, especially if you have any allergies or medical conditions.'
  },
  'Mint': {
    'scientificName': 'Mentha',
    'medicinalProperty': 'Mint, scientifically known as Mentha, is a medicinal herb valued for its various therapeutic properties, particularly in traditional medicine systems like Ayurveda and Western herbalism. Some of its key medicinal properties include:',
    'medicinalDetails': [
      'Relieving digestive issues: Mint is commonly used to alleviate digestive issues like indigestion, bloating, and stomach cramps. It contains compounds like menthol, which help relax the muscles of the digestive tract, improve bile flow, and reduce gastrointestinal discomfort.',
      'Reducing nausea and vomiting: Mint is effective in relieving nausea and vomiting associated with motion sickness, morning sickness during pregnancy, chemotherapy, and other causes. Its aroma and flavor help calm the stomach, suppress the urge to vomit, and promote relaxation.',
      'Relieving headaches and migraines: Mint has analgesic and vasodilator properties that help relieve headaches and migraines. Applying mint oil or inhaling its aroma helps relax tense muscles, improve blood circulation, and alleviate pain and discomfort associated with headaches.',
      'Improving respiratory health: Mint has decongestant and expectorant properties that help relieve respiratory symptoms like cough, congestion, and asthma. It helps clear airway passages, reduce inflammation in the respiratory tract, and promote easier breathing.'
    ],
    'commonGrowthLocation': 'Mint is native to Europe, Asia, and North America but is now cultivated in other parts of the world for its culinary and medicinal uses. It thrives in moist soil and temperate climates with partial shade.',
    'disclaimer': 'Consult a qualified healthcare professional before using mint or mint-derived products, especially if you have any allergies or medical conditions.'
  },
  'Nagadali': {
    'scientificName': 'Tabernaemontana divaricata',
    'medicinalProperty': 'Nagadali, also known as Tabernaemontana divaricata or pinwheel flower, is a medicinal plant valued for its various therapeutic properties. Some of its key medicinal properties include:',
    'medicinalDetails': [
      'Relieving pain and inflammation: Nagadali is used to alleviate pain and inflammation associated with conditions like arthritis, rheumatism, and muscle strains. It contains bioactive compounds with analgesic and anti-inflammatory properties, which help reduce pain, swelling, and stiffness in the joints and muscles.',
      'Promoting relaxation and sleep: Nagadali has sedative and anxiolytic effects on the nervous system, making it useful for reducing stress, anxiety, and insomnia. Drinking nagadali tea or inhaling its aroma helps promote relaxation, improve mood, and induce restful sleep.',
      'Supporting respiratory health: Nagadali is beneficial for respiratory health and is used to relieve cough, cold, and bronchitis. It has expectorant and bronchodilator properties that help clear airway congestion, reduce inflammation in the respiratory tract, and promote easier breathing.',
      'Enhancing skin health: Nagadali is used topically to promote skin health and treat various skin conditions like acne, eczema, and dermatitis. It has antimicrobial and anti-inflammatory properties, which help cleanse the skin, inhibit bacterial growth, and reduce inflammation and itching.'
    ],
    'commonGrowthLocation': 'Nagadali plants are native to South and Southeast Asia and are found in various parts of India, Sri Lanka, Myanmar, Thailand, and Indonesia. They are also cultivated in other tropical and subtropical regions of the world for their medicinal and ornamental value.',
    'disclaimer': 'Consult a qualified healthcare professional before using nagadali or nagadali-derived products, especially if you have any allergies or medical conditions.'
  },
  'Neem': {
    'scientificName': 'Azadirachta indica',
    'medicinalProperty': 'Neem, scientifically known as Azadirachta indica, is a medicinal tree valued for its various therapeutic properties. Some of its key medicinal properties include:',
    'medicinalDetails': [
      'Treating skin conditions: Neem is used to treat various skin conditions like acne, eczema, psoriasis, and fungal infections. It has antimicrobial, anti-inflammatory, and antiseptic properties, which help cleanse the skin, inhibit bacterial and fungal growth, and reduce inflammation and itching.',
      'Promoting dental health: Neem is beneficial for dental health and is used in traditional oral care products like toothpaste, mouthwash, and dental powders. It helps prevent dental caries, gum disease, and bad breath by inhibiting bacterial growth, reducing plaque formation, and maintaining oral hygiene.',
      'Supporting immune function: Neem boosts immune function and helps the body fight off infections and diseases. It contains bioactive compounds like nimbin, nimbidin, and quercetin, which stimulate the production of immune cells, enhance their activity, and strengthen the body\'s defense mechanisms against pathogens like bacteria, viruses, and fungi.',
      'Regulating blood sugar levels: Neem leaves and extracts are beneficial for managing diabetes and insulin resistance. They help lower blood sugar levels by improving insulin sensitivity, inhibiting carbohydrate digestion and absorption, and enhancing glucose utilization by cells.'
    ],
    'commonGrowthLocation': 'Neem trees are native to the Indian subcontinent and are found in various parts of India, Nepal, Bangladesh, Sri Lanka, and Pakistan. They are also cultivated in other tropical and subtropical regions of Asia, Africa, and the Americas for their medicinal and economic value.',
    'disclaimer': 'Consult a qualified healthcare professional before using neem or neem-derived products, especially if you have any allergies or medical conditions.'
  },


    'Nithyapushpa': {
    'scientificName': 'Vinca rosea',
    'medicinalProperty': 'Nithyapushpa, also known as Vinca rosea or Madagascar periwinkle, is a medicinal plant valued for its various therapeutic properties. Some of its key medicinal properties include:',
    'medicinalDetails': [
      'Treating diabetes: Nithyapushpa is used to manage diabetes and improve blood sugar control. It contains bioactive compounds like alkaloids, which help lower blood sugar levels by stimulating insulin secretion, increasing glucose uptake by cells, and inhibiting glucose absorption in the intestine.',
      'Fighting cancer: Nithyapushpa has anticancer properties and is used as a natural remedy for cancer prevention and treatment. It contains alkaloids like vincristine and vinblastine, which inhibit the growth of cancer cells, induce apoptosis (cell death), and prevent tumor progression in various types of cancer, including leukemia, lymphoma, and solid tumors.',
      'Relieving menstrual disorders: Nithyapushpa is beneficial for relieving menstrual disorders like irregular periods, menstrual cramps, and excessive bleeding. It helps regulate menstrual cycles, reduce menstrual pain and discomfort, and balance hormonal levels, improving overall menstrual health and well-being.',
      'Enhancing cognitive function: Nithyapushpa has neuroprotective properties and is used to enhance cognitive function and memory. It contains alkaloids and flavonoids, which protect brain cells from oxidative stress and inflammation, improve cerebral blood flow, and enhance neurotransmitter activity, promoting mental clarity and cognitive performance.'
    ],
    'commonGrowthLocation': 'Nithyapushpa plants are native to Madagascar but are now cultivated in other tropical and subtropical regions of the world for their medicinal and ornamental value. They are also considered invasive species in some regions due to their prolific growth and spread.',
    'disclaimer': 'Consult a qualified healthcare professional before using nithyapushpa or nithyapushpa-derived products, especially if you have any allergies or medical conditions.'
  },
  'Nooni': {
    'scientificName': 'Vitex negundo',
    'medicinalProperty': 'Nooni, also known as Vitex negundo or five-leaved chaste tree, is a medicinal plant valued for its various therapeutic properties. Some of its key medicinal properties include:',
    'medicinalDetails': [
      'Relieving pain and inflammation: Nooni is used to alleviate pain and inflammation associated with conditions like arthritis, rheumatism, and muscle strains. It contains bioactive compounds with analgesic and anti-inflammatory properties, which help reduce pain, swelling, and stiffness in the joints and muscles.',
      'Treating respiratory disorders: Nooni is beneficial for respiratory health and is used to relieve cough, cold, asthma, and bronchitis. It has expectorant, bronchodilator, and anti-inflammatory properties that help clear airway congestion, reduce inflammation in the respiratory tract, and promote easier breathing.',
      'Supporting digestive health: Nooni is used to alleviate digestive issues like indigestion, bloating, and stomach cramps. It contains compounds like flavonoids and terpenoids, which help relax the muscles of the digestive tract, improve bile flow, and reduce gastrointestinal discomfort.',
      'Promoting wound healing: Nooni leaves and bark are applied topically to wounds, cuts, and insect bites to promote healing and prevent infections. They have antiseptic and antimicrobial properties, which help cleanse the wound, inhibit bacterial growth, and accelerate tissue repair and regeneration.'
    ],
    'commonGrowthLocation': 'Nooni plants are native to South and Southeast Asia and are found in various parts of India, Nepal, Sri Lanka, Myanmar, Thailand, and Indonesia. They are also cultivated in other tropical and subtropical regions of the world for their medicinal and ornamental value.',
    'disclaimer': 'Consult a qualified healthcare professional before using noon or noon-derived products, especially if you have any allergies or medical conditions.'
  },


    'Pappaya': {
        'scientificName': 'Carica papaya',
        'medicinalProperty': 'Pappaya, also known as Carica papaya or papaya, is a tropical fruit valued for its delicious taste and various health benefits. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Improving digestion: Papaya contains enzymes like papain, which aid digestion and promote gastrointestinal health. It helps break down proteins, fats, and carbohydrates in the diet, improving nutrient absorption, reducing bloating and indigestion, and supporting regular bowel movements.',
            'Boosting immune function: Papaya is rich in vitamins A, C, and E, antioxidants that help strengthen the immune system and protect against infections. Regular consumption of papaya may help reduce the risk of colds, flu, and other respiratory infections.',
            'Lowering inflammation: Papaya contains enzymes and antioxidants that help reduce inflammation in the body and alleviate symptoms of inflammatory conditions like arthritis, gout, and asthma. It helps inhibit inflammatory mediators, suppress inflammatory pathways, and promote tissue healing and repair.',
            'Promoting skin health: Papaya is rich in vitamins A, C, and E, antioxidants that nourish and protect the skin from oxidative damage caused by UV radiation, pollution, and other environmental factors. It helps promote collagen production, improve skin elasticity, and reduce wrinkles and fine lines, enhancing overall skin health and appearance.'
        ],
        'commonGrowthLocation': 'Papaya trees are native to tropical regions of the Americas but are now cultivated in tropical and subtropical regions worldwide, including Asia, Africa, and Oceania.',
        'disclaimer': 'Consult a qualified healthcare professional before using papaya or papaya-derived products, especially if you have any allergies or medical conditions.'
    },
    'Pepper': {
        'scientificName': 'Piper nigrum',
        'medicinalProperty': 'Pepper, scientifically known as Piper nigrum, is a spice valued for its culinary and medicinal properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Improving digestion: Pepper stimulates digestion and helps relieve gastrointestinal issues like indigestion, bloating, and constipation. It contains piperine, a bioactive compound that increases digestive enzyme activity, enhances gastric motility, and improves nutrient absorption, promoting overall digestive wellness.',
            'Boosting metabolism: Pepper is known to boost metabolism and promote weight loss by increasing thermogenesis and fat oxidation. Piperine, the active compound in black pepper, enhances metabolic rate, improves insulin sensitivity, and reduces fat accumulation, making it beneficial for weight management.',
            'Enhancing nutrient absorption: Pepper enhances the bioavailability of nutrients by inhibiting enzymes that metabolize drugs and nutrients in the liver and intestine. Piperine helps increase the absorption of vitamins, minerals, and phytonutrients, maximizing their health benefits and efficacy in the body.',
            'Supporting respiratory health: Pepper has expectorant and decongestant properties, making it beneficial for respiratory health. It helps relieve respiratory symptoms like cough, cold, and congestion by loosening mucus, clearing airway passages, and reducing inflammation in the respiratory tract.'
        ],
        'commonGrowthLocation': 'Black pepper plants are native to South India but are cultivated in other tropical regions of Asia, Africa, and the Americas. They thrive in warm, humid climates with well-drained soil and ample sunlight.',
        'disclaimer': 'Consult a qualified healthcare professional before using pepper or pepper-derived products, especially if you have any allergies or medical conditions.'
    },
    'Pomegranate': {
        'scientificName': 'Punica granatum',
        'medicinalProperty': 'Pomegranate, scientifically known as Punica granatum, is a fruit valued for its delicious taste and various health benefits. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Lowering blood pressure: Pomegranate juice is rich in polyphenols and anthocyanins, antioxidants that help lower blood pressure by relaxing blood vessels and improving blood flow. Regular consumption of pomegranate juice may help reduce hypertension, a risk factor for heart disease and stroke.',
            'Supporting heart health: Pomegranate contains potent antioxidants like punicalagins and flavonoids, which help protect the heart by reducing oxidative stress and inflammation. It helps lower cholesterol levels, prevent plaque buildup in the arteries, and improve blood circulation, reducing the risk of heart disease and stroke.',
            'Boosting immune function: Pomegranate is rich in vitamins C and E, antioxidants that help strengthen the immune system and protect against infections. Regular consumption of pomegranate may help reduce the risk of colds, flu, and other respiratory infections.',
            'Promoting skin health: Pomegranate is rich in vitamins C and E, antioxidants that nourish and protect the skin from oxidative damage caused by UV radiation, pollution, and other environmental factors. It helps promote collagen production, improve skin elasticity, and reduce wrinkles and fine lines, enhancing overall skin health and appearance.'
        ],
        'commonGrowthLocation': 'Pomegranate trees are native to the Middle East and South Asia but are now cultivated in tropical and subtropical regions worldwide, including Asia, Africa, and the Americas.',
        'disclaimer': 'Consult a qualified healthcare professional before using pomegranates or pomegranate-derived products, especially if you have any allergies or medical conditions.'
    },
    'Raktachandini': {
        'scientificName': 'Pavonia odorata',
        'medicinalProperty': 'Raktachandini, also known as Pavonia odorata or fragrant pavonia, is a medicinal plant valued for its various therapeutic properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Relieving menstrual disorders: Raktachandini is used to relieve menstrual disorders like irregular periods, menstrual cramps, and excessive bleeding. It helps regulate menstrual cycles, reduce menstrual pain and discomfort, and balance hormonal levels, improving overall menstrual health and well-being.',
            'Treating skin conditions: Raktachandini is beneficial for treating various skin conditions like acne, eczema, psoriasis, and fungal infections. It has antimicrobial, anti-inflammatory, and antiseptic properties, which help cleanse the skin, inhibit bacterial and fungal growth, and reduce inflammation and itching.',
            'Promoting wound healing: Raktachandini leaves and flowers are applied topically to wounds, cuts, and insect bites to promote healing and prevent infections. They have antiseptic and antimicrobial properties, which help cleanse the wound, inhibit bacterial growth, and accelerate tissue repair and regeneration.',
            'Enhancing respiratory health: Raktachandini is beneficial for respiratory health and is used to relieve cough, cold, asthma, and bronchitis. It has expectorant, bronchodilator, and anti-inflammatory properties that help clear airway congestion, reduce inflammation in the respiratory tract, and promote easier breathing.'
        ],
        'commonGrowthLocation': 'Raktachandini plants are native to tropical and subtropical regions of the Americas, Africa, and Asia and are found in various parts of India, Sri Lanka, Myanmar, Thailand, and Indonesia. They are also cultivated in other tropical and subtropical regions of the world for their medicinal and ornamental value.',
        'disclaimer': 'Consult a qualified healthcare professional before using raktachandini or raktachandini-derived products, especially if you have any allergies or medical conditions.'
    },


    'Rose': {
        'scientificName': 'Rosa',
        'medicinalProperty': 'Rose, scientifically known as Rosa, is a flowering plant valued for its aromatic flowers and medicinal properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Relieving stress and anxiety: Rose essential oil is used in aromatherapy to reduce stress, anxiety, and depression and promote relaxation and emotional well-being. Its sweet, floral scent has a calming effect on the mind and body, helping alleviate tension, improve mood, and induce feelings of comfort and tranquility.',
            'Enhancing skin health: Rose oil is used in skincare products for its moisturizing, toning, and rejuvenating properties. It helps hydrate the skin, reduce dryness and irritation, and improve skin elasticity and texture. Rose oil is suitable for all skin types and is often used in facial oils, serums, and moisturizers to promote healthy, radiant skin.',
            'Improving digestion: Rose water is beneficial for digestion and is used to alleviate gastrointestinal issues like indigestion, bloating, and constipation. It helps stimulate digestive enzymes, enhance gastric motility, and improve nutrient absorption, promoting overall digestive wellness.',
            'Relieving menstrual cramps: Rose tea is used to relieve menstrual cramps and other symptoms of dysmenorrhea. It has analgesic and antispasmodic properties that help relax the uterine muscles, reduce menstrual pain and discomfort, and promote menstrual flow.'
        ],
        'commonGrowthLocation': 'Roses are native to various regions of the world, including Europe, Asia, and North America, and are now cultivated worldwide for their ornamental and medicinal value.',
        'disclaimer': 'Consult a qualified healthcare professional before using rose oil, rose water, or rose-derived products, especially if you have any allergies or medical conditions.'
    },
    'Sapota': {
        'scientificName': 'Manilkara zapota',
        'medicinalProperty': 'Sapota, also known as Manilkara zapota or chikoo, is a tropical fruit valued for its sweet taste and various health benefits. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Supporting digestive health: Sapota is rich in dietary fiber, which aids digestion and promotes gastrointestinal health. It helps regulate bowel movements, prevent constipation, and support a healthy gut microbiome, reducing the risk of digestive disorders like irritable bowel syndrome (IBS) and colon cancer.',
            'Boosting immune function: Sapota is rich in vitamins A and C, antioxidants that help strengthen the immune system and protect against infections. Regular consumption of sapota may help reduce the risk of colds, flu, and other respiratory infections.',
            'Improving skin health: Sapota is rich in vitamins A and E, antioxidants that nourish and protect the skin from oxidative damage caused by UV radiation, pollution, and other environmental factors. They help promote collagen production, improve skin elasticity, and reduce wrinkles and fine lines, enhancing overall skin health and appearance.',
            'Regulating blood sugar levels: Sapota has a low glycemic index and is beneficial for managing diabetes and insulin resistance. It helps stabilize blood sugar levels, prevent spikes in insulin, and reduce the risk of hyperglycemia and related complications.'
        ],
        'commonGrowthLocation': 'Sapota trees are native to Central America and Mexico but are now cultivated in tropical and subtropical regions worldwide, including India, Sri Lanka, Southeast Asia, Africa, and the Americas.',
        'disclaimer': 'Consult a qualified healthcare professional before using sapota or sapota-derived products, especially if you have any allergies or medical conditions.'
    },
    'Tulasi': {
        'scientificName': 'Ocimum tenuiflorum',
        'medicinalProperty': 'Tulasi, also known as Ocimum tenuiflorum or holy basil, is a medicinal herb valued for its various therapeutic properties, particularly in Ayurvedic medicine. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Boosting immune function: Tulasi is known for its immunomodulatory properties and is used to boost immune function and prevent infections. It helps stimulate the production of immune cells like T cells and natural killer cells, enhance their activity, and strengthen the body\'s defense mechanisms against pathogens like bacteria, viruses, and fungi.',
            'Relieving respiratory conditions: Tulasi is beneficial for respiratory health and is used to relieve cough, cold, asthma, and bronchitis. It has expectorant, bronchodilator, and anti-inflammatory properties that help clear airway congestion, reduce inflammation in the respiratory tract, and promote easier breathing.',
            'Supporting cardiovascular health: Tulasi helps maintain cardiovascular health by lowering cholesterol levels, regulating blood pressure, and reducing oxidative stress and inflammation in the arteries. It contains antioxidants like eugenol and flavonoids, which protect the heart from damage caused by free radicals and oxidative stress.',
            'Improving stress management: Tulasi has adaptogenic properties that help the body adapt to stress and promote mental well-being. It helps reduce the production of stress hormones like cortisol, improve resilience to stress, and enhance mood, cognitive function, and overall quality of life.'
        ],
        'commonGrowthLocation': 'Tulasi is native to the Indian subcontinent and is found throughout South Asia, Southeast Asia, and parts of Africa. It is cultivated in home gardens, temples, and herbal farms for its medicinal and spiritual significance.',
        'disclaimer': 'Consult a qualified healthcare professional before using tulasi or tulasi-derived products, especially if you have any allergies or medical conditions.'
    },
    'Wood_sorel': {
        'scientificName': 'Oxalis corniculata',
        'medicinalProperty': 'Wood sorrel, scientifically known as Oxalis corniculata, is a medicinal plant valued for its various therapeutic properties. Some of its key medicinal properties include:',
        'medicinalDetails': [
            'Relieving digestive issues: Wood sorrel is used to alleviate digestive issues like indigestion, bloating, and stomach cramps. It contains compounds like oxalic acid and flavonoids, which help relax the muscles of the digestive tract, improve bile flow, and reduce gastrointestinal discomfort.',
            'Reducing inflammation: Wood sorrel has anti-inflammatory properties that help reduce inflammation and pain associated with conditions like arthritis, muscle aches, and headaches. It inhibits the production of inflammatory compounds in the body, providing relief from swelling and discomfort.',
            'Supporting liver health: Wood sorrel is beneficial for liver health and is used to detoxify the liver, reduce oxidative stress, and prevent liver damage caused by toxins, alcohol, and free radicals. It helps stimulate bile production, enhance liver function, and improve overall liver health and well-being.',
            'Promoting wound healing: Wood sorrel leaves and stems are applied topically to wounds, cuts, and insect bites to promote healing and prevent infections. They have antiseptic and antimicrobial properties, which help cleanse the wound, inhibit bacterial growth, and accelerate tissue repair and regeneration.'
        ],
        'commonGrowthLocation': 'Wood sorrel is native to Europe, Asia, and North America and is found in various temperate and subtropical regions of the world. It grows in open woodlands, grasslands, and disturbed habitats, thriving in moist, well-drained soil and partial shade.',
        'disclaimer': 'Consult a qualified healthcare professional before using wood sorrel or wood sorrel-derived products, especially if you have any allergies or medical conditions.'
    },
    
} 

class_list = list(Plant_Details.keys())

if __name__ == "__main__":
    class_list = list(Plant_Details.keys())
    print(class_list)
