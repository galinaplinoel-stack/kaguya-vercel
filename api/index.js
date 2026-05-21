export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  return res.status(200).json({
    name: 'KAGUYA — AI Personality Engine',
    version: '0.2.0',
    endpoints: {
      health: '/api/health',
      personality: '/api/personality',
      emotion: '/api/emotion',
      chat: '/api/chat',
      relationships: '/api/relationships',
      memory: '/api/memory',
    },
  });
}
