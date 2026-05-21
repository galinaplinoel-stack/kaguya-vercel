const DEFAULT_TRAITS = {
  openness: 0.75,
  conscientiousness: 0.62,
  extraversion: 0.71,
  agreeableness: 0.78,
  neuroticism: 0.34,
};

// In-memory store (resets on cold start)
let traits = { ...DEFAULT_TRAITS };

export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();

  if (req.method === 'POST' && req.body?.traits) {
    for (const [key, val] of Object.entries(req.body.traits)) {
      if (key in traits) {
        traits[key] = Math.max(0, Math.min(1, parseFloat(val)));
      }
    }
  }

  return res.status(200).json({
    profile_id: 'default',
    traits,
    version: '0.2.0',
  });
}
