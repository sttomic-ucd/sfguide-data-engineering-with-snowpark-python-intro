from snowflake.snowpark import Session


def main(session: Session) -> str:
    return f"OK"
    
# For local debugging
if __name__ == "__main__":
    # Create a local Snowpark session
    with Session.builder.getOrCreate() as session:
        main(session)