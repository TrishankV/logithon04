# import streamlit as st
# import json

# def read_json(filename):
#     with open(filename, 'r') as f:
#         data = json.load(f)
#     return data

# def write_json(filename, data):
#     with open(filename, 'w') as f:
#         json.dump(data, f, indent=4)

# def main():
#     # Read data from st.json
#     st_data = read_json('st.json')

#     # Display data in Streamlit app
#     st.json(st_data)

#     # Allow users to edit the data
#     edited_data = st.text_area("Edit JSON Data", value=json.dumps(st_data, indent=4))

#     # Convert edited data back to JSON
#     edited_json_data = json.loads(edited_data)

#     # Button to download edited JSON data
#     if st.button("Download Edited JSON"):
#         write_json('edited_data.json', edited_json_data)
#         st.success("Edited JSON data downloaded successfully!")

# if __name__ == "__main__":
#     main()


# import streamlit as st
# import json

# data = {
#     "employees": [
#         {"name": "John Doe", "department": "Marketing", "place": "Remote"},
#         {"name": "Jane Doe", "department": "Software Engineering", "place": "Remote"},
#         {"name": "Don Joe", "department": "Software Engineering", "place": "Office"},
#     ]
# }

# json_string = json.dumps(data)

# st.json(json_string, expanded=True)

# st.download_button(
#     label="Download JSON",
#     file_name="data.json",
#     mime="application/json",
#     data=json_string,
# )

# import streamlit as st
# import json

# data = {
#     "employees": [
#         {"name": "John Doe", "department": "Marketing", "place": "Remote"},
#         {"name": "Jane Doe", "department": "Software Engineering", "place": "Remote"},
#         {"name": "Don Joe", "department": "Software Engineering", "place": "Office"},
#     ]
# }

# # Convert data dictionary to JSON string
# json_string = json.dumps(data, indent=4)

# # Text area to display and edit JSON data
# edited_json_string = st.text_area("Edit JSON Data", value=json_string, height=300)

# # Button to download edited JSON data
# if st.button("Download Edited JSON"):
#     edited_data = json.loads(edited_json_string)
#     with open("edited_data.json", "w") as f:
#         json.dump(edited_data, f, indent=4)
#     st.success("Edited JSON data downloaded successfully!")


# import streamlit as st
# import json

# def read_json_file(uploaded_file):
#     # Read the uploaded JSON file
#     with uploaded_file as f:
#         data = json.load(f)
#     return data

# # Upload JSON file
# uploaded_file = st.file_uploader("Upload JSON file", type=["json"])

# if uploaded_file is not None:
#     # Read the uploaded JSON file
#     data = read_json_file(uploaded_file)

#     # Convert data dictionary to JSON string
#     json_string = json.dumps(data, indent=4)

#     # Text area to display and edit JSON data
#     edited_json_string = st.text_area("Edit JSON Data", value=json_string, height=300)

#     # Button to download edited JSON data
#     if st.button("Download Edited JSON"):
#         edited_data = json.loads(edited_json_string)
#         with open("edited_data.json", "w") as f:
#             json.dump(edited_data, f, indent=4)
#         st.success("Edited JSON data downloaded successfully!")


# import streamlit as st
# import json
# import os

# def read_json_file(uploaded_file):
#     # Read the uploaded JSON file
#     with uploaded_file as f:
#         data = json.load(f)
#     return data

# def download_json_file(data, filename):
#     # Append 'edited' to the filename
#     filename = filename.split('.')[0] + "_edited.json"
#     # Save the edited JSON data to a new file
#     with open(filename, "w") as f:
#         json.dump(data, f, indent=4)
#     return filename

# # Upload JSON file
# uploaded_file = st.file_uploader("Upload JSON file", type=["json"])

# if uploaded_file is not None:
#     # Read the uploaded JSON file
#     data = read_json_file(uploaded_file)

#     # Convert data dictionary to JSON string
#     json_string = json.dumps(data, indent=4)

#     # Text area to display and edit JSON data
#     edited_json_string = st.text_area("Edit JSON Data", value=json_string, height=300)

#     # Button to download edited JSON data
#     if st.button("Download Edited JSON"):
#         edited_data = json.loads(edited_json_string)
#         # Get the filename from the uploaded file
#         filename = uploaded_file.name
#         # Download the edited JSON data
#         downloaded_filename = download_json_file(edited_data, filename)
#         # Provide a download link to the user
#         st.success(f"Edited JSON data downloaded as {downloaded_filename}!")

# import streamlit as st
# import json

# def read_json_file(uploaded_file):
#     # Read the uploaded JSON file
#     with uploaded_file as f:
#         data = json.load(f)
#     return data

# def download_json_file(data, filename):
#     # Append 'edited' to the filename
#     filename = filename.split('.')[0] + "_edited.json"
#     # Save the edited JSON data to a new file
#     with open(filename, "w") as f:
#         json.dump(data, f, indent=4)
#     return filename

# # Upload JSON file
# uploaded_file = st.file_uploader("Upload JSON file", type=["json"])

# if uploaded_file is not None:
#     # Read the uploaded JSON file
#     data = read_json_file(uploaded_file)

#     # Convert data dictionary to JSON string
#     json_string = json.dumps(data, indent=4)

#     # Text area to display and edit JSON data
#     edited_json_string = st.text_area("Edit JSON Data", value=json_string, height=300)

#     # Button to download edited JSON data
#     if st.button("Download Edited JSON"):
#         edited_data = json.loads(edited_json_string)
#         # Get the filename from the uploaded file
#         filename = uploaded_file.name
#         # Download the edited JSON data
#         downloaded_filename = download_json_file(edited_data, filename)
#         # Provide a download link to the user
#         st.success(f"Edited JSON data downloaded as {downloaded_filename}!")

import streamlit as st
import json

def read_json_file(uploaded_file):
    # Read the uploaded JSON file
    with uploaded_file as f:
        data = json.load(f)
    return data

def download_json_file(data, filename):
    # Append 'edited' to the filename
    filename = filename.split('.')[0] + "_edited.json"
    # Save the edited JSON data to a new file
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    return filename

# Upload JSON file
uploaded_file = st.file_uploader("Upload JSON file", type=["json"])

if uploaded_file is not None:
    # Read the uploaded JSON file
    data = read_json_file(uploaded_file)

    # Convert data dictionary to JSON string
    json_string = json.dumps(data, indent=4)

    # Text area to display and edit JSON data
    edited_json_string = st.text_area("Edit JSON Data", value=json_string, height=300)

    # Button to download edited JSON data
    if st.button("Download Edited JSON"):
        edited_data = json.loads(edited_json_string)
        # Get the filename from the uploaded file
        filename = uploaded_file.name
        # Download the edited JSON data
        downloaded_filename = download_json_file(edited_data, filename)
        # Provide a download link to the user
        st.success(f"Edited JSON data downloaded as {downloaded_filename}!")

    # Feedback buttons side by side
    st.write("Was this helpful?")
    col1, col2 = st.beta_columns(2)
    if col1.button("👍"):
        st.write("Thanks for your feedback!")
    if col2.button("👎"):
        st.write("We're sorry to hear that. Please let us know how we can improve.")


