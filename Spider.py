from zhihu_oauth import ZhihuClient

client = ZhihuClient()

client.load_token('token.pkl')

me = client.me()





# answer = client.answer(94150403)

# print(answer.question.title)
# print(answer.author.name)
# print(answer.voteup_count)
# print(answer.thanks_count)
# print(answer.created_time)
# print(answer.updated_time)

# for voter in answer.voters:
#     print(voter.name, voter.headline)


question_number=[20787350]


for  q in question_number:

    index=0
    question = client.question(q)

    print(question.title)

    for answer in question.answers:
        if index>666:break
        print(answer.author.name, answer.voteup_count)
        answer.save(question.title)
        index+=1