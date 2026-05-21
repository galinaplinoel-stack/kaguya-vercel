const EMOTION_ICONS = {
  joy: ' ', sadness: ' ', anger: ' ', fear: ' ',
  surprise: ' ', disgust: ' ', trust: ' ', anticipation: ' ', neutral: ' ',
};

let emotion = {
  primary: 'joy',
  intensity: 0.72,
  valence: 0.6,
  arousal: 0.5,
  icon: ' ',
};

export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();

  if (req.method === 'POST' && req.body?.event) {
    const event = req.body.event.toLowerCase();
    if (/happy|good|love|great|wonderful/.test(event)) {
      emotion = { primary: 'joy', intensity: 0.85, valence: 0.8, arousal: 0.6, icon: ' ' };
    } else if (/sad|bad|miss|lonely|cry/.test(event)) {
      emotion = { primary: 'sadness', intensity: 0.7, valence: -0.5, arousal: 0.3, icon: ' ' };
    } else if (/angry|hate|annoying|stupid/.test(event)) {
      emotion = { primary: 'anger', intensity: 0.75, valence: -0.6, arousal: 0.8, icon: ' ' };
    } else if (/surprise|wow|omg|unexpected/.test(event)) {
      emotion = { primary: 'surprise', intensity: 0.8, valence: 0.3, arousal: 0.9, icon: ' ' };
    } else {
      emotion = { primary: 'neutral', intensity: 0.5, valence: 0.0, arousal: 0.4, icon: ' ' };
    }
  }

  return res.status(200).json({ profile_id: 'default', emotion });
}
