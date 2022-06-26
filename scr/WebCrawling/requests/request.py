requests.request(' ', "url", **kwargs)

requests.get("url", params=None, **kwargs) //http 요청 방식
requests.post("url", data=None, json=None, **kwargs) //
requests.head("url", **kwargs) //http 요청 방식 (get의 확장) head 만 받아 옴
requests.put("url", data=None, **kwargs)
requests.patch("url", data=None, **kwargs)
requests.delete("url", **kwargs)

//params - (option) 요청 시 전달할 쿼리 문자열 지정
//data - (option) 요청 시 바디에 담아 전달할 파라미터 지정
