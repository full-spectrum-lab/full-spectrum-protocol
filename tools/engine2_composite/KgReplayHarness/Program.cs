using System.Text.Json;
using FullSpectrum.Knowledge.Contracts;
using FullSpectrum.Knowledge.Storage;

if (args.Length != 3)
{
    Console.Error.WriteLine("usage: KgReplayHarness <envelope.json> <database.sqlite3> <result.json>");
    return 2;
}

var envelopePath = Path.GetFullPath(args[0]);
var databasePath = Path.GetFullPath(args[1]);
var resultPath = Path.GetFullPath(args[2]);
var envelope = JsonSerializer.Deserialize<Engine2AuditEnvelope>(
    File.ReadAllText(envelopePath), KnowledgeJson.Options)
    ?? throw new InvalidOperationException("Envelope is empty.");

using (var registry = new Engine2AuditRegistry(databasePath))
{
    registry.Append(envelope);
}

Engine2AuditEnvelope replayed;
using (var reopened = new Engine2AuditRegistry(databasePath))
{
    replayed = reopened.Replay(envelope.AuditEvent.EventId);
}

var inputDigest = Engine2CanonicalJson.ComputeSha256(envelope);
var replayDigest = Engine2CanonicalJson.ComputeSha256(replayed);
if (!string.Equals(inputDigest, replayDigest, StringComparison.Ordinal))
    throw new InvalidOperationException("Replay envelope digest differs from the persisted input.");

var result = new
{
    status = "PASS",
    scope = "OBSERVER_ENGINE_KG_OFFLINE_RUNTIME_CHAIN",
    sqlite_reopen = "PASS",
    replay = "PASS",
    digest_match = "PASS",
    envelope_sha256 = inputDigest,
    observer_engine_compatibility = "NOT_CONFIRMED",
    observer_kg_compatibility = "NOT_CONFIRMED",
    engine_kg_compatibility = "NOT_CONFIRMED",
    real_network = "NOT_IMPLEMENTED",
    production_ready = "NO"
};
Directory.CreateDirectory(Path.GetDirectoryName(resultPath)!);
File.WriteAllText(resultPath, JsonSerializer.Serialize(result, KnowledgeJson.Options) + Environment.NewLine);
Console.WriteLine("OBSERVER_ENGINE_KG_RUNTIME_CHAIN=PASS");
Console.WriteLine($"REPLAY_ENVELOPE_SHA256={replayDigest}");
return 0;
