import unittest
from jsonrpc_notification_fence.core import run
class DomainTests(unittest.TestCase):
 def test_notification_no_reply(self):
  x=run({'messages':[dict(jsonrpc='2.0',method='echo'),dict(jsonrpc='2.0',method='echo',id=1)]});self.assertEqual(len(x['replies']),1);self.assertEqual(x['notifications'],1)
 def test_null_is_request(self):self.assertEqual(run({'messages':[dict(jsonrpc='2.0',method='echo',id=None)]})['requests'],1)
 def test_typed_ids(self):self.assertEqual(run({'messages':[dict(jsonrpc='2.0',method='echo',id=x)for x in [1,'1']]})['typed_id_collisions'],0)
