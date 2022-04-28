#!/usr/bin/env bash

PORT=5000
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "CHAS":{  
      "0":0
   },
   "RM":{  
      "0":1600.575
   },
   "TAX":{  
      "0":2960.0
   },
   "PTRATIO":{  
      "0":155.3
   },
   "B":{  
      "0":3956.9
   },
   "LSTAT":{  
      "0":4.98
   }
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict