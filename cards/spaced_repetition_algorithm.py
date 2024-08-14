from datetime import datetime, timezone
from .models import LearningPhase, LearningStep

def evaluate_card(card, learning_step_id, step, graduating_interval, max_interval_days):
    DEFAULT_HARD_INTERVAL = 0.8 
    DEFAULT_EASY_BONUS = 1.3
    MINIMUM_EASE = 1.3
    MINIMUM_INTERVAL = 1

    learning_step_instance = LearningStep.objects.get(id=learning_step_id)
    learning_step = learning_step_instance.des_learning_step

    if card.id_learning_phase:
        learning_phase = card.id_learning_phase.des_learning_phase
    else:
        learning_phase = None

    current_interval = card.nex_interval_card
    ease_factor = card.eas_factor_card / 100 

    if card.fir_review_card is None:
        card.fir_review_card = datetime.now(timezone.utc).isoformat()

      
    if learning_phase is None or learning_phase == "Learning Phase": 
        if learning_step == "Again":
            new_interval = MINIMUM_INTERVAL  
            card.id_learning_phase = LearningPhase.objects.get(des_learning_phase="Learning Phase")
        elif learning_step == "Hard":
            new_interval = step * DEFAULT_HARD_INTERVAL
            card.id_learning_phase = LearningPhase.objects.get(des_learning_phase="Learning Phase")
        elif learning_step == "Good" or learning_step == "Easy":
            new_interval = graduating_interval * 60  
            card.id_learning_phase = LearningPhase.objects.get(des_learning_phase="Graduated Phase")
    else:
        if learning_step == "Again":
            card.lap_card = True
            new_interval = 10  
            ease_factor -= 0.2
            card.id_learning_phase = LearningPhase.objects.get(des_learning_phase="Learning Phase")
        elif learning_step == "Hard":
            ease_factor -= 0.15
            new_interval = current_interval * 1.2
        elif learning_step == "Good":
            new_interval = current_interval * ease_factor
        elif learning_step == "Easy":
            new_interval = current_interval * ease_factor * DEFAULT_EASY_BONUS
            ease_factor += 0.15

        ease_factor = max(ease_factor, MINIMUM_EASE)
        new_interval = min(new_interval, max_interval_days * 1440)

    card.nex_interval_card = new_interval
    if card.rev_card > 0:
        card.las_interval_card = current_interval
        card.las_review_card = datetime.now(timezone.utc).isoformat()
        card.id_last_learning_step = learning_step_instance
    else:
        card.las_interval_card = None
        card.las_review_card = None
        card.id_last_learning_step = None
    card.eas_factor_card = int(ease_factor * 100)
    card.rev_card += 1
    
    return card