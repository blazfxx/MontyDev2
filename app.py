import streamlit as st
import random
import time

st.set_page_config(page_title="Survival Kit", page_icon="🧰")
st.title("🧰 Survival Kit?")
st.subheader("Because reality is hard, and lying is easy.")
st.caption("Created by Muhammad Khan")
st.caption("THIS IS FOR FUN, DON'T TAKE IT SERIOUSLY")



tab1, tab2, tab3, tab5 = st.tabs(["Reality Check", "Excuse generator [to save your life?]", "Listen to Music", "My Apps :D"])

with tab1:
    st.header("Can you sruvive any longer???")

    job_title = st.text_input("Whats ur job title?", placeholder="e.g., Software Engineer, Youtuber, Student, Vlogger, CEO")
    income = st.number_input("What's your income?", min_value=0, value=0)

    if st.button("Judge Me!"):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.005)
            progress.progress(i + 1)

        st.subheader("THE Verdict")

        job_lower = job_title.lower()
        
        if "dev" in job_lower or "programmer" in job_lower:
            st.error(f"Ah, a {job_title}. So you just copy-paste code all day and call it a job? Gotchu.")
        elif "youtuber" in job_lower or "vlogger" in job_lower:
            st.error(f"...{job_title}?! So you just beg for views and money? Dind't see that coming...")
        elif "ceo" in job_lower or "founder" in job_lower or "owner" in job_lower:
            st.error(f"A {job_title}? So you just exploit others for profit? Classic.")
        elif "engineer" in job_lower:
            st.error(f"{job_title}? So you just build things, but worse? Cool, cool")
        elif "student" in job_lower:
            st.error(f"You a {job_title}??? Brother, just drop out already and save us both the trouble.")
        elif "teacher" in job_lower or "professor" in job_lower:
            st.error(f"A {job_title}? One of the only actual jobs in here 🤣.")
        elif "dad" in job_lower or "mom" in job_lower:
            st.error(f"{job_title}??? When did you come back 😳")
        elif "mom" in job_lower:
            st.error(f"Hey there")
        else:
            st.write(f"'{job_title}'??? Never heard of that before, prob cause my brain is cooked...")


        if income == 0:
            st.header("💀 BROKE.")
            st.info("Put the fries in the bag or smth man")
        elif income < 1000:
            st.header("📉 POVERTY LINE GAMING.")
            st.info("Bro... BRO, whats happening???")
        elif income < 3000:
            st.header("😐 MEH.")
            st.info("You can afford rent OR food. Pick one.")
        else:
            st.header("💰 You are fine.")
            st.info(":( Lucky you..."
            "Oh, yea, gimme ur money too while you're at it.")


with tab2:
    st.header("Did yyou mess up???")
    st. subheader("Let us save you!")

    recipient = st.selectbox("Who do you need an excuse for?", ["Boss", "Teacher", "Parent", "Friend", "Coach", "Mom"])
    severty = st.slider("How bad is it?", 1, 10, 5)

    issue = ["the Wifi rounter", "The cloud server", "My pet", "My (electronic) alarm clock", "The cell tower"]
    action = ["broke down", "caught fire", "exploded", "went missing", "got hacked", "gained consciousness and attacked me"]
    consequence = ["so I had to call a SWAT team", "so I have to deal with this and cna't come", "so I need 2 more hours", "so I need some time to try to leave alive"]

    if st.button("Generate Excuse"):
        part1 = random.choice(issue)
        part2 = random.choice(action)
        part3 = random.choice(consequence)

        if severty > 8:
            st.error("🛑 This is serious. Use this:")
            excuse = f"EMERGENCY: {part1} {part2} dangerously. I am speaking to the FBI, the Police, AND the SWAT Team."
        elif recipient == "Mom":
            st.error("Nah bro, your cooked, we cant help. The slipper never misses its target...")
        else:
            st.text("Here is your professional excuse:")
            excuse = f"I apologize for the delay. Unfortunately, {part1} {part2} {part3}"

        st.info(excuse)

        st.caption("Highlight the text, and either right-click and copy, or press Ctrl+C/Cmd+C to copy...")

with tab5:
    st.header("Mac apps by me you can check out!")
    st.caption("blazfoxx/WitheredAI are my usernames")


    st.divider()
    coll, col2 = st.columns([1, 4])

    with coll:
        st.image("GAZE.png", width=200)
    with col2:
        st.subheader("GAZE")
        st.write("Monitors your desktop, when active, and lets you revisit moments from the past")
        st.write("**Version:** 1.0 | **Size:** 1.5 MB")
        st.link_button("Download GAZE", "https://drive.google.com/uc?export=download&id=1mvNyIc8TQHp3FyteYw-Ah07BRri_kje8")

    st.divider()
    coll, col2 = st.columns([1, 4])

    with coll:
        st.image("ZapRequestDarkMode-NoBG.png", width=200)
    with col2:
        st.subheader("ZapRequest")
        st.write("Lets you send, and recieve from APIs")
        st.write("**Version:** 1.0 | **Size:** 2.5 MB")
        st.link_button("Download ZapRequest", "https://drive.google.com/uc?export=download&id=1hIcdtY6I3t3DmNK22NhImDhvEgBRomt4")

    st.divider()
    coll, col2 = st.columns([1, 4])

    with coll:
        st.image("AmbientFocusNOBG.png", width = 200)
    with col2:
        st.subheader("Ambient Focus")
        st.write("Lets you mix ambient noises together to help you study!")
        st.write("**Version:** 1.0 | **Size:** 674.5 MB")
        st.link_button("Download Ambient Focus from google drive", "https://drive.google.com/uc?export=download&id=1a_TgqmuyQWQxh7VvX9La7aYpABG__E0s")