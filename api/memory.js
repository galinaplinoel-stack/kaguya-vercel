let memories = [
  { id: 'mem_001', content: 'First interaction with the user', importance: 0.8, emotional_valence: 0.7, timestamp: Date.now() - 86400000, type: 'episodic' },
  { id: 'mem_002', content: 'User asked about personality engine capabilities', importance: 0.6, emotional_valence: 0.3, timestamp: Date.now() - 3600000, type: 'semantic' },
];

export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();

  if (req.method === 'POST' && req.body?.content) {
    memories.push({
      id: `mem_${String(memories.length + 1).padStart(3, '0')}`,
      content: req.body.content,
      importance: req.body.importance ?? 0.5,
      emotional_valence: req.body.emotional_valence ?? 0.0,
      timestamp: Date.now(),
      type: req.body.type ?? 'episodic',
    });
  }

  return res.status(200).json({ profile_id: 'default', memories, total: memories.length });
}
