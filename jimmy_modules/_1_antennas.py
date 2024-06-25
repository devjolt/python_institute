from random import choice

questions = {
    'All antennas': {
        'question_with_0':'Which of the following is PLACEHOLDER?',
        'question_with_1':'Which of the following best describes a PLACEHOLDER?',
        'type':['make_items_question_from_pairs'],
        'course_code':'',
        'pairs':(
            (f'a {choice(["surface", "ground"])} wave antenna',['VHF vehicle mounted', 'VHF ground spike', 'VHF elevated ground spike', 'HF vehicle mounted', 'HF sloping wire', 'HF 12m co-site']),
            ('a space wave antenna',['VHF ground spike', 'VHF monopole', 'VHF dipole', 'UHF vehicle mounted', 'UHF elevated dipole']),
            ('a sky wave antenna',['droopy dipole', 'marlborough broadband (150w)', 'horizontal', '3/4 endfed']),
            
        ),
        'fillers': (
            (['an air wave antenna', 'an ionosphere wave antenna'], [f'{choice(["tree", "air", "space", "surface", "extended", "vehicle mounted", "mexborough", "benson", "rizzler"])} {choice(["dipole", "monopole", "spike", "wire", "ariel", "satcom", "coax"])}', 'mushroom'])
        )
    }
}