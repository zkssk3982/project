from blood.service import BloodService

if __name__ == '__main__':
    service = BloodService('data.txt')
    raw_data = service.create_raw_data()
    service.draw_chart(raw_data)
    result = service.make_session(raw_data)
    print("결과 {}".format(result))