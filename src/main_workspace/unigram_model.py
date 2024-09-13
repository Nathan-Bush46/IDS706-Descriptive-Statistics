import random


def predict_word():
    """predict a word"""
    return "the"


def predict_unigram():
    """predict a unigram"""
    return {"the": 0.6, "of": 0.3, "dinosaur": 0.1}


def sample_from_distribution(dist: dict[str, float], k: int):
    """Sample from distribution"""
    pop = list(dist.keys())
    weights = list(dist.values())
    print(pop, weights)
    return random.choices(pop, weights, k=k)


if __name__ == "__main__":
    print(predict_word())
    print(sample_from_distribution(predict_unigram(), 20))
