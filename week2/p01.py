thresholds = {
    "會計系": [
        {
            "subjects": [1, 1, 1, 1, 0],
            "score": 57
        },
        {
            "subjects": [1, 0, 0, 0, 0],
            "score": 15
        }
    ],
    "公衛系": [
        {
            "subjects": [0, 1, 1, 0, 1],
            "score": 38
        }
    ],
    "經濟系": [
        {
            "subjects": [0, 0, 0, 1, 1],
            "score": 26
        },
        {
            "subjects": [0, 0, 1, 0, 0],
            "score": 15
        }
    ],
    "資工系": [
        {
            "subjects": [0, 1, 0, 1, 0],
            "score": 27
        },
        {
            "subjects": [0, 0, 1, 0, 0],
            "score": 15
        }
    ],
}

scores = list(map(int, input().split(',')))
target = input()

def couldPass(threshold):
    if sum([a*b for a, b in zip(scores, threshold["subjects"])]) >= threshold["score"]:
        return True
    else:
        return False

if all(map(couldPass, thresholds[target])):
    print(1)
else:
    print(0)