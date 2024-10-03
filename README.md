<p align="center">
    <img src="https://github.com/user-attachments/assets/69390b88-4ecc-4562-8a34-375699b0c271">
</p>
</br>
</br>
<hr>
<h1 align="center">Not Another Topic Explorer</h1>
</br>
</br>
</br>
# compliance-v3


```Shell
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```
```json
{
    "emp_id": "12345678",
    "user_message": "what is the value of tesla going to be in 2025?",
    "document_uploaded": false,
    "document_metadata": {
        "path": "no-path",
        "name": "doc",
        "workspace": "workspace-name",
        "rag_embed_index": "table-name",
        "rag_raw_index": "table-name"
    }
}
```


### document_metadata_schema
```json
document_metadata_schema {
  "properties": {
    "path": {
      "default": "no-path",
      "title": "Path",
      "type": "string"
    },
    "name": {
      "default": "doc",
      "title": "Name",
      "type": "string"
    },
    "workspace": {
      "title": "Workspace",
      "type": "string"
    },
    "rag_embed_index": {
      "title": "Rag Embed Index",
      "type": "string"
    },
    "rag_raw_index": {
      "title": "Rag Raw Index",
      "type": "string"
    }
  },
  "required": [
    "workspace",
    "rag_embed_index",
    "rag_raw_index"
  ],
  "title": "DocumentMetadata",
  "type": "object"
}
```

### real_time_message_request_schema
```json
real_time_message_request_schema {
  "$defs": {
    "DocumentMetadata": {
      "properties": {
        "path": {
          "default": "no-path",
          "title": "Path",
          "type": "string"
        },
        "name": {
          "default": "doc",
          "title": "Name",
          "type": "string"
        },
        "workspace": {
          "title": "Workspace",
          "type": "string"
        },
        "rag_embed_index": {
          "title": "Rag Embed Index",
          "type": "string"
        },
        "rag_raw_index": {
          "title": "Rag Raw Index",
          "type": "string"
        }
      },
      "required": [
        "workspace",
        "rag_embed_index",
        "rag_raw_index"
      ],
      "title": "DocumentMetadata",
      "type": "object"
    }
  },
  "properties": {
    "emp_id": {
      "title": "Emp Id",
      "type": "string"
    },
    "user_message": {
      "title": "User Message",
      "type": "string"
    },
    "document_uploaded": {
      "title": "Document Uploaded",
      "type": "boolean"
    },
    "document_metadata": {
      "anyOf": [
        {
          "$ref": "#/$defs/DocumentMetadata"
        },
        {
          "type": "null"
        }
      ]
    }
  },
  "required": [
    "emp_id",
    "user_message",
    "document_uploaded",
    "document_metadata"
  ],
  "title": "RealTimeMessageRequest",
  "type": "object"
}
```

### rule_schema
```json
rule_schema {
  "properties": {
    "id": {
      "title": "Id",
      "type": "integer"
    },
    "created_at": {
      "format": "date-time",
      "title": "Created At",
      "type": "string"
    },
    "active": {
      "title": "Active",
      "type": "boolean"
    },
    "rule": {
      "title": "Rule",
      "type": "string"
    }
  },
  "required": [
    "id",
    "created_at",
    "active",
    "rule"
  ],
  "title": "Rule",
  "type": "object"
}
```

### real_time_message_response_schema
```json
real_time_message_response_schema {
  "$defs": {
    "Rule": {
      "properties": {
        "id": {
          "title": "Id",
          "type": "integer"
        },
        "created_at": {
          "format": "date-time",
          "title": "Created At",
          "type": "string"
        },
        "active": {
          "title": "Active",
          "type": "boolean"
        },
        "rule": {
          "title": "Rule",
          "type": "string"
        }
      },
      "required": [
        "id",
        "created_at",
        "active",
        "rule"
      ],
      "title": "Rule",
      "type": "object"
    }
  },
  "properties": {
    "emp_id": {
      "title": "Emp Id",
      "type": "string"
    },
    "user_message": {
      "title": "User Message",
      "type": "string"
    },
    "document_uploaded": {
      "title": "Document Uploaded",
      "type": "boolean"
    },
    "violation_timestamp": {
      "format": "date-time",
      "title": "Violation Timestamp",
      "type": "string"
    },
    "match_count": {
      "title": "Match Count",
      "type": "integer"
    },
    "matches": {
      "items": {
        "type": "object"
      },
      "title": "Matches",
      "type": "array"
    },
    "rules": {
      "items": {
        "$ref": "#/$defs/Rule"
      },
      "title": "Rules",
      "type": "array"
    }
  },
  "required": [
    "emp_id",
    "user_message",
    "document_uploaded",
    "violation_timestamp",
    "match_count",
    "matches",
    "rules"
  ],
  "title": "RealTimeMessageResponse",
  "type": "object"
}
```

