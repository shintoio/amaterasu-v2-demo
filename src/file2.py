high_no_df = ama_context
               .get_dataframe("start", "odd")
               .where("_1 > 100")

high_no_df.write.save("file:///tmp/test1", format="json")
