import random

def generate_matrix():
    # Define the possible shapes, patterns, and transformations
    shapes = ['square', 'circle', 'triangle']
    patterns = ['solid', 'striped', 'dotted']
    transformations = ['rotate', 'flip', 'scale']

    # Generate a random 3x3 matrix
    matrix = []
    for _ in range(3):
        row = []
        for _ in range(3):
            shape = random.choice(shapes)
            pattern = random.choice(patterns)
            transformation = random.choice(transformations)
            element = {'shape': shape, 'pattern': pattern, 'transformation': transformation}
            row.append(element)
        matrix.append(row)

    # Remove the last element to represent the missing piece
    matrix[2][2] = '?'

    return matrix

def generate_answer_options(matrix):
    # Get the shape, pattern, and transformation of the missing piece
    missing_shape = matrix[2][1]['shape']
    missing_pattern = matrix[2][1]['pattern']
    missing_transformation = matrix[1][2]['transformation']

    # Generate the correct answer
    correct_answer = {
        'shape': missing_shape,
        'pattern': missing_pattern,
        'transformation': missing_transformation
    }

    # Generate distractors (incorrect answer options)
    distractors = []
    for _ in range(7):
        shape = random.choice(['square', 'circle', 'triangle'])
        pattern = random.choice(['solid', 'striped', 'dotted'])
        transformation = random.choice(['rotate', 'flip', 'scale'])
        distractor = {'shape': shape, 'pattern': pattern, 'transformation': transformation}
        distractors.append(distractor)

    # Combine the correct answer and distractors
    answer_options = [correct_answer] + distractors
    random.shuffle(answer_options)

    return answer_options

def check_answer(matrix, selected_answer):
    # Get the shape, pattern, and transformation of the missing piece
    missing_shape = matrix[2][1]['shape']
    missing_pattern = matrix[2][1]['pattern']
    missing_transformation = matrix[1][2]['transformation']

    # Convert the selected answer from string to integer
    selected_index = int(selected_answer)

    # Get the selected answer option
    selected_option = generate_answer_options(matrix)[selected_index]

    # Check if the selected answer matches the missing piece
    if (
        selected_option['shape'] == missing_shape and
        selected_option['pattern'] == missing_pattern and
        selected_option['transformation'] == missing_transformation
    ):
        return True
    else:
        return False