from knowledge_manager.manager import KnowledgeBaseManager

manager = KnowledgeBaseManager()

print("="*60)
print("AVAILABLE KNOWLEDGE BASES")
print("=" * 60)

for kb in manager.list_knowledge_bases():
    print(manager.get_metadata(kb))