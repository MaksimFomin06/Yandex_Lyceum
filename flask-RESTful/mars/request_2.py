from data.db_session import create_session, global_init
from data.users import User


def main():
    db = "db\mars_explorer.db"
    global_init(db)
    db_sess = create_session()
    colonists = db_sess.query(User.id).filter(
        User.address.like('module_1%'),
        ~User.speciality.like('%engineer%'),
        ~User.position.like('%engineer%')
    ).all()
    
    for colonist in colonists:
        print(colonist[0])


if __name__ == "__main__":
    main()