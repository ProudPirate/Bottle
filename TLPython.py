from collections import Counter


class Features:
    """to extract the most requested top number of features
    as long as it is a part of possible features"""

    def get_top_features(self, topFeaturesNumber, possibleFeatures, featureRequests):
        """Method for getting top Features as per topFeaturesNumber input

        Args:
            topFeaturesNumber ([integer]): [no of features to be extracted]
            possibleFeatures ([list]): [possible pool of features]
            featureRequests ([list]): [customer requests]

        Returns:
            [list]: [extracted top topFeaturesNumber from possibleFeatures]
        """
        # Make dictionary of feature value pair
        possibleFeaturesMap = dict()
        for feature in possibleFeatures:
            # Initialize the value of given feature to 0
            possibleFeaturesMap[feature] = 0
            for request in featureRequests:
                # Increment the count of possibleFeature item
                possibleFeaturesMap[feature] += (request.lower()).count(feature)
        c = Counter(possibleFeaturesMap)
        # returns top topFeaturesNumber values
        return c.most_common(topFeaturesNumber)


topFeaturesNumber = 3
possibleFeatures = ["storage", "battery",
                    "hover", "alexa", "waterproof", "solar"]
featureRequests = [
    "I wish my Kindle had even more storage",
    "I wish the battery life on my Kindle lasted 2 years.",
    "I read in the bath and would enjoy a waterproof Kindle",
    "Waterproof and increased battery are my top two",
    "I want to take my Kindle into the shower. Waterproof please waterproof!",
    "I wanna make my Kindle hover on my desk",
    "How about a solar Kindle!",
]

if __name__ == "__main__":
    # Instantiation
    jar = Features()
    item = jar.get_top_features(
        topFeaturesNumber, possibleFeatures, featureRequests)
    print(f"Top {topFeaturesNumber} feature requests are :")
    for e in item:
        print(f"{e[0]} \t=>count {e[1]}")
