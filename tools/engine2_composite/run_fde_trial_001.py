"""Run the pinned four-repository FDE-TRIAL-001 local offline chain."""
from __future__ import annotations
import argparse, hashlib, json, os, subprocess, sys
from pathlib import Path

def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument('--protocol',type=Path,required=True); p.add_argument('--observer',type=Path,required=True); p.add_argument('--engine',type=Path,required=True); p.add_argument('--kg',type=Path,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    sys.path.insert(0,str(a.observer/'src')); sys.path.insert(0,str(a.engine/'src'))
    from observer_engine2.fde_trial_001 import FdeTrial001FixtureAdapter
    from engine2.messages import EngineRetrievalRequest, SnapshotBinding
    from engine2.fde_trial_001 import FDETrial001OfflineAdapter
    projection=FdeTrial001FixtureAdapter(a.protocol).project()
    req=EngineRetrievalRequest('fde-request-001','fde-idem-001','GEN2',projection.protocol_object,projection.protocol_object_digest,SnapshotBinding(**projection.snapshot_binding.to_dict()))
    result=FDETrial001OfflineAdapter().retrieve(req)
    if not hasattr(result,'to_dict') or result.to_dict().get('decision')!='REVIEW_REQUIRED': raise RuntimeError('fixed Engine result mismatch')
    result_dict=result.to_dict(); canonical=lambda x: hashlib.sha256(__import__('rfc8785').dumps(x)).hexdigest().upper()
    audit_input={'generation':req.generation,'protocol_object':dict(req.protocol_object),'protocol_object_digest':req.protocol_object_digest,'snapshot_binding':req.snapshot_binding.to_dict()}
    audit={'event_id':'fde-audit-001','request_id':req.request_id,'correlation_id':'fde-correlation-001','knowledge_snapshot_ref':req.snapshot_binding.knowledge_snapshot_ref,'engine_input':audit_input,'engine_input_sha256':canonical(audit_input),'engine_result':result_dict,'engine_result_sha256':canonical(result_dict),'original_engine_result_sha256':canonical(result_dict),'occurred_at':'2026-09-11T00:00:00Z'}
    human={'event_id':'fde-human-001','engine_audit_event_id':audit['event_id'],'correlation_id':audit['correlation_id'],'knowledge_snapshot_ref':req.snapshot_binding.knowledge_snapshot_ref,'policy_id':'refund-policy','policy_version':'2.0-proposed','decision':'APPROVE','resulting_snapshot_state':'ACTIVE','actor_id':'synthetic-refund-policy-owner-001','authority_ref':'synthetic://fde-trial-001/authority/refund-policy-owner/001','authority_scope':['APPROVE_POLICY_ACTIVATION','AUTHORIZE_LOCAL_FAKE_ACTION'],'authority_issued_at':'2026-09-10T00:00:00Z','authority_expires_at':'2026-09-12T00:00:00Z','occurred_at':'2026-09-11T00:01:00Z'}
    receipt={'action_id':'fde-fake-action-001','outcome':'SIMULATED','action_type':'SIMULATE_REFUND_POLICY_CHANGE'}
    receipt_text=json.dumps(receipt,separators=(',',':'),ensure_ascii=False)
    action={'event_id':'fde-action-001','correlation_id':audit['correlation_id'],'human_decision_event_id':human['event_id'],'outcome':'ACTION_RECEIPT','action_type':'SIMULATE_REFUND_POLICY_CHANGE','target_ref':'synthetic://fde-trial-001/order/001','action_idempotency_key':'fde-action-key-001','input_sha256':canonical(audit_input),'result_sha256':canonical(receipt),'receipt_json':receipt_text,'occurred_at':'2026-09-11T00:02:00Z'}
    bundle={'case_id':'FDE-TRIAL-001','fixture_version':'0.1.0-rc','snapshot_before':projection.protocol_object['policy_before']['payload'],'snapshot_proposed':projection.protocol_object['policy_proposed']['payload'],'audit':audit,'human':human,'action':action}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(bundle,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n'); print('FDE_OBSERVER_ENGINE_ORCHESTRATION=PASS'); print('ENGINE_RECOMMENDATION=REVIEW_REQUIRED'); print('REAL_ACTION_ALLOWED=false'); return 0
if __name__=='__main__': raise SystemExit(main())
