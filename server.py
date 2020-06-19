import uvicorn
import os

import templates


async def app(scope, receive, send):
  """
  Server endpoint for all the Epyk reports
  
  :param scope:
  :param receive:
  :param send:
  """
  assert scope['type'] == 'http'
  script_name = scope['path'][1:]

  if 'refresh=Y' in scope['query_string'].decode("utf-8"):
    templates.refresh(script_name)

  await send({
    'type': 'http.response.start',
    'status': 200,
    'headers': [
      [b'content-type', b'text/html'],
    ]
  })

  with open(os.path.join("views", "%s.html" % script_name)) as f:
    await send({
      'type': 'http.response.body',
      'body': f.read().encode('utf-8'),
    })


if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=5000, log_level="info", reload=True)
