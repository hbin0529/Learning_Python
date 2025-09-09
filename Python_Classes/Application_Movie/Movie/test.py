'''
1. 생성자 생성 및 변수 작성 ex) application.py, movie_name, actor_name, actress_name
2. 생성한 class를 사용할 py 파일에서 import
 - ex) from application import * (또는 class 이름 ex: Movie)
3. 영화를 소개하는 것이므로 목록을 담을 list 생성 ex) list_of_movie_details = []
4. while 반복문을 돌려주며 movie_name 등을 입력받음
 - ex) movie_name = input("영화이름 : ")
5. option과 같은 변수를 넣어줌으로써 계속 진행할 것인지, 중단 할 수 있는 장치 생성.
 - ex) option = input("continue? [yes/no] : "
 *주의) while 반복문이라서 사용자가 그만할 수 있는 추가 장치를 만들어줌.
       단, 사용자가 no, NO, No, nO 등으로 작성할 수 있으니, 대소문자 비교 로직을 추가해준다.
       ex) if option.lower() == "no"
6. 마지막으로 영화목록을 담은 리스트를 반복문으로 출력.
 - ex) for movies in list_of_movie_details:
           movies.movie_details()

'''