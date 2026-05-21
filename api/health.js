export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  return res.status(200).json({ status: 'ok', engine: 'kaguya', version: '0.2.0' });
}
