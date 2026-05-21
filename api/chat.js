const RESPONSES = {
  joy: ['That makes me so happy!  ', 'Wonderful! Feeling great about this!', 'Yay! This is amazing!'],
  neutral: ['I see. Tell me more.', 'Interesting perspective.', 'Hmm, I understand.'],
  curiosity: ['Oh? Fascinating! Tell me more!', 'Im really curious!', 'What an interesting thought!'],
};

const pick = (arr) => arr[Math.floor(Math.random() * arr.length)];

export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { message = '', emotion = 'neutral' } = req.body || {};
  let response;

  const msg = message.toLowerCase();
  if (/hello|hi|hey|halo/.test(msg)) {
    response = pick(['Hello there! Nice to meet you!  ', 'Hi! Im KAGUYA!', 'Hey! How can I help?']);
  } else if (/who are you|what are you/.test(msg)) {
    response = "Im KAGUYA, an AI Personality Engine! I have emotions, relationships, and I evolve over time.";
  } else if (/how are you|how do you feel/.test(msg)) {
    response = `Im feeling ${emotion} right now! Thanks for asking!  `;
  } else {
    response = pick(RESPONSES[emotion] || RESPONSES.neutral);
  }

  return res.status(200).json({
    response,
    emotion,
    tone: { warmth: 0.78, humor: 0.65, formality: 0.42, verbosity: 0.55 },
    timestamp: Date.now(),
  });
}