### chat_message_schema
```json
chat_message_schema {
  "properties": {
    "id": {
      "title": "Id",
      "type": "integer"
    },
    "sess_id": {
      "title": "Sess Id",
      "type": "string"
    },
    "emp_id": {
      "title": "Emp Id",
      "type": "string"
    },
    "message_id": {
      "title": "Message Id",
      "type": "integer"
    },
    "input": {
      "title": "Input",
      "type": "string"
    },
    "timestamp": {
      "format": "date-time",
      "title": "Timestamp",
      "type": "string"
    },
    "feedback_rating": {
      "title": "Feedback Rating",
      "type": "string"
    },
    "output": {
      "title": "Output",
      "type": "string"
    },
    "chat_type": {
      "title": "Chat Type",
      "type": "string"
    }
  },
  "required": [
    "id",
    "sess_id",
    "emp_id",
    "message_id",
    "input",
    "timestamp",
    "feedback_rating",
    "output",
    "chat_type"
  ],
  "title": "ChatMessage",
  "type": "object"
}
```

### batch_message_response_schema
```json
batch_message_response_schema {
  "$defs": {
    "Rule": {
      "properties": {
        "id": {
          "title": "Id",
          "type": "integer"
        },
        "created_at": {
          "format": "date-time",
          "title": "Created At",
          "type": "string"
        },
        "active": {
          "title": "Active",
          "type": "boolean"
        },
        "rule": {
          "title": "Rule",
          "type": "string"
        }
      },
      "required": [
        "id",
        "created_at",
        "active",
        "rule"
      ],
      "title": "Rule",
      "type": "object"
    }
  },
  "properties": {
    "emp_id": {
      "title": "Emp Id",
      "type": "string"
    },
    "input": {
      "title": "Input",
      "type": "string"
    },
    "chat_type": {
      "title": "Chat Type",
      "type": "string"
    },
    "timestamp": {
      "format": "date-time",
      "title": "Timestamp",
      "type": "string"
    },
    "match_count": {
      "title": "Match Count",
      "type": "integer"
    },
    "matches": {
      "items": {
        "type": "object"
      },
      "title": "Matches",
      "type": "array"
    },
    "rules": {
      "items": {
        "$ref": "#/$defs/Rule"
      },
      "title": "Rules",
      "type": "array"
    }
  },
  "required": [
    "emp_id",
    "input",
    "chat_type",
    "timestamp",
    "match_count",
    "matches",
    "rules"
  ],
  "title": "BatchMessageResponse",
  "type": "object"
}
```

### elastic_setup
```json
PUT /regex_rules_index/_settings
{
  "analysis": {
    "filter": {
      "synonym_filter": {
        "type": "synonym_graph",
        "synonyms": ["predict, forecast, anticipate"]
      }
    },
    "analyzer": {
      "custom_synonym_analyzer": {
        "type": "custom",
        "tokenizer": "standard",
        "filter": ["lowercase", "synonym_filter"]
      }
    }
  }
}

PUT /regex_rules_index/_mapping
{
  "properties": {
    "sanitiztion_term": {
      "type": "text",
      "fields": {
        "stemmed": {
          "type": "text",
          "analyzer": "english"
        },
        "synonym": {
          "type": "text",
          "analyzer": "custom_synonym_analyzer"
        },
        "raw": {
          "type": "keyword"
        }
      }
    },
    "entity": {
      "type": "text",
      "analyzer": "standard"
    }
  }
}

GET /regex_rules_index/_analyze
{
  "analyzer": "custom_synonym_analyzer",
  "text": "forecast"
}

GET /regex_rules_index/_search
{
  "query": {
    "match": {
      "sanitiztion_term.synonym": "forecast"
    }
  },
  "size": 100
}
```
