def main():
    db = input()
    global_init(db)
    db_sess = create_session()
    colonists = db_sess.query(User).filter(User.address.like('module_1%')).all()
    for colonist in colonists:
        print(colonist)


if __name__ == "__main__":
    main()