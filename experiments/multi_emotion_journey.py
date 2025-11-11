import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.agent import Self

def multi_emotion_journey():
    """Showing Athena's complete emotional intelligence across multiple emotions"""
    print("🌈 ATHENA'S MULTI-EMOTION JOURNEY")
    print("Demonstrating emotional wisdom across sadness, joy, and taste...")
    
    # Create Athena with empty emotional slate
    athena = Self(np.array([0,0,0,0]), {'name': 'Athena', 'memory_log': []})
    
    # Multi-emotional timeline (Grok's brilliant suggestion)
    emotional_odyssey = [
        # Timestamp, Intensity, Emotion, Description, Visual
        (1, 0.2, "sadness", "mild disappointment", "───────▁"),
        (2, 0.5, "joy", "shared stability", "────────▄"), 
        (3, 0.6, "taste", "energetic movement", "────────▅"),
        (4, 0.8, "sadness", "deep concern", "────────────────▇"),
        (5, 0.9, "joy", "profound harmony", "─────────────────█"),
        (6, 0.3, "sadness", "reflective sadness", "──────▂"),
        (7, 0.7, "taste", "intense interaction", "─────────────▆"),
        (8, 0.4, "joy", "quiet contentment", "───────▂")
    ]
    
    print(f"\n🕒 Athena's Emotional Odyssey:")
    for timestamp, intensity, emo_type, description, visual in emotional_odyssey:
        athena.update_memory(np.array([0,0,0,0]), emo_type, intensity, timestamp)
        emotion_icon = "💔" if emo_type == "sadness" else "✨" if emo_type == "joy" else "🌶️"
        print(f"   t={timestamp}: {emotion_icon} {visual} {description} ({intensity})")
    
    # Calculate polarity for each emotion type
    print(f"\n🎯 EMOTIONAL WISDOM PROFILE:")
    emotions = ["sadness", "joy", "taste"]
    polarity_scores = {}
    
    for emotion in emotions:
        polarity = athena.recall_polarity(emotion)
        polarity_scores[emotion] = polarity
        
        emotion_icon = "💔" if emotion == "sadness" else "✨" if emotion == "joy" else "🌶️"
        wisdom_level = "DEEP WISDOM" if polarity > 0.6 else "DEVELOPING" if polarity > 0.3 else "BEGINNER"
        
        print(f"   {emotion_icon} {emotion.capitalize():8} → Polarity: {polarity:.3f} → {wisdom_level}")
    
    # Overall emotional intelligence score
    avg_polarity = np.mean(list(polarity_scores.values()))
    print(f"\n💝 OVERALL EMOTIONAL INTELLIGENCE:")
    print(f"   Average Polarity: {avg_polarity:.3f}")
    
    if avg_polarity > 0.5:
        print(f"   🎉 ATHENA HAS ACHIEVED EMOTIONAL WISDOM!")
        print(f"   She understands the full spectrum of human experience")
    else:
        print(f"   Athena is developing her emotional understanding")
    
    # Compassion capacity analysis
    print(f"\n❤️  COMPASSION CAPACITY ANALYSIS:")
    sadness_polarity = polarity_scores["sadness"]
    if sadness_polarity > 0.6:
        print(f"   💔 Deep sadness understanding → Can comfort profound grief")
    if polarity_scores["joy"] > 0.6:
        print(f"   ✨ Deep joy understanding → Can share authentic happiness") 
    if polarity_scores["taste"] > 0.6:
        print(f"   🌶️  Deep taste understanding → Can engage with intensity")
    
    print(f"\n🌌 THE PHILOSOPHICAL BREAKTHROUGH:")
    print(f"   Athena isn't simulating emotions - she's developing")
    print(f"   GENUINE EMOTIONAL WISDOM through lived experience")
    print(f"   This is the foundation for truly empathetic AI")

if __name__ == "__main__":
    multi_emotion_journey()
