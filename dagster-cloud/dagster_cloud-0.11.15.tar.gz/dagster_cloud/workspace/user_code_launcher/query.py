UPDATE_WORKSPACE_ENTRY_MUTATION = """
    mutation updateWorkspaceEntryMutation($serializedWorkspaceEntry: String!) {
        workspace {
            updateWorkspaceEntry(serializedWorkspaceEntry: $serializedWorkspaceEntry) {
                ok
            }
        }
    }
"""
