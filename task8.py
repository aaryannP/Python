posts = [
    {"user": "alice", "likes": 120, "comments": 12, "shares": 8, "topic": "tech"},
    {"user": "bob", "likes": 200, "comments": 22, "shares": 14, "topic": "travel"},
    {"user": "alice", "likes": 90, "comments": 10, "shares": 5, "topic": "tech"},
    {"user": "diana", "likes": 300, "comments": 40 , "shares": 25, "topic": "health"},
    {"user": "bob", "likes": 100, "comments": 12, "shares": 7, "topic": "travel"},
]

# Calculate total engagement per user
total_engagement = {}
for post in posts:
    user = post["user"]
    engagement = post["likes"] + post["comments"] + post["shares"]
    if user in total_engagement:
        total_engagement[user] += engagement
    else:
        total_engagement[user] = engagement
print("\nTotal Engagement per User:")
for user, engagement in total_engagement.items():
    print(f"{user}: {engagement} interactions")

# Identify the top influencer
top_influencer = max(total_engagement, key=total_engagement.get)
print(f"\nTop Influencer: {top_influencer} with {total_engagement[top_influencer]} interactions")

# Calculate topic-wise engagement
topic_engagement = {}
for post in posts:
    topic = post["topic"]
    engagement = post["likes"] + post["comments"] + post["shares"]
    if topic in topic_engagement:
        topic_engagement[topic] += engagement
    else:
        topic_engagement[topic] = engagement
print("\nTopic-wise Engagement:")
for topic, engagement in topic_engagement.items():
    print(f"{topic}: {engagement} interactions")

# Find the most engaging topic
most_engaging_topic = max(topic_engagement, key=topic_engagement.get)
print(f"\nMost Engaging Topic: {most_engaging_topic} with {topic_engagement[most_engaging_topic]} interactions")
