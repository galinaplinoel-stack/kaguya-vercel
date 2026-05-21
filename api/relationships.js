let relationships = [
  { id: 'user_001', name: 'User', trust: 0.75, affection: 0.68, familiarity: 0.55, interactions: 42 },
];

export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();

  if (req.method === 'POST' && req.body?.name) {
    relationships.push({
      id: `user_${String(relationships.length + 1).padStart(3, '0')}`,
      name: req.body.name,
      trust: req.body.trust ?? 0.5,
      affection: req.body.affection ?? 0.5,
      familiarity: req.body.familiarity ?? 0.3,
      interactions: 0,
    });
  }

  return res.status(200).json({ profile_id: 'default', relationships });
}
